"""
Magazine Management Module

This module defines the Magazine class which represents magazines in the library system.
Magazines are library items that can be borrowed by users.

The Magazine class provides:
- Magazine creation with genre information
- Automatic ID generation following the M-Aa-YYYY-N format
- Magazine-specific information display
- Input validation for all magazine attributes

Magazines inherit from LibraryItem and provide a simpler interface compared to
books and DVDs, as they cannot be reserved.
"""

from library_item import LibraryItem
from exceptions import InvalidDataTypeError, InvalidValueError

class Magazine(LibraryItem):
    """
    Represents a magazine in the library system.
    
    Magazines are library items that can be borrowed by users. Each magazine
    has a genre classification but cannot be reserved (unlike books and DVDs).
    
    Attributes:
        id (str): Unique magazine identifier (auto-generated or custom)
        title (str): The magazine's title
        author (str): The magazine's author/editor
        year (int): Publication year
        available (bool): Whether the magazine is available for borrowing
        genre (str): The magazine's genre classification
        
    Class Attributes:
        counter (int): Class-level counter for auto-generating magazine numbers
    """
    
    counter = 0  # counts every object created from this class
    
    def __init__(self, title, author, year, available, genre, custom_id=None):
        """
        Initialize a new magazine with all required attributes.
        
        All parameters are validated before assignment. The magazine ID can be
        either auto-generated or provided as a custom ID.
        
        Args:
            title (str): The magazine's title (non-empty string)
            author (str): The magazine's author/editor (at least 2 characters)
            year (int): Publication year (positive integer)
            available (bool): Whether the magazine is available for borrowing
            genre (str): The magazine's genre (non-empty string)
            custom_id (str, optional): Custom magazine ID. If None, auto-generates ID
            
        Raises:
            InvalidDataTypeError: If any parameter has the wrong data type
            InvalidValueError: If any parameter has an invalid value
        """
        super().__init__(title, author, year, bool(available))
        self.__validate_genre(genre)
        self.__genre = genre
        Magazine.counter += 1
        self.__magazine_num = Magazine.counter
        # Set ID to custom_id if provided, otherwise use auto-generated ID
        self._id = custom_id if custom_id is not None else self._item_id()

    def __validate_genre(self, genre):
        """
        Validate the genre parameter for a magazine.
        
        Ensures the genre is a non-empty string with actual content.
        
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
        Auto-generate a magazine ID following the standard format.
        
        Format: M-Aa-YYYY-N
            M: Magazine identifier (always 'M')
            Aa: Author's initials (first character of each word)
            YYYY: Publication year
            N: Magazine number (sequential counter)
            
        Returns:
            str: Auto-generated magazine ID
        """
        return f"M-{super()._item_id()}-{self.__magazine_num}"

    @property
    def genre(self):
        """
        Get the magazine's genre.
        
        Returns:
            str: The magazine's genre classification
        """
        return self.__genre

    @genre.setter
    def genre(self, genre):
        """
        Set the magazine's genre with validation.
        
        Args:
            genre (str): The new genre (non-empty string)
            
        Raises:
            InvalidDataTypeError: If genre is not a string
            InvalidValueError: If genre is empty or contains only whitespace
        """
        self.__validate_genre(genre)
        self.__genre = genre

    def display_info(self):
        """
        Display formatted information about the magazine.
        
        Returns a multi-line string containing all magazine information
        including ID, type, title, author, year, availability, and genre.
        
        Returns:
            str: Formatted string containing magazine information
        """
        return (
            f"Item ID: {self.id}\n"
            f"Item type: Magazine\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Year: {self.year}\n"
            f"Available: {self.available}\n"
            f"Genre: {self.genre}"
        )

    def check_availability(self):
        """
        Check if the magazine is available for borrowing.
        
        Returns the current availability status of the magazine.
        
        Returns:
            bool: True if the magazine is available, False otherwise
        """
        return self.available
