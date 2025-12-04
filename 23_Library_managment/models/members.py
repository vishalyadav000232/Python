from .base import Base

class Member(Base):
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id

    @property
    def name(self):
        return self.__name
    
    @property
    def member_id(self):
        return self.__member_id
        
    def save(self):
        with open("23_Library_managment/database/members.txt", "a") as f:
            f.write(f"{self.__name},{self.__member_id}\n")
    
    def __str__(self):
        return f"{self.__name}, ({self.__member_id})"
