
from pathlib import Path
import sys
import pandas as pd
import numpy as np

# Optional sklearn use
try:
    from sklearn.preprocessing import StandardScaler
    _HAS_SKLEARN = True
except Exception:
    _HAS_SKLEARN = False

DEFAULT_DIR = Path("/Users/prakashramesh/Git repot for IITM/Prakash_IITM/Data")


def find_csv_files(data_dir: Path):
    return sorted(data_dir.glob("*.csv"))


def load_and_concat(csv_paths):
    dfs = []
    for p in csv_paths:
        try:
            df = pd.read_csv(p)
            print(f"Loaded {p.name} shape={df.shape}")
            dfs.append(df)
        except Exception as e:
            print(f"Failed to read {p}: {e}")
    if not dfs:
        return pd.DataFrame()
    if len(dfs) == 1:
        return dfs[0].copy()
    return pd.concat(dfs, ignore_index=True, sort=False)


def clean_column_names(df: pd.DataFrame):
    df = df.copy()

    def clean(c):
        c2 = str(c).strip()
        c2 = c2.lower()
        c2 = c2.replace(" ", "_")
        c2 = c2.replace("-", "_")
        c2 = "".join(ch for ch in c2 if ch.isalnum() or ch == "_")
        return c2
    df.columns = [clean(c) for c in df.columns]
    return df


def coerce_types(df: pd.DataFrame):
    df = df.copy()
    # Trim whitespace from object/string columns
    obj_cols = df.select_dtypes(include=["object"]).columns.tolist()
    for c in obj_cols:
        df[c] = df[c].astype(str).str.strip().replace({"nan": np.nan})
    # Parse dates for columns with 'date' in name
    for c in df.columns:
        if "date" in c:
            df[c] = pd.to_datetime(df[c], errors="coerce")
    # Coerce numbers
    for c in df.columns:
        if c in obj_cols:
            # try convert object columns with mostly numeric-looking values
            converted = pd.to_numeric(df[c], errors="coerce")
            non_na = converted.notna().sum()
            if non_na > 0 and non_na / max(1, len(df)) >= 0.5:
                df[c] = converted
    # Final dtype hinting
    return df


def handle_missing(df: pd.DataFrame, drop_threshold=0.6):
    df = df.copy()
    # Drop columns with too many missing values
    missing_frac = df.isna().mean()
    drop_cols = missing_frac[missing_frac > drop_threshold].index.tolist()
    if drop_cols:
        print(
            f"Dropping columns with >{int(drop_threshold*100)}% missing: {drop_cols}")
        df = df.drop(columns=drop_cols)

    # Fill numeric with median
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    for c in num_cols:
        if df[c].isna().any():
            med = df[c].median()
            df[c] = df[c].fillna(med)

    # Fill categorical/object with mode (or 'unknown')
    obj_cols = df.select_dtypes(
        include=["object", "category"]).columns.tolist()
    for c in obj_cols:
        if df[c].isna().any():
            try:
                mode = df[c].mode(dropna=True)[0]
            except Exception:
                mode = None
            df[c] = df[c].fillna(mode if pd.notna(mode) else "unknown")

    # For datetimes, fill with earliest date if missing (or leave)
    dt_cols = df.select_dtypes(include=["datetime64"]).columns.tolist()
    for c in dt_cols:
        if df[c].isna().any():
            min_dt = df[c].min()
            if pd.notna(min_dt):
                df[c] = df[c].fillna(min_dt)
    return df


def drop_duplicates(df: pd.DataFrame):
    before = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    after = len(df)
    print(f"Dropped {before-after} duplicate rows")
    return df


def encode_categoricals(df: pd.DataFrame, one_hot_thresh=20):
    df = df.copy()
    obj_cols = df.select_dtypes(
        include=["object", "category"]).columns.tolist()
    for c in obj_cols:
        n_unique = df[c].nunique(dropna=True)
        if n_unique == 0:
            df = df.drop(columns=[c])
            continue
        if n_unique <= one_hot_thresh:
            dummies = pd.get_dummies(
                df[c], prefix=c, dummy_na=False, dtype=np.uint8)
            df = pd.concat([df.drop(columns=[c]), dummies], axis=1)
        else:
            # use ordered categorical codes
            df[c] = df[c].astype("category").cat.codes.replace({-1: np.nan})
    return df


def scale_numeric(df: pd.DataFrame):
    df = df.copy()
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if not num_cols:
        return df
    if _HAS_SKLEARN:
        scaler = StandardScaler()
        df[num_cols] = scaler.fit_transform(df[num_cols])
        print("Scaled numeric columns with sklearn StandardScaler")
    else:
        # z-score by hand
        for c in num_cols:
            mean = df[c].mean()
            std = df[c].std()
            if std == 0 or np.isnan(std):
                df[c] = 0.0
            else:
                df[c] = (df[c] - mean) / std
        print("Scaled numeric columns with manual z-score")
    return df


def save_outputs(df: pd.DataFrame, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "cleaned_data.csv"
    parquet_path = out_dir / "cleaned_data.parquet"
    df.to_csv(csv_path, index=False)
    try:
        df.to_parquet(parquet_path, index=False)
    except Exception as e:
        print(f"Parquet write failed (optional): {e}")
    print(f"Wrote cleaned CSV: {csv_path}")
    print(f"Wrote cleaned PARQUET (if supported): {parquet_path}")


def main(data_dir: Path):
    if not data_dir.exists():
        print(f"Data directory does not exist: {data_dir}")
        return
    csvs = find_csv_files(data_dir)
    if not csvs:
        print(f"No CSV files found in {data_dir}")
        return
    df = load_and_concat(csvs)
    if df.empty:
        print("No data loaded; exiting")
        return
    print(f"Initial shape: {df.shape}")
    df = clean_column_names(df)
    df = coerce_types(df)
    df = drop_duplicates(df)
    df = handle_missing(df)
    df = encode_categoricals(df)
    df = scale_numeric(df)
    print(f"Final shape: {df.shape}")
    out_dir = data_dir / "cleaned"
    save_outputs(df, out_dir)


if __name__ == "__main__":
    arg = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DIR
    main(arg)
