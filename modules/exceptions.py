
class LibraryError(Exception):
    """Base class for library related exceptions."""
    pass


class ItemNotFoundError(LibraryError):
    """Raised when an item is not found in the library."""
    pass


class UserNotFoundError(LibraryError):
    """Raised when a user is not found in the library."""
    pass


class ItemNotAvailableError(LibraryError):
    """Raised when an item is not available for borrowing."""
    pass


class ItemNotBorrowedError(LibraryError):
    """Raised when a user tries to return an item they haven't borrowed."""
    pass
