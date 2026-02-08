# library management system
# 1. Add Book
# 2. Remove Book
# 3. Search Book
# 4. Display All Books
# 5. Exit
library = []
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        book_name = input("Enter book name to add: ")
        library.append(book_name)
        print(f'"{book_name}" added to the library.')

    elif choice == '2':
        book_name = input("Enter book name to remove: ")
        if book_name in library:
            library.remove(book_name)
            print(f'"{book_name}" removed from the library.')
        else:
            print(f'"{book_name}" not found in the library.')

    elif choice == '3':
        book_name = input("Enter book name to search: ")
        if book_name in library:
            print(f'"{book_name}" is available in the library.')
        else:
            print(f'"{book_name}" is not available in the library.')

    elif choice == '4':
        if library:
            print("Books in the library:")
            for book in library:
                print(f"- {book}")
        else:
            print("The library is empty.")

    elif choice == '5':
        print("Exiting the Library Management System.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
