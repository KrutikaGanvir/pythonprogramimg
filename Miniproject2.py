# ---------------------------------MINI PROJECT NO.2-------------------------------------

# -------------------------- Create a simple library system.----------------------
class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book_name):
           self.books.append(book_name)
           print(book_name,"added successfully")

    def issue_book(self,book_name):
        if book_name in self.books:
           self.books.remove(book_name)
           print(book_name,"issued succesfully") 
        else:
            print("Book is not available")

    def return_book(self,book_name):
        self.books.append(book_name)
        print(book_name,"returned succesfully") 

    def display_book(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(book)    

Library =  Library()
Library.add_book("Python Basics")
Library.add_book("C++ Programming")
Library.add_book("Java Programming")
Library.issue_book("Python Basics")
Library.return_book("Python Basics")
Library.display_book()
