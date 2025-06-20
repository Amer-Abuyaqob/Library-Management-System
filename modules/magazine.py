from library_item import LibraryItem
from user import User
from reservable import Reservable

class Magazine(LibraryItem, Reservable):
    counter = 0
    def __init__(self, title, author, year, available, genre):
        super().__init__(title, author, year, available)
        self.__genre = genre
        self.__reserved: User | None = None
        Magazine.counter += 1
        self.__magazine_num = Magazine.counter
        self._id = self._item_id()  # Initialize auto generated ID 

    def _item_id(self):
        """
        Auto generation of item IDs bassed on the item's type
        Format: T-AA-YYYY-N
            T: Item's type -> M: magazine
            AA: Author's first name initials
            YYYY: Publish year
            N: Item number
        """
        return f"M-{super()._item_id()}-{self.__magazine_num}"

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    def display_info(self):
        return f'''
        Item type: Magazine
        Title: {self.title}
        Author: {self.author}
        Year: {self.year}
        Available: {self.available}
        Genre: {self.genre}
        '''

    def check_availability(self):
        return self.available

    @property
    def reserved_by(self) -> User | None:
        return self.__reserved

    def reserve(self, user: User) -> None:
        """Mark the magazine as reserved by ``user``."""
        self.__reserved = user
