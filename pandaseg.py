import pandas as pd
import numpy as np
df = pd.read_csv(
    "/Users/prakashramesh/Git repot for IITM/Prakash_IITM/Data/HR_Employee attrition_dirty.csv")
print(df.head())
print(df.columns)
print(df.dtypes)
print(df.describe())
print(df.isnull().sum())
print(df["Attrition"].value_counts())
print(df["Department"].value_counts())
print(df.shape)
