"""
Library Item Abstract Base Class Module

This module defines the abstract base class for all library items in the system.
LibraryItem serves as the foundation for Book, DVD, and Magazine classes, providing
common functionality and enforcing a consistent interface across all item types.

The class implements:
- Common attributes (title, author, year, availability)
- Input validation for all attributes
- Property getters and setters with validation
- Abstract methods that must be implemented by subclasses
- Automatic ID generation based on item characteristics

All library items inherit from this class and must implement the abstract methods
display_info() and check_availability().
"""

from abc import ABC, abstractmethod

from exceptions import InvalidDataTypeError, InvalidValueError

class LibraryItem(ABC):
    """
    Abstract base class for all library items.
    
    This class provides the common interface and functionality for all items
    in the library system. It enforces consistent behavior across different
    item types while allowing for type-specific implementations.
    
    Attributes:
        title (str): The title of the item
        author (str): The author/creator of the item
        year (int): The publication year
        available (bool): Whether the item is available for borrowing
        id (str): Unique identifier for the item (auto-generated or custom)
    
    Abstract Methods:
        display_info(): Return formatted information about the item
        check_availability(): Return the availability status
    """
    
    def __init__(self, title, author, year, available):
        """
        Initialize a library item with basic attributes.
        
        All parameters are validated before assignment to ensure data integrity.
        
        Args:
            title (str): The title of the item (non-empty string)
            author (str): The author/creator of the item (at least 2 characters)
            year (int): The publication year (positive integer)
            available (bool): Whether the item is available for borrowing
            
        Raises:
            InvalidDataTypeError: If any parameter has the wrong data type
            InvalidValueError: If any parameter has an invalid value
        """
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
        """
        Get the title of the item.
        
        Returns:
            str: The item's title
        """
        return self.__title

    @property
    def author(self):
        """
        Get the author of the item.
        
        Returns:
            str: The item's author/creator
        """
        return self.__author

    @property
    def year(self):
        """
        Get the publication year of the item.
        
        Returns:
            int: The item's publication year
        """
        return self.__year

    @property
    def available(self):
        """
        Get the availability status of the item.
        
        Returns:
            bool: True if the item is available for borrowing, False otherwise
        """
        return self.__available

    @property
    def id(self):
        """
        Get the unique identifier of the item.
        
        Returns:
            str: The item's unique ID
        """
        return self._id

    @title.setter
    def title(self, title):
        """
        Set the title of the item with validation.
        
        Args:
            title (str): The new title (non-empty string)
            
        Raises:
            InvalidDataTypeError: If title is not a string
            InvalidValueError: If title is empty or contains only whitespace
        """
        self.__validate_title(title)
        self.__title = title

    @author.setter
    def author(self, author):
        """
        Set the author of the item with validation.
        
        Args:
            author (str): The new author (at least 2 characters)
            
        Raises:
            InvalidDataTypeError: If author is not a string
            InvalidValueError: If author is empty or has less than 2 characters
        """
        self.__validate_author(author)
        self.__author = author

    @year.setter
    def year(self, year):
        """
        Set the publication year of the item with validation.
        
        Args:
            year (int): The new publication year (positive integer)
            
        Raises:
            InvalidDataTypeError: If year is not an integer
            InvalidValueError: If year is not a positive non-zero integer
        """
        self.__validate_year(year)
        self.__year = year

    @available.setter
    def available(self, available):
        """
        Set the availability status of the item with validation.
        
        Args:
            available (bool): The new availability status
            
        Raises:
            InvalidDataTypeError: If available is not a boolean
        """
        self.__validate_available(available)
        self.__available = available
        
    @abstractmethod
    def display_info(self):
        """
        Display information about the library item.
        
        This abstract method must be implemented by subclasses to provide
        formatted information about the specific item type.
        
        Returns:
            str: Formatted string containing item information
        """
        pass

    @abstractmethod
    def check_availability(self):
        """
        Check if the item is available.
        
        This abstract method must be implemented by subclasses to provide
        the current availability status of the item.
        
        Returns:
            bool: True if the item is available, False otherwise
        """
        pass
    
    def __validate_title(self, title):
        """
        Validate the title parameter for a library item.
        
        Ensures the title is a non-empty string with actual content.
        
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
        
        Ensures the author is a string with at least 2 characters.
        
        Args:
            author: The author name to validate
            
        Raises:
            InvalidDataTypeError: If author is not a string
            InvalidValueError: If author is empty, contains only whitespace, or has less than 2 characters
        """
        if not isinstance(author, str):
            raise InvalidDataTypeError("string", type(author).__name__)
            
        if len(author.strip()) < 2:
            raise InvalidValueError("Author's name must be a non-empty string with at least two characters.")

    def __validate_year(self, year):
        """
        Validate the year parameter for a library item.
        
        Ensures the year is a positive integer representing a valid publication year.
        
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
        Generate the base part of an item ID.
        
        Creates a standardized ID format based on the item's characteristics.
        Format: T-Aa-YYYY-N
            T: Item's type (implemented by subclasses)
            Aa: Author's initials (first character of each word)
            YYYY: Publish year
            N: Item number (implemented by subclasses)
            
        Returns:
            str: The base ID string without the type prefix and item number
        """
        return f"{self.__author_initials()}-{self.__year}"
    
    def __author_initials(self):
        """
        Generate author initials from the author's name.
        
        Takes the first character of the first and last words in the author's name.
        If the author has only one word, takes the first two characters.
        
        Returns:
            str: Two-character string representing author initials
        """
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
        
        Ensures the availability status is a boolean value.
        
        Args:
            available: The availability status to validate
            
        Raises:
            InvalidDataTypeError: If available is not a boolean
        """
        if not isinstance(available, bool):
            raise InvalidDataTypeError("bool", type(available).__name__)