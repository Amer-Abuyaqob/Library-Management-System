"""
DVD Management Module

This module defines the DVD class which represents DVDs in the library system.
DVDs are library items that can be borrowed and reserved by users.

The DVD class provides:
- DVD creation with duration information
- Automatic ID generation following the D-Aa-YYYY-N format
- Reservation functionality through the Reservable interface
- DVD-specific information display
- Input validation for all DVD attributes

DVDs inherit from LibraryItem and implement the Reservable interface,
allowing them to be both borrowed and reserved by users.
"""

from library_item import LibraryItem
from user import User
from reservable import Reservable
from exceptions import InvalidDataTypeError, InvalidValueError

class DVD(LibraryItem, Reservable):
    """
    Represents a DVD in the library system.
    
    DVDs are library items that can be borrowed and reserved by users.
    Each DVD has a duration in minutes and can be reserved by a single user
    at a time.
    
    Attributes:
        id (str): Unique DVD identifier (auto-generated or custom)
        title (str): The DVD's title
        author (str): The DVD's director/creator
        year (int): Publication year
        available (bool): Whether the DVD is available for borrowing
        duration (int): Duration of the DVD content in minutes
        reserved_by (User or None): User who has reserved the DVD, if any
        
    Class Attributes:
        counter (int): Class-level counter for auto-generating DVD numbers
    """
    
    counter = 0

    def __init__(self, title, author, year, available, duration, custom_id=None):
        """
        Initialize a new DVD with all required attributes.
        
        All parameters are validated before assignment. The DVD ID can be
        either auto-generated or provided as a custom ID.
        
        Args:
            title (str): The DVD's title (non-empty string)
            author (str): The DVD's director/creator (at least 2 characters)
            year (int): Publication year (positive integer)
            available (bool): Whether the DVD is available for borrowing
            duration (int): Duration in minutes (positive integer)
            custom_id (str, optional): Custom DVD ID. If None, auto-generates ID
            
        Raises:
            InvalidDataTypeError: If any parameter has the wrong data type
            InvalidValueError: If any parameter has an invalid value
        """
        super().__init__(title, author, year, bool(available))
        self.__validate_duration(duration)
        self.__duration = duration  # duration of the dvd content in minutes
        self.__reserved: User | None = None
        DVD.counter += 1
        self.__dvd_num = DVD.counter
        # Set ID to custom_id if provided, otherwise use auto-generated ID
        self._id = custom_id if custom_id is not None else self._item_id()

    def __validate_duration(self, duration):
        """
        Validate the duration parameter for a DVD.
        
        Ensures the duration is a positive integer representing minutes.
        
        Args:
            duration: The duration to validate (in minutes)
            
        Raises:
            InvalidDataTypeError: If duration is not an integer
            InvalidValueError: If duration is not a positive non-zero integer
        """
        if not isinstance(duration, int):
            raise InvalidDataTypeError("integer", type(duration).__name__)

        if duration <= 0:
            raise InvalidValueError("Duration must be a positive non-zero integer")

    def _item_id(self):
        """
        Auto-generate a DVD ID following the standard format.
        
        Format: D-Aa-YYYY-N
            D: DVD identifier (always 'D')
            Aa: Author's initials (first character of each word)
            YYYY: Publication year
            N: DVD number (sequential counter)
            
        Returns:
            str: Auto-generated DVD ID
        """
        return f"D-{super()._item_id()}-{self.__dvd_num}"

    @property
    def duration(self):
        """
        Get the DVD's duration.
        
        Returns:
            int: The DVD's duration in minutes
        """
        return self.__duration

    @duration.setter
    def duration(self, duration):
        """
        Set the DVD's duration with validation.
        
        Args:
            duration (int): The new duration in minutes (positive integer)
            
        Raises:
            InvalidDataTypeError: If duration is not an integer
            InvalidValueError: If duration is not a positive non-zero integer
        """
        self.__validate_duration(duration)
        self.__duration = duration

    def display_info(self):
        """
        Display formatted information about the DVD.
        
        Returns a multi-line string containing all DVD information
        including ID, type, title, author, year, availability, and duration.
        
        Returns:
            str: Formatted string containing DVD information
        """
        return (
            f"Item ID: {self.id}\n"
            f"Item type: DVD\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Year: {self.year}\n"
            f"Available: {self.available}\n"
            f"Duration: {self.duration} minutes"
        )
    
    def check_availability(self):
        """
        Check if the DVD is available for borrowing.
        
        Returns the current availability status of the DVD.
        
        Returns:
            bool: True if the DVD is available, False otherwise
        """
        return self.available

    @property
    def reserved_by(self) -> User | None:
        """
        Get the user who has reserved this DVD.
        
        Returns:
            User or None: The user who has reserved the DVD, or None if not reserved
        """
        return self.__reserved

    def reserve(self, user: User) -> None:
        """
        Reserve the DVD for a specific user.
        
        Marks the DVD as reserved by the specified user. Only one user
        can reserve a DVD at a time.
        
        Args:
            user (User): The user who is reserving the DVD
        """
        self.__reserved = user
