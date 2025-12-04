from ..models.book import Book
from ..models.members import Member

import os

class Services:
    def __init__(self):
        self.books = []
        self.members = []

    # Load books from file
    def loads_books(self):
        path = "23_Library_managment/database/books.txt"
        if not os.path.exists(path):
            open(path, "w").close()

        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line :
                    continue
                parts = line.split(",")
                if len(parts) != 3:
                    continue

                title, author, book_id, issued_to = parts
                book = Book(title, author, book_id)
                if issued_to != "None":
                    book.issued_to = issued_to
                self.books.append(book)

    # Load members from file
    def load_members(self):
        path = "23_Library_managment/database/members.txt"
        if not os.path.exists(path):
            open(path, "w").close()

        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 2:
                    continue
                print(f"Skipping invalid line: {line}")
                name, member_id = parts
                self.members.append(Member(name, member_id))

    # Add new book
    def add_book(self, title, author, book_id):
        book = Book(title, author, book_id)
        book.save()
        self.books.append(book)
        return book

    # Add new member
    def add_member(self, name, member_id):
        member = Member(name, member_id)
        member.save()
        self.members.append(member)
        return member

    # Issue a book
    def issue_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if book is None:
            return "Book not found"
        if member is None:
            return "Member not found"
        if book.is_issued:
            return "Book already issued"

        book.issued_to = member_id
        self._update_books_file()
        return f"Book issued to {member.name}"

    # Return a book
    def return_book(self, book_id):
        book = self.find_book(book_id)

        if book is None:
            return "Book not found"
        if not book.is_issued:
            return "Book was not issued"

        book.issued_to = None
        self._update_books_file()
        return "Book returned successfully"

    # Find book by ID
    def find_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                return b
        return None

    # Find member by ID
    def find_member(self, member_id):
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None

    # Update books file
    def _update_books_file(self):
        path = "23_Library_managment/database/books.txt"
        with open(path, "w") as f:
            for b in self.books:
                issued = b.issued_to if b.issued_to else "None"
                f.write(f"{b.title},{b.author},{b.book_id},{issued}\n")

    # View books
    def view_books(self):
        print("\n---- Book List ----")
        for b in self.books:
            print(b)

    # View members
    def view_members(self):
        print("\n---- Members List ----")
        for m in self.members:
            print(m)
