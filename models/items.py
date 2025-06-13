from .library_item import LibraryItem, Reservable
from exceptions.CustomeExceptions import ItemNotAvailableError, UserNotFoundError, FileNotFoundError, ItemNotFoundError

class Book(LibraryItem, Reservable):
    def __init__(self, item_id,title,auther,is_available,isbn,reserved_by=None):
        super().__init__(item_id, title, auther, is_available)
        self.isbn = isbn
        self.reserved_by = reserved_by 

    def display_info(self):
        available = "Yes" if self.is_available else "No, it's Borrowed"
        print(f"Book ID:{self.item_id}, Title: {self.title}, Author: {self.auther}, ISBN: {self.isbn}, Available: {available}")

    def reserve(self, user):
        if self.reserved_by: # Check if the book is already reserved
            raise ItemNotAvailableError(f"{self.title} is not available for reservation.")
        self.reserved_by = user.user_id 
        print(f"{self.title} has been reserved by {user.name}.")

class Magazine(LibraryItem):
    def __init__(self,item_id,title,auther,is_available,issn,year):
        super().__init__(item_id,title,auther,is_available)
        self.issn=issn
        self.year=year

    def display_info(self):
        available = "Yes" if self.is_available else "No, it's Borrowed"
        print(f"Magazine ID:{self.item_id}, Title: {self.title}, Author: {self.auther}, ISSN: {self.issn}, Year: {self.year}, Available: {available}")



class DVD(LibraryItem, Reservable):
    def __init__(self, item_id,title,auther,is_available,director,reserved_by=None):
        super().__init__(item_id, title, auther, is_available)
        self.director = director
        self.reserved_by = reserved_by 

    def display_info(self):
        available = "Yes" if self.is_available else "No, it's Borrowed"
        print(f"DVD ID:{self.item_id}, Title: {self.title}, Director: {self.director}, Available: {available}")

    def reserve(self, user):
        if self.reserved_by: # Check if the DVD is already reserved
            raise ItemNotAvailableError(f"{self.title} is not available for reservation.")
        self.reserved_by = user.user_id 
        print(f"{self.title} has been reserved by {user.name}.")        
