"""
Custom Exceptions Module

This module defines all custom exceptions used throughout the Library Management System.
These exceptions provide specific error handling for different scenarios encountered
during library operations.

The exceptions are organized into two main categories:
1. General validation exceptions (InvalidDataTypeError, InvalidValueError, MissingFieldError)
2. Library-specific business logic exceptions (inheriting from LibraryError)

All exceptions include descriptive error messages to help users understand what went wrong.
"""

class InvalidDataTypeError(Exception):
    """
    Raised when an input has an incorrect data type.
    
    This exception is used throughout the system to ensure that all inputs
    have the correct data type before processing.
    
    Attributes:
        expected_type (str): The expected data type
        received_type (str): The actual data type received
    """
    def __init__(self, expected_type, received_type):
        """
        Initialize the exception with expected and received types.
        
        Args:
            expected_type (str): The expected data type
            received_type (str): The actual data type received
        """
        super().__init__(f"Expected data type: {expected_type}, but got: {received_type}")

class InvalidValueError(Exception):
    """
    Raised when a value is invalid (e.g., empty, too short, out of range).
    
    This exception is used for validation of input values that have the correct
    type but contain invalid content.
    
    Attributes:
        message (str): Description of why the value is invalid
    """
    def __init__(self, message):
        """
        Initialize the exception with a descriptive message.
        
        Args:
            message (str): Description of the validation error
        """
        super().__init__(message)

class MissingFieldError(Exception):
    """
    Raised when a required field is missing from a dictionary.
    
    This exception is commonly used when loading data from JSON files
    where certain fields are mandatory for proper object creation.
    
    Attributes:
        field_name (str): The name of the missing field
    """
    def __init__(self, field_name):
        """
        Initialize the exception with the missing field name.
        
        Args:
            field_name (str): The name of the missing field
        """
        super().__init__(f"The entry is missing the required field '{field_name}'.")


class LibraryError(Exception):
    """
    Base class for all library-related exceptions.
    
    This serves as a common parent class for all exceptions that are
    specific to library business logic operations.
    """
    pass

class ItemAlreadyExistsError(LibraryError):
    """
    Raised when trying to add an item that already exists in the library.
    
    This prevents duplicate items from being added to the library system.
    
    Attributes:
        item (str): Description of the item that already exists
    """
    def __init__(self, item):
        """
        Initialize the exception with item description.
        
        Args:
            item (str): Description of the item that already exists
        """
        super().__init__(f"The item [{item}] already exists.")

class UserAlreadyExistsError(LibraryError):
    """
    Raised when trying to add a user that already exists in the library.
    
    This prevents duplicate users from being registered in the system.
    
    Attributes:
        user (str): Description of the user that already exists
    """
    def __init__(self, user):
        """
        Initialize the exception with user description.
        
        Args:
            user (str): Description of the user that already exists
        """
        super().__init__(f"The user [{user}] already exists.")

class ItemNotFoundError(LibraryError):
    """
    Raised when an item is not found in the library.
    
    This exception is used when trying to perform operations on items
    that don't exist in the library system.
    
    Attributes:
        item (str): Description of the item that was not found
    """
    def __init__(self, item):
        """
        Initialize the exception with item description.
        
        Args:
            item (str): Description of the item that was not found
        """
        super().__init__(f"The item [{item}] doesn't exists.")


class UserNotFoundError(LibraryError):
    """
    Raised when a user is not found in the library.
    
    This exception is used when trying to perform operations on users
    that don't exist in the library system.
    
    Attributes:
        user (str): Description of the user that was not found
    """
    def __init__(self, user):
        """
        Initialize the exception with user description.
        
        Args:
            user (str): Description of the user that was not found
        """
        super().__init__(f"The user [{user}] doesn't exists.")


class ItemNotAvailableError(LibraryError):
    """
    Raised when an item is not available for borrowing.
    
    This exception is used when a user tries to borrow an item that
    is already borrowed by another user or is otherwise unavailable.
    
    Attributes:
        item (str): Description of the item that is not available
    """
    def __init__(self, item):
        """
        Initialize the exception with item description.
        
        Args:
            item (str): Description of the item that is not available
        """
        super().__init__(f"The item [{item}] is not available for borrowing.")


class ItemNotBorrowedError(LibraryError):
    """
    Raised when a user tries to return an item they haven't borrowed.
    
    This exception prevents users from returning items they don't have
    in their borrowing history.
    
    Attributes:
        item (str): Description of the item being returned
        user (str): Description of the user attempting the return
    """
    def __init__(self, item, user):
        """
        Initialize the exception with item and user descriptions.
        
        Args:
            item (str): Description of the item being returned
            user (str): Description of the user attempting the return
        """
        super().__init__(f"The item [{item}] is not borrowed by [{user}].")

class InvalidItemIDFormatError(LibraryError):
    """
    Raised when an item ID does not follow the required format.
    
    Item IDs must follow the format: T-Aa-YYYY-N
    Where T is the item type (B/D/M), Aa are author initials,
    YYYY is the publication year, and N is a sequential number.
    
    Attributes:
        item_id (str): The invalid item ID that was provided
    """
    def __init__(self, item_id):
        """
        Initialize the exception with the invalid item ID.
        
        Args:
            item_id (str): The invalid item ID that was provided
        """
        super().__init__(f"Expected ID format: T-Aa-YYYY-N (e.g., B-JD-2020-1), but got: {item_id}")

class InvalidUserIDFormatError(LibraryError):
    """
    Raised when a user ID does not follow the required format.
    
    User IDs must follow the format: U-Ff-Ll-N
    Where U is the user identifier, Ff are first name initials,
    Ll are last name initials, and N is a sequential number.
    
    Attributes:
        user_id (str): The invalid user ID that was provided
    """
    def __init__(self, user_id):
        """
        Initialize the exception with the invalid user ID.
        
        Args:
            user_id (str): The invalid user ID that was provided
        """
        super().__init__(f"Expected ID format: U-Ff-Ll-N (e.g., U-Jo-Sm-1), but got: {user_id}")
