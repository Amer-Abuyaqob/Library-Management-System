class ItemNotAvailableError(Exception):
    """Exception raised when attempting to reserve an already reserved item."""
    pass
