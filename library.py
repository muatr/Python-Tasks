class File:
    def __init__(self, library):
        self.file = open(library, "a+")
        self.books = []
    
    def add_book(self, book):
        for i in range(len(self.books)):
            if self.books[i].title == title:
                print("\nThe entered book already exists!!!")
                return 0
        self.books.append(book)

    def remove_book(self, title):
        for i in range(len(self.books)):
            if self.books[i].title == title:
                temp = self.books[i].title
                self.books.pop(i)
                return temp

    def list_books(self):
        if self.books:
            for i in self.books:
                print(f"Book: {i.title}, Author: {i.author}")
        else:
            print("No books found!!!")

class Book:
    def __init__(self, title, author, year, page):
        self.title = title
        self.author = author
        self.year = year
        self.page = page
        
library = File("library.txt")
choice = 0

while choice != 4:
    choice = int(input("\n*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book\n4) Quit\nEnter your choice: "))
    
    if choice == 1:
        print("\n*** Book List ***")
        library.list_books()
        
    elif choice == 2:
        title = input("\nEnter the book title: ")
        author = input("Enter the author: ")
        year = input("Enter the release year: ")
        page = input("Enter the number of pages: ")
        book = Book(title, author, year, page)
        library.add_book(book)
        
    elif choice == 3:
        if library.books:
            print("Removed book's title: ", library.remove_book(input("\nEnter the book title to remove: ")))
        else:
            print("\nThere are no books to remove!!!")

    else:
        if choice != 4:
            print("\nPlease enter a valid number (1-4) !!!")