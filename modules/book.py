from library_item import LibraryItem
from user import User
from reservabale import Reservable

class Book(LibraryItem, Reservable):
    counter = 0 # counts every object created from this class
    def __init__(self, title, author, year, available, genre):
        super().__init__(title, author, year, available)
        self.__genre = genre
        self.__reserved = None
        Book.counter += 1
        self.__book_num = Book.counter
        self._id = self._item_id()  # Changed from __id to _id

    def _item_id(self):
        """
        Auto generation of item IDs bassed on the item's type
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

    def reserve(self, user: User):
        """
        Reserve the book for a specific user.

        Args:
            user (User): The user who is reserving the book.

        Sets the __reserved attribute to the given user, indicating that the book is reserved by this user.
        """
        self.__reserved = user

if __name__ == "__main__":
    book = Book("seso", "aMer", 2010, True, "Fiction")
    print(book.id)