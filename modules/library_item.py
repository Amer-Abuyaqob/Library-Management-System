from abc import ABC, abstractmethod

from exceptions import InvalidDataTypeError, InvalidValueError

class LibraryItem(ABC):
    def __init__(self, title, author, year, available):
        super().__init__()

        self.__validate_title(title)
        self.__title = title

        self.__validate_author(author)
        self.__author = author

        self.__validate_year(year)
        self.__year = year
        
        self.__validate_available(available)
        self.__available = available
        self._id = ""

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    @property
    def available(self):
        return self.__available

    @property
    def id(self):
        return self._id

    @title.setter
    def title(self, title):
        self.__validate_title(title)
        self.__title = title

    @author.setter
    def author(self, author):
        self.__validate_author(author)
        self.__author = author

    @year.setter
    def year(self, year):
        self.__validate_year(year)
        self.__year = year

    @available.setter
    def available(self, available):
        self.__validate_available(available)
        self.__available = available
        
    @abstractmethod
    def display_info(self):
        """
        Display information about the library item.
        Should be implemented by subclasses.
        """
        pass

    @abstractmethod
    def check_availability(self):
        """
        Check if the item is available.
        Should be implemented by subclasses.
        """
        pass
    
    def __validate_title(self, title):
        """
        Validate the title parameter for a library item.
        
        Args:
            title: The title to validate
            
        Raises:
            InvalidDataTypeError: If title is not a string
            InvalidValueError: If title is empty or contains only whitespace
        """
        if not isinstance(title, str):
            raise InvalidDataTypeError("string", type(title).__name__)
            
        if not title.strip():
            raise InvalidValueError("Title must be a non-empty string") 

    def __validate_author(self, author):
        """
        Validate the author parameter for a library item.
        
        Args:
            author: The author name to validate
            
        Raises:
            InvalidDataTypeError: If author is not a string
            InvalidValueError: If author is empty, contains only whitespace, or has less than 2 characters
        """
        if not isinstance(author, str):
            raise InvalidDataTypeError("string", type(author).__name__)
            
        if not author.strip() or len(author.strip()) < 2:
            raise InvalidValueError("Author's name must be a non-empty string with at least two characters.")

    def __validate_year(self, year):
        """
        Validate the year parameter for a library item.
        
        Args:
            year: The publication year to validate
            
        Raises:
            InvalidDataTypeError: If year is not an integer
            InvalidValueError: If year is not a positive non-zero integer
        """
        if not isinstance(year, int):
            raise InvalidDataTypeError("integer", type(year).__name__)

        if year <= 0:
            raise InvalidValueError("Year must be a positive non-zero integer")

    def _item_id(self):
        """
        Auto generation of item IDs based on the item's type
        Format: T-Aa-YYYY-N
            T: Item's type -> {B: book, D: DVD, M: Magazine}
            Aa: Author's initials (first character of each word)
            YYYY: Publish year
            N: Item number (implemented by subclasses)
        """
        return f"{self.__author_initials()}-{self.__year}"
    
    def __author_initials(self):
        """Generate author initials from the first character of each word in the author's name."""
        words = self.__author.strip().split()
        if len(words) >= 2:
            # Take first character of first and last word
            return f"{words[0][0].upper()}{words[-1][0].upper()}"
        else:
            # If single word, take first two characters
            return f"{self.__author[0].upper()}{self.__author[1].lower()}"

    def __validate_available(self, available):
        """
        Validate the available parameter for a library item.
        
        Args:
            available: The availability status to validate
            
        Raises:
            InvalidDataTypeError: If available is not a boolean
        """
        if not isinstance(available, bool):
            raise InvalidDataTypeError("bool", type(available).__name__)