from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, author, year, available):
        super().__init__()
        self.__title = title
        self.__author = author
        self.__year = int(year)
        self.__available = bool(available)

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
        pass

    @abstractmethod
    def check_availability(self):
        pass