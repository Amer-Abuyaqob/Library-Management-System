from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, author, year, available):
        super().__init__()
        self.__title = title
        self.__author = author
        self.__year = int(year)
        self.__available = bool(available)
        self._id = ""

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    @property
    def available(self):
        return self.__available

    @property
    def id(self):
        return self._id

    @title.setter
    def title(self, title):
        self.__title = title

    @author.setter
    def author(self, author):
        self.__author = author

    @year.setter
    def year(self, year):
        self.__year = int(year)

    @available.setter
    def available(self, available):
        self.__available = bool(available)
        
    @abstractmethod
    def display_info(self):
        """
        Display information about the library item.
        Should be implemented by subclasses.
        """
        pass

    @abstractmethod
    def check_availability(self):
        """
        Check if the item is available.
        Should be implemented by subclasses.
        """
        pass

    def _item_id(self):
        """
        Auto generation of item IDs bassed on the item's type
        Format: T.AA.YYYY.N
            T: Item's type -> {B: book, D: DVD, M: Magazine}
            AA: Author's first name initials
            YYYY: Publish year
            N: Item number (implemented by subclasses)
        """
        return f"{self.__author_initials()}-{self.__year}"
    
    def __author_initials(self):
        return f"{self.__author[0].upper()}{self.__author[1].lower()}"