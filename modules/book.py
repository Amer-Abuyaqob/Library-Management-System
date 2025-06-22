from library_item import LibraryItem
from user import User
from reservable import Reservable
from errors import ItemNotAvailableError

class Book(LibraryItem, Reservable):
    counter = 0  # counts every object created from this class

    def __init__(self, title, author, year, available, genre):
        super().__init__(title, author, year, available)
        self.__genre = genre
        self.__reserved: User | None = None
        Book.counter += 1
        self.__book_num = Book.counter
        self._id = self._item_id()  # Changed from __id to _id

    def _item_id(self):
        """
        Auto generation of item IDs based on the item's type
        Format: T-AA-YYYY-N
            T: Item's type -> B: book
            AA: Author's first name initials
            YYYY: Publish year
            N: Item number
        """
        return f"B-{super()._item_id()}-{self.__book_num}"

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    def display_info(self):
        return f'''
        Item type: Book
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
        """Mark the book as reserved by ``user``."""
        if user is None or not isinstance(user, User):
            raise TypeError("user must be a non-null User instance")
        if self.__reserved is not None:
            raise ItemNotAvailableError(
                f"Book '{self.id}' is already reserved")
        self.__reserved = user

    def cancel_reservation(self) -> None:
        """Cancel any existing reservation."""
        self.__reserved = None
