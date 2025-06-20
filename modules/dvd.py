from library_item import LibraryItem
from modules.user import User
from reservabale import Reservable

class DVD(LibraryItem, Reservable):
    def __init__(self, title, author, year, available, duration):
        super().__init__(title, author, year, available)
        self.__duration = int(duration) # duration of the dvd content in minutes
        self.__reserved = None

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
    
    def reserve(self, user: User):
        """
        Reserve the DVD for a specific user.

        Args:
            user (User): The user who is reserving the DVD.

        Sets the __reserved attribute to the given user, indicating that the DVD is reserved by this user.
        """
        self.__reserved = user