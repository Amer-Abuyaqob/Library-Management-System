from library_item import LibraryItem
from user import User
from reservable import Reservable
from exceptions import InvalidDataTypeError, InvalidValueError

class Book(LibraryItem, Reservable):
    counter = 0  # counts every object created from this class
    # FIXME: add reserved as an attribute and refactor all of the methods accordingly
    def __init__(self, title, author, year, available, genre):
        super().__init__(title, author, year, available)

        try:
            self.__validate_genre(genre)
            self.__genre = genre
            self.__reserved: User | None = None
            Book.counter += 1
            self.__book_num = Book.counter
            self._id = self._item_id()  # Initialize auto generated ID

        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")
        except InvalidValueError as value:
            print(f"Caught: {value}")
            

    def __validate_genre(self, genre):
        """
        Validate the genre parameter for a book.
        
        Args:
            genre: The genre to validate
            
        Raises:
            InvalidDataTypeError: If genre is not a string
            InvalidValueError: If genre is empty or contains only whitespace
        """
        if not isinstance(genre, str):
            raise InvalidDataTypeError("string", type(genre).__name__)
            
        if not genre.strip():
            raise InvalidValueError("Genre must be a non-empty string")

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
        try:
            self.__validate_genre(genre)
            self.__genre = genre
            return True
        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")
            return False
        except InvalidValueError as value:
            print(f"Caught: {value}")
            return False

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
        self.__reserved = user
