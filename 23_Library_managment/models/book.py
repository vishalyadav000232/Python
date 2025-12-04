from .base import Base


class Book (Base):
    def __init__(self , title , author , book_id):
        self.__title = title
        self.__author= author
        self.__book_id = book_id
        self.issued_to = None

    @property
    def title(self):
        return self.__title
    @property
    def author(self):
        return self.__author
    @property
    def book_id(self):
        return self.__book_id
    @property
    def is_issues(self):
        return self.is_issues
    


    def save(self):
        with open("23_Library_managment/database/books.txt", "a") as file:
            file.write(f"{self.__title} , {self.__author} , {self.__book_id} , None\n")

    def __str__(self):
        status = f" Issued to {self.issued_to}" if self.issued_to else "Availble"
        return f"[{self.__book_id}  {self.__title} by {self.__author} | {status}]"
            
        
