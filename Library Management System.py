import datetime

print()
print ("Hello!!")
print ('This is your Library Management System')

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = 'available'
        self.borrow_date = None
        self.return_date = None

class Library:
    
    def __init__(self):
        self.books = []
        
#adding_new_books
    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")
        
#borrow_books        
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == 'available':
                    book.status = 'borrowed'
                    book.borrow_date = datetime.datetime.now()
                    print(f"You have borrowed '{book.title}' on {book.borrow_date}")
                else:
                    print(f"The book '{book.title}' is already borrowed.")
                return
        print("Book not found.")
        
#return_book
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == 'borrowed':
                    book.status = 'available'
                    book.return_date = datetime.datetime.now()
                    print(f"You have returned '{book.title}' on {book.return_date}")
                else:
                    print(f"The book '{book.title}' was not borrowed.")
                return
        print("Book not found.")
        
#view_available_books
    def view_available_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.status == 'available':
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")


                    
#view_borrow_books
    def view_borrowed_books(self):
        print("\nBorrowed Books:")
        for book in self.books:
            if book.status == 'borrowed':
                    print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add New Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Available Books")
        print("5. View Borrowed Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the book's title: ")
            author = input("Enter the book's author: ")
            isbn = input("Enter the book's ISBN: ")
            library.add_book(title, author, isbn)
        elif choice == '2':
            isbn = input("Enter the book's ISBN to borrow: ")
            library.borrow_book(isbn)
        elif choice == '3':
            isbn = input("Enter the book's ISBN to return: ")
            library.return_book(isbn)
        elif choice == '4':
            library.view_available_books()
        elif choice == '5':
            library.view_borrowed_books()
        elif choice == '6':
            print ('Leaving the system.Have a great day!')
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
