from library_item import LibraryItem
from user import User
from reservable import Reservable

class DVD(LibraryItem, Reservable):
    counter = 0

    def __init__(self, title, author, year, available, duration):
        super().__init__(title, author, year, available)

        try:
            duration = int(duration)
        except (TypeError, ValueError) as exc:
            raise ValueError("duration must be a positive integer") from exc
        if duration <= 0:
            raise ValueError("duration must be a positive integer")

        self.__duration = duration  # duration of the dvd content in minutes
        self.__reserved: User | None = None
        DVD.counter += 1
        self.__dvd_num = DVD.counter
        self._id = self._item_id()  # Initialize auto generated ID

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
        self.__duration = duration

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
