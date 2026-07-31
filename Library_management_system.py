class Book:
    def __init__(self, title):
        self.title = title
        self.is_issued = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        book = Book(title)
        self.books.append(book)
        print(f'"{title}" added successfully.')

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'"{title}" removed successfully.')
                return
        print("Book not found.")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_issued:
                    book.is_issued = True
                    print(f'"{title}" issued successfully.')
                else:
                    print("Book already issued.")
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_issued:
                    book.is_issued = False
                    print(f'"{title}" returned successfully.')
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books in library.")
            return

        print("\nLibrary Books:")
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(f"{book.title} - {status}")


library = Library()

while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        library.add_book(title)

    elif choice == "2":
        title = input("Enter book title: ")
        library.remove_book(title)

    elif choice == "3":
        title = input("Enter book title: ")
        library.issue_book(title)

    elif choice == "4":
        title = input("Enter book title: ")
        library.return_book(title)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")