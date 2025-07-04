"""
User Management Module

This module defines the User class which represents library users in the system.
Users can borrow items, have borrowing history, and are identified by unique IDs.

The User class provides:
- User registration with validation
- Automatic ID generation following the U-Ff-Ll-N format
- Borrowing history tracking
- User information display
- Input validation for all user attributes

Users are essential for the borrowing system and are referenced by items
when they are borrowed or reserved.
"""

from modules.exceptions import InvalidDataTypeError, InvalidValueError

class User:
    """
    Represents a library user with borrowing capabilities.
    
    Each user has a unique identifier, personal information, and a list
    of currently borrowed items. Users can borrow and return items through
    the library system.
    
    Attributes:
        id (str): Unique user identifier (auto-generated or custom)
        first_name (str): User's first name (at least 2 characters)
        last_name (str): User's last name (at least 2 characters)
        borrowed_items (list): List of item IDs currently borrowed by the user
        
    Class Attributes:
        counter (int): Class-level counter for auto-generating user numbers
    """
    
    counter = 0
    
    def __init__(self, first_name, last_name, custom_id=None):
        """
        Initialize a new user with personal information.
        
        All parameters are validated before assignment. The user ID can be
        either auto-generated or provided as a custom ID.
        
        Args:
            first_name (str): User's first name (at least 2 characters)
            last_name (str): User's last name (at least 2 characters)
            custom_id (str, optional): Custom user ID. If None, auto-generates ID
            
        Raises:
            InvalidDataTypeError: If any parameter has the wrong data type
            InvalidValueError: If any parameter has an invalid value
        """
        self.__validate_name(first_name, "first name")
        self.__first_name = first_name

        self.__validate_name(last_name, "last name")
        self.__last_name = last_name

        self.__borrowed_items = []

        User.counter += 1
        self.__user_num = User.counter
        # Set ID to custom_id if provided, otherwise use auto-generated ID
        self.__id = custom_id if custom_id is not None else self.__user_id()

    def __validate_name(self, name, name_type):
        """
        Validate a name parameter for a user.
        
        Ensures the name is a non-empty string with at least 2 characters.
        
        Args:
            name: The name to validate
            name_type: The type of name (e.g., "first name", "last name") for error messages
            
        Raises:
            InvalidDataTypeError: If name is not a string
            InvalidValueError: If name is empty, contains only whitespace, or has less than 2 characters
        """
        if not isinstance(name, str):
            raise InvalidDataTypeError("string", type(name).__name__)
            
        if len(name.strip()) < 2:
            raise InvalidValueError(f"{name_type.title()} must be a non-empty string with at least two characters")

    @property
    def id(self):
        """
        Get the user's unique identifier.
        
        Returns:
            str: The user's unique ID
        """
        return self.__id

    @property
    def first_name(self):
        """
        Get the user's first name.
        
        Returns:
            str: The user's first name
        """
        return self.__first_name

    @property
    def last_name(self):
        """
        Get the user's last name.
        
        Returns:
            str: The user's last name
        """
        return self.__last_name

    @property
    def borrowed_items(self):
        """
        Get the list of items currently borrowed by the user.
        
        Returns:
            list: List of item IDs that the user has borrowed
        """
        return self.__borrowed_items
    
    def __user_id(self):
        """
        Auto-generate a user ID following the standard format.
        
        Format: U-Ff-Ll-N
            U: User identifier (always 'U')
            Ff: First name initials (first two characters)
            Ll: Last name initials (first two characters)
            N: User number (sequential counter)
            
        Returns:
            str: Auto-generated user ID
        """
        return f"U-{self.__first_initials()}-{self.__last_initials()}-{self.__user_num}"
    
    def __first_initials(self):
        """
        Generate initials from the first name.
        
        Takes the first two characters of the first name, with the first
        character capitalized and the second lowercase.
        
        Returns:
            str: Two-character string representing first name initials
        """
        return f"{self.__first_name[0].upper()}{self.__first_name[1].lower()}"
    
    def __last_initials(self):
        """
        Generate initials from the last name.
        
        Takes the first two characters of the last name, with the first
        character capitalized and the second lowercase.
        
        Returns:
            str: Two-character string representing last name initials
        """
        return f"{self.__last_name[0].upper()}{self.__last_name[1].lower()}"   

    def display_info(self):
        """
        Display formatted information about the user.
        
        Returns a multi-line string containing all user information
        including ID, name, and current borrowed items.
        
        Returns:
            str: Formatted string containing user information
        """
        return (
            f"User ID: {self.id}\n"
            f"First Name: {self.first_name}\n"
            f"Last Name: {self.last_name}\n"
            f"Borrowed Items: {self.borrowed_items}"
        )
    
    def add_borrowed_item(self, item_id):
        """
        Add an item to the user's borrowed items list.
        
        Only adds the item if it's not already in the list to prevent duplicates.
        
        Args:
            item_id (str): The ID of the item being borrowed
        """
        if item_id not in self.__borrowed_items:
            self.__borrowed_items.append(item_id)

    def remove_borrowed_item(self, item_id):
        """
        Remove an item from the user's borrowed items list.
        
        Only removes the item if it exists in the list.
        
        Args:
            item_id (str): The ID of the item being returned
        """
        if item_id in self.__borrowed_items:
            self.__borrowed_items.remove(item_id)

    @first_name.setter
    def first_name(self, first_name):
        """
        Set the user's first name with validation.
        
        Args:
            first_name (str): The new first name (at least 2 characters)
            
        Raises:
            InvalidDataTypeError: If first_name is not a string
            InvalidValueError: If first_name is empty or has less than 2 characters
        """
        self.__validate_name(first_name, "first name")
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Set the user's last name with validation.
        
        Args:
            last_name (str): The new last name (at least 2 characters)
            
        Raises:
            InvalidDataTypeError: If last_name is not a string
            InvalidValueError: If last_name is empty or has less than 2 characters
        """
        self.__validate_name(last_name, "last name")
        self.__last_name = last_name
        
