from library_item import LibraryItem
from user import User
from reservable import Reservable
from exceptions import InvalidDataTypeError, InvalidValueError

class DVD(LibraryItem, Reservable):
    counter = 0

    def __init__(self, title, author, year, available, duration, custom_id=None):
        super().__init__(title, author, year, available)

        try:
            self.__validate_duration(duration)
            self.__duration = duration  # duration of the dvd content in minutes
            self.__reserved: User | None = None
            DVD.counter += 1
            self.__dvd_num = DVD.counter
            # Set ID to custom_id if provided, otherwise use auto-generated ID
            self._id = custom_id if custom_id is not None else self._item_id()

        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")
        except InvalidValueError as value:
            print(f"Caught: {value}")

    def __validate_duration(self, duration):
        """
        Validate the duration parameter for a DVD.
        
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
        Auto generation of item IDs based on the item's type
        Format: T-AA-YYYY-N
            T: Item's type -> D: DVD
            AA: Author's first name initials
            YYYY: Publish year
            N: Item number
        """
        return f"D-{super()._item_id()}-{self.__dvd_num}"

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        try:
            self.__validate_duration(duration)
            self.__duration = duration
            return True
        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")
            return False
        except InvalidValueError as value:
            print(f"Caught: {value}")
            return False

    def display_info(self):
        return f'''
        Item type: DVD
        Title: {self.title}
        Author: {self.author}
        Year: {self.year}
        Available: {self.available}
        Duration: {self.duration} minutes 
        '''
    
    def check_availability(self):
        return self.available

    @property
    def reserved_by(self) -> User | None:
        return self.__reserved

    def reserve(self, user: User) -> None:
        """Mark the DVD as reserved by ``user``."""
        self.__reserved = user
