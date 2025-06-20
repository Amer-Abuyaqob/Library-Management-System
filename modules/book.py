from library_item import LibraryItem
from modules.user import User
from reservabale import Reservable

class Book(LibraryItem, Reservable):
    def __init__(self, title, author, year, available, genre):
        super().__init__(title, author, year, available)
        self.__genre = genre
        self.__reserved = None

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    def reserve(self, user: User):
        """
        Reserve the book for a specific user.

        Args:
            user (User): The user who is reserving the book.

        Sets the __reserved attribute to the given user, indicating that the book is reserved by this user.
        """
        self.__reserved = user