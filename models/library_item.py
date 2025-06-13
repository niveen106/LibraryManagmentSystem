from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self,item_id,title,auther,is_available=True):
        self.item_id=item_id
        self.title=title
        self.auther=auther
        self.is_available=is_available

    @abstractmethod
    def display_info(self):
        pass

    def check_availability(self):
        return self.is_available

class Reservable(ABC):
    @abstractmethod
    def reserve(self, user):
        pass
 