from exceptions import InvalidDataTypeError, InvalidValueError

class User:
    counter = 0
    # FIXME: delete attribute (user_id) after removing it from all of the other methods
    def __init__(self, first_name, last_name):
        # TODO: auto generated user_id (U-FfLl-N)
        try:
            self.__validate_name(first_name, "first name")
            self.__first_name = first_name

            self.__validate_name(last_name, "last name")
            self.__last_name = last_name

            self.__borrowed_items = []

            User.counter += 1
            self.__user_num = User.counter
            self.__id = self.__user_id()

        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")
        except InvalidValueError as value:
            print(f"Caught: {value}")

    def __validate_name(self, name, name_type):
        """
        Validate a name parameter for a user.
        
        Args:
            name: The name to validate
            name_type: The type of name (e.g., "first name", "last name") for error messages
            
        Raises:
            InvalidDataTypeError: If name is not a string
            InvalidValueError: If name is empty, contains only whitespace, or has less than 2 characters
        """
        if not isinstance(name, str):
            raise InvalidDataTypeError("string", type(name).__name__)
            
        if not name.strip() or len(name.strip()) < 2:
            raise InvalidValueError(f"{name_type.title()} must be a non-empty string with at least two characters")

    @property
    def id(self):
        return self.__id

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def borrowed_items(self):
        return self.__borrowed_items
    
    def __user_id(self):
        """
        Auto generation of item IDs based on the item's type
        Format: T.AA.YYYY.N
            T: Item's type -> {B: book, D: DVD, M: Magazine}
            AA: Author's first name initials
            YYYY: Publish year
            N: Item number (implemented by subclasses)
        """
        return f"U-{self.__first_initials()}{self.__last_initials()}-{self.__user_num}"
    
    def __first_initials(self):
        return f"{self.__first_name[0].upper()}{self.__first_name[1].lower()}"
    
    def __last_initials(self):
        return f"{self.__last_name[0].upper()}{self.__last_name[1].lower()}"   

    def display_info(self):
        return f'''
        User ID: {self.id}
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Borrowed Items: {len(self.borrowed_items)} items
        '''
    
    def add_borrowed_item(self, item):
        """Add an item to the user's borrowed items list."""
        if item not in self.__borrowed_items:
            self.__borrowed_items.append(item)

    def remove_borrowed_item(self, item):
        """Remove an item from the user's borrowed items list."""
        if item in self.__borrowed_items:
            self.__borrowed_items.remove(item)

    @first_name.setter
    def first_name(self, first_name):
        self.__validate_name(first_name, "first name")
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        self.__validate_name(last_name, "last name")
        self.__last_name = last_name
