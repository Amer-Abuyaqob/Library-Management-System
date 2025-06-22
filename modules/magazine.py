from library_item import LibraryItem

class Magazine(LibraryItem):
    counter = 0
    def __init__(self, title, author, year, available, genre):
        super().__init__(title, author, year, available)

        if not isinstance(genre, str) or not genre.strip():
            raise ValueError("genre must be a non-empty string")

        self.__genre = genre
        Magazine.counter += 1
        self.__magazine_num = Magazine.counter
        self._id = self._item_id()  # Initialize auto generated ID

    def _item_id(self):
        """
        Auto generation of item IDs based on the item's type
        Format: T-AA-YYYY-N
            T: Item's type -> M: magazine
            AA: Author's first name initials
            YYYY: Publish year
            N: Item number
        """
        return f"M-{super()._item_id()}-{self.__magazine_num}"

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
