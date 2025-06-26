class InvalidDataTypeError(Exception):
    """Raised when an input has an incorrect data type."""
    def __init__(self, expected_type, received_type):
        super().__init__(f"Expected data type: {expected_type}, but got: {received_type}")

class InvalidValueError(Exception):
    """Raised when a string value is invalid (e.g., empty or too short)."""
    def __init__(self, message):
        super().__init__(message)

class LibraryError(Exception):
    """Base class for library related exceptions."""
    pass

class ItemAlreadyExistsError(LibraryError):
    """Raised when trying to add an item that already exists."""
    def __init__(self, item):
        super().__init__(f"The item [{item}] already exists.")

class ItemNotFoundError(LibraryError):
    """Raised when an item is not found in the library."""
    def __init__(self, item):
        super().__init__(f"The item [{item}] doesn't exists.")


class UserNotFoundError(LibraryError):
    """Raised when a user is not found in the library."""
    pass


class ItemNotAvailableError(LibraryError):
    """Raised when an item is not available for borrowing."""
    pass


class ItemNotBorrowedError(LibraryError):
    """Raised when a user tries to return an item they haven't borrowed."""
    pass
