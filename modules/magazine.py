from library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, author, year, available, genre):
        super().__init__(title, author, year, available)
        self.__genre = genre
        self.__reserved = None

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    def display_info(self):
        return f'''
        Item type: Magazine
        Title: {self.title}
        Author: {self.author}
        Year: {self.year}
        Available: {self.available}
        Genre: {self.genre}
        '''
    
    def check_availability(self):
        return self.available