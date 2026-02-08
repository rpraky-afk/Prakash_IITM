class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year, **details):
        book = {
            "title": title,
            "author": author,
            "year": year,
        }
        book.update(details)
        self.books.append(book)

    def search_books(self, criteria):
        return [book for book in self.books if criteria(book)]

    def calculate_stats(self):
        if not self.books:
            return 0, None, None, None
        years = [book['year'] for book in self.books]
        avg_year = sum(years) / len(years)
        min_year = min(years)
        max_year = max(years)
        total_books = len(self.books)
        return avg_year, min_year, max_year, total_books

    def filter_books(self, condition):
        return [book for book in self.books if condition(book)]

    def sorted_books(self, key, reverse=False):
        return sorted(self.books, key=lambda book: book[key], reverse=reverse)


print("=" * 50)
print("📚 LIBRARY MANAGEMENT SYSTEM")
print("=" * 50)

library = Library()


library.add_book("To Kill a Mockingbird", "Harper Lee",
                 1960, genre="Fiction", pages=281)
library.add_book("1984", "George Orwell", 1949, genre="Dystopian", pages=328)
library.add_book("The Great Gatsby", "F. Scott Fitzgerald",
                 1925, genre="Classic", pages=180)

# display all books
print("\nAll Books in the Library:")
for book in library.books:
    print(book)

# calculate and display statistics
avg_year, min_year, max_year, total_books = library.calculate_stats()
print(
    f"\nLibrary Statistics:\nTotal Books: {total_books}\nAverage Publication Year: {avg_year}\nOldest Book Year: {min_year}\nNewest Book Year: {max_year}")
# search for books by author
author_search = "George Orwell"
found_books = library.search_books(
    lambda book: book['author'] == author_search)
print(f"\nBooks by {author_search}:")
for book in found_books:
    print(book)

# search for books published after a certain year
year_threshold = 1950
recent_books = library.filter_books(lambda book: book['year'] > year_threshold)
print(f"\nBooks published after {year_threshold}:")
for book in recent_books:
    print(book)

# sort by publication year
sorted_by_year = library.sorted_books('year')
print("\nBooks sorted by Publication Year:")
for book in sorted_by_year:
    print(book)

# books sorted by title z to a
sorted_by_title_desc = library.sorted_books('title', reverse=True)
print("\nBooks sorted by Title (Z to A):")
for book in sorted_by_title_desc:
    print(book)
