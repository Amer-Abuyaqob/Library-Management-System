import json
import os

from user import User
from book import Book
from magazine import Magazine
from dvd import DVD

from exceptions import (
    InvalidDataTypeError,
    MissingFieldError,
    ItemNotFoundError,
    UserNotFoundError,
    ItemNotAvailableError,
    ItemNotBorrowedError,
    ItemAlreadyExistsError,
    InvalidValueError
)

class Library:
    def __init__(self):
        self.__items_file = os.path.join("data", "items.json")
        self.__users_file = os.path.join("data", "users.json")
        self.__items = []
        self.__users = []
        self.load_data()

    @property
    def items(self):
        return self.__items
    
    @property
    def users(self):
        return self.__users
    
    def __isItem(self, item):
        if not isinstance(item, (Book, DVD, Magazine)):
            raise InvalidDataTypeError("Book/DVD/Magazine", type(item).__name__)
      
    def __item_exists(self, item):
        for existing_item in self.__items:
            if (existing_item.title == item.title and
                existing_item.author == item.author and
                existing_item.year == item.year):
                return True
        return False

    def __isUser(self, user):
        if not isinstance(user, User):
            raise InvalidDataTypeError("User", type(user).__name__)
      
    def __user_exists(self, user):
        for existing_user in self.__users:
            if (existing_user.first_name == user.first_name and
                existing_user.last_name == user.last_name):
                return True
        return False

    def __IsUserName(self, name, name_type):
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
        
    def add_item(self, item):
        """
        Add a new item to the library.
        Args:
            item: LibraryItem object to add
        Returns:
            bool: True if item was added successfully, False otherwise
        Raises:
            ValueError: If item with same ID already exists
            ItemNotFoundError: If item is not an instance of Book, DVD or Magazine
        """
        try:
            self.__isItem(item)
            
            if self.__item_exists(item):
                raise ItemAlreadyExistsError(f"{item.title} ({item.year}) by {item.author}")

            self.__items.append(item)
            return True

        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")
            return False

        except ItemAlreadyExistsError as exists:
            print(f"Caught: {exists}")
            return False

    def update_item(self, item, new_item):
        """
        Update an item's attributes.
        Args:
            item_id: ID of the item to update
            **kwargs: Key-value pairs of attributes to update
        Returns:
            bool: True if update was successful, False otherwise
        Raises:
            ItemNotFoundError: If item doesn't exist
        """
        try:
            self.__isItem(new_item)
            
            if self.__item_exists(new_item):
                raise ItemAlreadyExistsError(f"{new_item.title} ({new_item.year}) by {new_item.author}")

            self.__isItem(item)

        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")
            return False

        except ItemAlreadyExistsError as exists:
            print(f"Caught: {exists}")
            return False

        try:
            if item in self.__items:
                index = self.__items.index(item)
                self.__items[index] = new_item
                return True
            else:
                raise ItemNotFoundError(f"{item.title} ({item.year}) by {item.author}")

        except ItemNotFoundError as not_found:
            print(f"Caught: {not_found}")
            return False 

    def remove_item(self, item):
        """
        Remove an item from the library.
        Args:
            item_id: ID of the item to remove
        Returns:
            bool: True if item was removed successfully, False otherwise
        Raises:
            ItemNotFoundError: If item doesn't exist
        """
        try:
            self.__isItem(item)
            
            if item not in self.__items:
                raise ItemNotFoundError(f"{item.title} ({item.year}) by {item.author}")

            self.__items.remove(item)
            return True
        
        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")
            return False

        except ItemNotFoundError as not_found:
            print(f"Caught: {not_found}")
            return False 

    def add_user(self, user):
        """
        Add a new user to the library.
        Args:
            user: User object to add
        Returns:
            bool: True if user was added successfully, False otherwise
        Raises:
            InvalidDataTypeError: If user is not an instance of User
            ItemAlreadyExistsError: If user with same ID already exists
        """
        try:
            self.__isUser(user)
            
            if self.__user_exists(user):
                # FIXME: replace with UserAlreadyExistsError
                raise ItemAlreadyExistsError(f"User with ID '{user.id}'")

            self.__users.append(user)
            return True

        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")
            return False
        # FIXME: replace with UserAlreadyExistsError
        except ItemAlreadyExistsError as exists:
            print(f"Caught: {exists}")
            return False

    def remove_user(self, user):
        """
        Remove a user from the library.
        Args:
            user: User object to remove
        Returns:
            bool: True if user was removed successfully, False otherwise
        Raises:
            InvalidDataTypeError: If user is not an instance of User
            UserNotFoundError: If user doesn't exist
        """
        try:
            self.__isUser(user)
            
            if user not in self.__users:
                raise UserNotFoundError(f"{user.first_name} {user.last_name}")

            self.__users.remove(user)
            return True
        
        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")
            return False

        except UserNotFoundError as not_found:
            print(f"Caught: {not_found}")
            return False

    def update_user(self, user, new_user):
        """
        Update a user's attributes.
        Args:
            user: User object to update
            new_user: New User object with updated attributes
        Returns:
            bool: True if update was successful, False otherwise
        Raises:
            InvalidDataTypeError: If user or new_user is not an instance of User
            UserNotFoundError: If user doesn't exist
            ItemAlreadyExistsError: If new_user with same ID already exists
        """
        try:
            self.__isUser(user)
            self.__isUser(new_user)
            
            if self.__user_exists(new_user):
                # FIXME: replace with UserAlreadyExistsError
                raise ItemAlreadyExistsError(f"User with ID '{new_user.id}'")

        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")
            return False

        # FIXME: replace with UserAlreadyExistsError
        except ItemAlreadyExistsError as exists:
            print(f"Caught: {exists}")
            return False

        try:
            if user in self.__users:
                index = self.__users.index(user)
                self.__users[index] = new_user
                return True
            else:
                raise UserNotFoundError(f"{user.first_name} {user.last_name}")

        except UserNotFoundError as not_found:
            print(f"Caught: {not_found}")
            return False

    # TODO: improve with helper method
    def __create_item(self, item):
        """Create a ``LibraryItem`` from a raw dictionary.

        The method validates that ``item`` contains the required keys with
        values of the correct type before instantiating the appropriate class.

        Parameters
        ----------
        item: dict
            Dictionary describing the item as read from the JSON file.

        Returns
        -------
        LibraryItem

        Raises
        ------
        ValueError
            If the dictionary is missing fields or if a field has an invalid
            type or value.
        """
        try:
            if not isinstance(item, dict):
                raise InvalidDataTypeError("dict", type(item).__name__)
        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")

        # Common mandatory fields for all items
        required_fields = {
            "id": str,
            "type": str,
            "title": str,
            "author": str,
            "year": int,
            "available": bool,
        }

        # Validate required fields
        for field, expected_type in required_fields.items():
            # try:
            if field not in item:
                raise MissingFieldError(field)
                
            if not isinstance(item[field], expected_type):
                raise InvalidDataTypeError(expected_type.__name__, type(item[field]).__name__)
            # except
            
            # Validate if the data follows the required format (not empty, > 0)
            # id: not empty, type: not empty, title: not empty, author: > 2 chars, year: > 0

            # try:
            if field == "id" and not item[field].strip():
                raise InvalidValueError("ID must be a non-empty string")
            elif field == "type" and not item[field].strip():
                raise InvalidValueError("Type must be a non-empty string")
            elif field == "title" and not item[field].strip():
                raise InvalidValueError("Title must be a non-empty string")
            elif field == "author" and len(item[field].strip()) < 2:
                raise InvalidValueError("Author must be a non-empty string with at least two characters")
            elif field == "year" and item[field] <= 0:
                raise InvalidValueError("Year must be a positive non-zero integer")
            # except

        # Optional validation for reserved
        # try:
        if "reserved" in item and not isinstance(item["reserved"], User):
            raise InvalidDataTypeError("User", type(item["reserved"]).__name__)
        # except

        item_type = item["type"].upper()

        if item_type == "BOOK":
            # try:
            if "genre" not in item:
                raise MissingFieldError("genre")
            if not isinstance(item["genre"], str):
                raise InvalidDataTypeError("string", type(item["genre"]).__name__)
            # Validate if the data follows the required format (not empty, > 0)
            # genre: not empty
            if not item["genre"].strip():
                raise InvalidValueError("Genre must be a non-empty string")
                
            item_obj = Book(item["title"], item["author"], item["year"], item["available"], item["genre"], item["id"])
            # except

        elif item_type == "MAGAZINE":
            # try:
            if "genre" not in item:
                raise MissingFieldError("genre")
            if not isinstance(item["genre"], str):
                raise InvalidDataTypeError("string", type(item["genre"]).__name__)
            # Validate if the data follows the required format (not empty, > 0)
            # genre: not empty
            if not item["genre"].strip():
                raise InvalidValueError("Genre must be a non-empty string")
            item_obj = Magazine(item["title"], item["author"], item["year"], item["available"], item["genre"], item["id"])
            # except

        elif item_type == "DVD":
            # try:
            if "duration" not in item:
                raise MissingFieldError("duration")
            if not isinstance(item["duration"], int):
                raise InvalidDataTypeError("integer", type(item["duration"]).__name__)
            # Validate if the data follows the required format (not empty, > 0)
            # duration: > 0
            if item["duration"] <= 0:
                raise InvalidValueError("Duration must be a positive non-zero integer")
            item_obj = DVD(item["title"], item["author"], item["year"], item["available"], item["duration"], item["id"])
            # except

        else:
            # try:
            raise InvalidValueError(f"Unknown item type '{item_type}'")
            # except

        return item_obj
    
    def __load_items(self):
        """
        Load items from JSON file.
        Reads items.json to populate the library's items list.
        """
        self.__items = []  # Clearing the items list to avoid duplicates
        with open(self.__items_file, "r", encoding="utf-8") as f:
            items_data = json.load(f)

        # FIXME: try-except here
        for item in items_data:
            item_obj = self.__create_item(item)
            self.add_item(item_obj)

    def __load_users(self):
        """
        Loads users from JSON file.
        Reads users.json to populate the library's users list.
        """
        self.__users = []  # Clearing the items list to avoid duplicates
        with open(self.__users_file, "r", encoding="utf-8") as f:
            users_data = json.load(f)
        # TODO: move to helper method
        for user in users_data:
            try:
                # Validate required fields
                required_fields = {
                    "first_name": str,
                    "last_name": str,
                    "id": str
                }

                for field, expected_type in required_fields.items():
                    if field not in user:
                        raise MissingFieldError(field)
                    
                    if not isinstance(user[field], expected_type):
                        raise InvalidDataTypeError(expected_type.__name__, type(user[field]).__name__)
                    
                    # Validate if the data follows the required format
                    if field in ["first_name", "last_name"] and len(user[field].strip()) < 2:
                        raise InvalidValueError(f"{field.replace('_', ' ').title()} must be a non-empty string with at least two characters")
                    elif field == "id" and not user[field].strip():
                        raise InvalidValueError("User ID must be a non-empty string")

                # Create user object with validated data
                user_obj = User(user["first_name"], user["last_name"], user["id"])

                # Add borrowed items by matching IDs with already loaded items
                for item_id in user.get("borrowed_items", []):
                    try:
                        # Find the corresponding item in the library
                        for item in self.__items:
                            if item.id == item_id:
                                user_obj.add_borrowed_item(item_id)
                                break
                        else:
                            raise ItemNotFoundError(f"{item.title} ({item.year}) by {item.author}")

                    except ItemNotFoundError as item_Nfound:
                        print(f"Caught: {item_Nfound}")

                self.add_user(user_obj)

            except MissingFieldError as missing:
                print(f"Caught: {missing}")
            except InvalidDataTypeError as data_type:
                print(f"Caught: {data_type}")
            except InvalidValueError as value:
                print(f"Caught: {value}")

    def load_data(self):
        """
        Load library data from JSON files.
        Reads items.json and users.json to populate the library's items and users.
        Raises FileNotFoundError if files don't exist.
        """
        self.__load_items()
        self.__load_users()


    def __item_entry(self, item):
        entry = {
                "id": item.id,
                "type": item.__class__.__name__,
                "title": item.title,
                "author": item.author,
                "year": item.year,
                "available": item.available,
            }
        if isinstance(item, (Book, Magazine)):
            entry["genre"] = item.genre
        if isinstance(item, DVD):
            entry["duration"] = item.duration
        return entry
    
    def __user_entry(self, user):
        entry = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "borrowed_items": user.borrowed_items
        }
        return entry
    
    def __save_items(self):
        items_data = []
        for item in self.__items:
            entry = self.__item_entry(item)
            items_data.append(entry)
            
        os.makedirs(os.path.dirname(self.__items_file), exist_ok=True)
        with open(self.__items_file, "w", encoding="utf-8") as f:
            json.dump(items_data, f, indent=2)

    def __save_users(self):
        users_data = []
        for user in self.__users:
            entry = self.__user_entry(user)
            users_data.append(entry)

        os.makedirs(os.path.dirname(self.__users_file), exist_ok=True)
        with open(self.__users_file, "w", encoding="utf-8") as f:
            json.dump(users_data, f, indent=2)

    def save_data(self):
        """
        Saves library data to JSON files.
        Writes current items and users to items.json and users.json respectively.
        Raises IOError if writing to files fails.
        """
        self.__save_items()
        self.__save_users()

    def borrow_item(self, user, item):
        """
        Borrow an item for a user.
        Args:
            user: User object borrowing the item
            item: LibraryItem object to borrow
        Returns:
            bool: True if item was borrowed successfully, False otherwise
        Raises:
            UserNotFoundError: If the user doesn't exist
            ItemNotFoundError: If the item doesn't exist
            ItemNotAvailableError: If the item is not available
        """
        try:
            self.__isItem(item)
            self.__isUser(user)

            # Check if user exists in the library
            if user not in self.__users:
                raise UserNotFoundError(f"{user.first_name} {user.last_name}")
            
            # Check if item exists in the library
            if item not in self.__items:
                raise ItemNotFoundError(f"{item.title} ({item.year}) by {item.author}")
            
            # Check if item is available
            if not item.available:
                raise ItemNotAvailableError(f"{item.title} ({item.year}) by {item.author}")
            
            # Add item to user's borrowed items
            user.add_borrowed_item(item)
            # Mark item as unavailable
            item.available = False
            return True
        
        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")
            return False  
        except UserNotFoundError as user_Nfound:
            print(f"Caught: {user_Nfound}")
            return False
        except ItemNotFoundError as item_Nfound:
            print(f"Caught: {item_Nfound}")
            return False
        except ItemNotAvailableError as item_Navailable:
            print(f"Caught: {item_Navailable}")
            return False

    def return_item(self, user, item):
        """
        Return an item from a user.
        Args:
            user: User object returning the item
            item: LibraryItem object to return
        Returns:
            bool: True if item was returned successfully, False otherwise
        Raises:
            UserNotFoundError: If the user doesn't exist
            ItemNotFoundError: If the item doesn't exist
            ItemNotBorrowedError: If the user hasn't borrowed the item
        """
        try:
            self.__isItem(item)
            self.__isUser(user)
        
            # Check if user exists in the library
            if user not in self.users:
                raise UserNotFoundError(f"{user.first_name} {user.last_name}")
            
            # Check if item exists in the library
            if item not in self.items:
                raise ItemNotFoundError(f"{item.title} ({item.year}) by {item.author}")
            
            # Check if user has borrowed the item
            if item not in user.borrowed_items:
                raise ItemNotBorrowedError(f"{item.title} ({item.year}) by {item.author}", f"{user.first_name} {user.last_name}")
            
            # Remove item from user's borrowed items
            user.remove_borrowed_item(item)
            # Mark item as available
            item.available = True
            return True
        
        except InvalidDataTypeError as data_type:
            print(f"Caught: {data_type}")
            return False  
        except UserNotFoundError as user_Nfound:
            print(f"Caught: {user_Nfound}")
            return False
        except ItemNotFoundError as item_Nfound:
            print(f"Caught: {item_Nfound}")
            return False
        except ItemNotBorrowedError as item_Nborrowed:
            print(f"Caught: {item_Nborrowed}")
            return False

if __name__ == "__main__":
    l = ["abc", "efg", "hij"]
    dic = {"list": l}
    print(dic)