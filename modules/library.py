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
    UserAlreadyExistsError,
    InvalidValueError
)

class Library:
    # ===================== INIT & FILE PATHS =====================
    def __init__(self):
        self.__items_file = os.path.join("data", "items.json")
        self.__users_file = os.path.join("data", "users.json")
        self.__items = []
        self.__users = []
        self.load_data()

    # ===================== PROPERTY GETTERS =====================
    @property
    def items(self):
        return self.__items
    
    @property
    def users(self):
        return self.__users

    # ===================== VALIDATION METHODS =====================
    def __isItem(self, item):
        if not isinstance(item, (Book, DVD, Magazine)):
            raise InvalidDataTypeError("Book/DVD/Magazine", type(item).__name__)
    
    def __item_exists(self, item):
        # FIXME: might need to check id as well
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
        # FIXME: might need to check id as well
        for existing_user in self.__users:
            if (existing_user.first_name == user.first_name and
                existing_user.last_name == user.last_name):
                return True
        return False

    def get_item(self, item_id):
        for item in self.__items:
            if item.id == item_id:
                return item
        return None
    
    def get_user(self, user_id):
        for user in self.library.users:
            if user.id == user_id:
                return user
        return None
       
    # ===================== ITEM MODIFICATION METHODS =====================
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
        self.__isItem(item)
        
        if self.__item_exists(item):
            raise ItemAlreadyExistsError(f"{item.title} ({item.year}) by {item.author} (ID: {item.id})")

        self.__items.append(item)
        return True

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
        self.__isItem(new_item)
        
        if self.__item_exists(new_item):
            raise ItemAlreadyExistsError(f"{new_item.title} ({new_item.year}) by {new_item.author} (ID: {new_item.id})")

        self.__isItem(item)

        if item in self.__items:
            index = self.__items.index(item)
            self.__items[index] = new_item
            return True
        else:
            raise ItemNotFoundError(f"{item.title} ({item.year}) by {item.author} (ID: {item.id})")

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
        self.__isItem(item)
        
        if item not in self.__items:
            raise ItemNotFoundError(f"{item.title} ({item.year}) by {item.author} (ID: {item.id})")

        self.__items.remove(item)
        return True

    # ===================== USER MODIFICATION METHODS =====================
    def add_user(self, user):
        """
        Add a new user to the library.
        Args:
            user: User object to add
        Returns:
            bool: True if user was added successfully, False otherwise
        Raises:
            InvalidDataTypeError: If user is not an instance of User
            UserAlreadyExistsError: If user with same name already exists
        """
        self.__isUser(user)
        
        if self.__user_exists(user):
            raise UserAlreadyExistsError(f"{user.first_name} {user.last_name} (ID: {user.id})")

        self.__users.append(user)
        return True

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
        self.__isUser(user)
        
        if user not in self.__users:
            raise UserNotFoundError(f"{user.first_name} {user.last_name} (ID: {user.id})")

        self.__users.remove(user)
        return True

    def update_user(self, user, new_user):
        """
        Update a user's attributes.
        Args:
            user: User object to update
            new_user: New User object with updated attributes
        Returns:
            bool: True if update was successful, False otherwise
        Raises:
            UserNotFoundError: If user doesn't exist
            UserAlreadyExistsError: If new_user with same name already exists
        """
        self.__isUser(new_user)
        
        if self.__user_exists(new_user):
            raise UserAlreadyExistsError(f"{new_user.first_name} {new_user.last_name} (ID: {new_user.id})")

        self.__isUser(user)

        if user in self.__users:
            index = self.__users.index(user)
            self.__users[index] = new_user
            return True
        else:
            raise UserNotFoundError(f"{user.first_name} {user.last_name} (ID: {user.id})")

    # ===================== ITEM LOADING METHODS =====================
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
        if not isinstance(item, dict):
            raise InvalidDataTypeError("dict", type(item).__name__)

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
            if field not in item:
                raise MissingFieldError(field)
                
            if not isinstance(item[field], expected_type):
                raise InvalidDataTypeError(expected_type.__name__, type(item[field]).__name__)
            
            # Validate if the data follows the required format
            # id: not empty, type: not empty, title: not empty, author: > 2 chars, year: > 0

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

        # Optional validation for reserved
        if "reserved" in item and not isinstance(item["reserved"], User):
            raise InvalidDataTypeError("User", type(item["reserved"]).__name__)

        item_type = item["type"].upper()

        if item_type == "BOOK":
            if "genre" not in item:
                raise MissingFieldError("genre")
            if not isinstance(item["genre"], str):
                raise InvalidDataTypeError("string", type(item["genre"]).__name__)
            # Validate if the data follows the required format (not empty, > 0)
            # genre: not empty
            if not item["genre"].strip():
                raise InvalidValueError("Genre must be a non-empty string")
                
            item_obj = Book(item["title"], item["author"], item["year"], item["available"], item["genre"], item["id"])

        elif item_type == "MAGAZINE":
            if "genre" not in item:
                raise MissingFieldError("genre")
            if not isinstance(item["genre"], str):
                raise InvalidDataTypeError("string", type(item["genre"]).__name__)
            # Validate if the data follows the required format (not empty, > 0)
            # genre: not empty
            if not item["genre"].strip():
                raise InvalidValueError("Genre must be a non-empty string")
            item_obj = Magazine(item["title"], item["author"], item["year"], item["available"], item["genre"], item["id"])

        elif item_type == "DVD":
            if "duration" not in item:
                raise MissingFieldError("duration")
            if not isinstance(item["duration"], int):
                raise InvalidDataTypeError("integer", type(item["duration"]).__name__)
            # Validate if the data follows the required format (not empty, > 0)
            # duration: > 0
            if item["duration"] <= 0:
                raise InvalidValueError("Duration must be a positive non-zero integer")
            item_obj = DVD(item["title"], item["author"], item["year"], item["available"], item["duration"], item["id"])

        else:
            raise InvalidValueError(f"Unknown item type '{item_type}'")

        return item_obj
    
    def __load_items(self):
        """
        Load items from JSON file.
        Reads items.json to populate the library's items list.
        """
        self.__items = []  # Clearing the items list to avoid duplicates
        with open(self.__items_file, "r", encoding="utf-8") as f:
            items_data = json.load(f)

        for item in items_data:
            item_obj = self.__create_item(item)
            self.add_item(item_obj)

    # ===================== USER LOADING METHODS =====================
    def __load_users(self):
        """
        Loads users from JSON file.
        Reads users.json to populate the library's users list.
        """
        self.__users = []  # Clearing the items list to avoid duplicates
        with open(self.__users_file, "r", encoding="utf-8") as f:
            users_data = json.load(f)
        
        for user in users_data:
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
                # Find the corresponding item in the library
                for item in self.__items:
                    if item.id == item_id:
                        user_obj.add_borrowed_item(item_id)
                        break
                else:
                    raise ItemNotFoundError(f"Item with ID '{item_id}'")

            self.add_user(user_obj)

    def load_data(self):
        """
        Load library data from JSON files.
        Reads items.json and users.json to populate the library's items and users.
        Raises FileNotFoundError if files don't exist.
        """
        self.__load_items()
        self.__load_users()

    # ===================== ITEM SAVING METHODS =====================
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
    
    def __save_items(self):
        items_data = []
        for item in self.__items:
            entry = self.__item_entry(item)
            items_data.append(entry)
            
        os.makedirs(os.path.dirname(self.__items_file), exist_ok=True)
        with open(self.__items_file, "w", encoding="utf-8") as f:
            json.dump(items_data, f, indent=2)

    # ===================== USER SAVING METHODS =====================
    def __user_entry(self, user):
        entry = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "borrowed_items": user.borrowed_items
        }
        return entry
    
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

    # ===================== BORROW/RETURN METHODS =====================
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
        self.__isItem(item)
        self.__isUser(user)

        # Check if user exists in the library
        if user not in self.__users:
            raise UserNotFoundError(f"{user.first_name} {user.last_name} (ID: {user.id})")
        
        # Check if item exists in the library
        if item not in self.__items:
            raise ItemNotFoundError(f"{item.title} ({item.year}) by {item.author} (ID: {item.id})")
        
        # Check if item is available
        if not item.available:
            raise ItemNotAvailableError(f"{item.title} ({item.year}) by {item.author}")
        
        # Add item to user's borrowed items
        user.add_borrowed_item(item.id)
        # Mark item as unavailable
        item.available = False
        return True

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
        self.__isItem(item)
        self.__isUser(user)
    
        # Check if user exists in the library
        if user not in self.users:
            raise UserNotFoundError(f"{user.first_name} {user.last_name} (ID: {user.id})")
        
        # Check if item exists in the library
        if item not in self.items:
            raise ItemNotFoundError(f"{item.title} ({item.year}) by {item.author} (ID: {item.id})")
        
        # Check if user has borrowed the item
        if item.id not in user.borrowed_items:
            raise ItemNotBorrowedError(f"{item.title} ({item.year}) by {item.author}", f"{user.first_name} {user.last_name}")
        
        # Remove item from user's borrowed items
        user.remove_borrowed_item(item.id)
        # Mark item as available
        item.available = True
        return True
