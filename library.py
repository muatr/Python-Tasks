# Store library data
class File:
    def __init__(self, library):
        # Open the file
        self.file = open(library, "a+")
        self.books = []
    
    def add_book(self, book):
        # Check if there is a book with the same title
        for i in range(len(self.books)):
            if self.books[i].title == title:
                print("\nThe entered book already exists!!!")
                return 0
        self.books.append(book) # Add the new book to the list

    def remove_book(self, title):
        # Find and delete the book from the list
        for i in range(len(self.books)):
            if self.books[i].title == title:
                print("Removed book's title: ", self.books[i].title)
                self.books.pop(i)
                return 1
        print(f"There is no book with title {title} on the list!!!") # If no such book found

    def list_books(self):
        # Print all books in the library
        if self.books:
            for i in self.books:
                print(f"Book: {i.title}, Author: {i.author}, Year: {i.year}, Page: {i.page}")
        else: #  If the library is empty
            print("No books found!!!")

#  Create an object of class 'File'
class Book:
    def __init__(self, title, author, year, page):
        self.title = title
        self.author = author
        self.year = year
        self.page = page
        
library = File("library.txt") #  Create a file object
choice = 0 #  Initialize choice variable

while choice != 4: #  Get user input
    choice = int(input("\n*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book\n4) Quit\nEnter your choice: "))
    
    if choice == 1: # List books
        print("\n*** Book List ***")
        library.list_books()
        
    elif choice == 2: # Add a book
        title = input("\nEnter the book title: ")
        author = input("Enter the author: ")
        while True: # Ensure that the entered number is integer
            year = input("Enter the release year: ")
            try:
                if(int(year)):
                    break
            except:
                print("Please enter a valid number!!!")
        while True: # Ensure that the entered number is integer
            page = input("Enter the number of pages: ")
            try:
                if(int(page)):
                    break
            except:
                print("Please enter a valid number!!!")
        # Create a new book object and add it to the library
        book = Book(title, author, year, page)
        library.add_book(book)
        
    elif choice == 3: # Check if  there are any books in the library
        if library.books:
            library.remove_book(input("\nEnter the book title to remove: "))
        else:
            print("\nThere are no books to remove!!!")

    else:
        if choice != 4: # If the specified numbers are not entered
            print("\nPlease enter a valid number (1-4) !!!")