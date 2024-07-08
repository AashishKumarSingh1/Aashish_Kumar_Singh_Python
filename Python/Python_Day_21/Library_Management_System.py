class Book:

    def __init__(self,title,author,isbn) -> None:
        self.title=title
        self.author=author
        self.isbn=isbn

    def __str__(self) -> str:
        return f"Book(title : {self.title} , Author :{self.author} , ISBN : {self.isbn})"
    
    def __eq__(self, other: object) -> bool:
        return self.isbn==other.isbn 
      

class Member:

    def __init__(self,name,member):
        self.name=name
        self.member=member
        self.borrowed=[]

    def borrow_book(self,book):
        self.borrowed.append(book)

    def return_book(self,book):
        self.borrowed.remove(book)
    
    def __str__(self) -> str:
        return f"Member(Name:{self.name} , ID: {self.member} , Borrowed Books:{len(self.borrowed)})"


class Library:

    def __init__(self) -> None:
        self.books=[]
        self.members=[]

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self,isbn):
        self.books=[book for book in self.books if book.isbn != isbn]

    def register_member(self,member):
        self.members.append(member)

    def deregister_member(self,member_id):
        self.members=[member for member in self.members if member.member !=member_id]

    # ------------------------------------------------------------------#

    def borrow_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if member and book:
            member.borrow_book(book)
            self.books.remove(book)
            return True
        return False

    def return_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member == member_id), None)
        if member:
            book = next((b for b in member.borrowed if b.isbn == isbn), None)
            if book:
                member.return_book(book)
                self.books.append(book)
                return True
        return False

    def display_books(self):
        for book in self.books:
            print(book)

    def display_members(self):
        for member in self.members:
            print(member)

    #-----------------------------------------------------------------------#

# Create some books
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

# Create some members
member1 = Member("Alice", "M001")
member2 = Member("Bob", "M002")

# Create a library
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)

# Register members
library.register_member(member1)
library.register_member(member2)
print()

# Display books and members
library.display_books()
library.display_members()
print()

# Borrow a book
library.borrow_book("M001", 1234567890)
library.display_books()
library.display_members()
print()

# Return a book
library.return_book("M001", 1234567890)
library.display_books()
library.display_members()
print()