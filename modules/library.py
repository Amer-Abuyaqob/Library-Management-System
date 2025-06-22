import json
import os

from user import User
from book import Book
from magazine import Magazine
from dvd import DVD

from exceptions import (
    ItemNotFoundError,
    UserNotFoundError,
    ItemNotAvailableError,
    ItemNotBorrowedError,
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
        if not isinstance(item, (Book, DVD, Magazine)):
            raise ItemNotFoundError("Invalid item type")

        if any(existing_item.id == item.id for existing_item in self.items):
            raise ValueError(f"Item with ID '{item.id}' already exists")

        self.items.append(item)
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
        # FIXME: exception handling
        index = self.items.index(item)
        self.items[index] = new_item

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
        # FIXME: exception handling
        self.items.remove(item)

    def add_user(self, user):
        """
        Add a new user to the library.
        Args:
            user: User object to add
        Returns:
            bool: True if user was added successfully, False otherwise
        Raises:
            ValueError: If user with same ID already exists
            UserNotFoundError: If user is not an instance of User
        """
        if not isinstance(user, User):
            raise UserNotFoundError("Invalid user type")

        if any(existing_user.id == user.id for existing_user in self.users):
            raise ValueError(f"User with ID '{user.id}' already exists")

        self.users.append(user)
        return True
    
    def remove_user(self, user):
        """
        Remove a user from the library.
        Args:
            user_id: ID of the user to remove
        Returns:
            bool: True if user was removed successfully, False otherwise
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        # FIXME: exception handling
        self.users.remove(user)

    def update_user(self, user, new_user):
        """
        Update a user's attributes.
        Args:
            user_id: ID of the user to update
            **kwargs: Key-value pairs of attributes to update
        Returns:
            bool: True if update was successful, False otherwise
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        # FIXME: exception handling
        index = self.users.index(user)
        self.users[index] = new_user

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
            raise ValueError("Item entry must be a dictionary")

        # Common mandatory fields for all items
        required_fields = {
            "type": str,
            "title": str,
            "author": str,
            "year": int,
            "available": bool,
        }

        for field, expected_type in required_fields.items():
            if field not in item:
                raise ValueError(f"Missing required field '{field}' in item entry")
            if not isinstance(item[field], expected_type):
                raise ValueError(
                    f"Field '{field}' must be of type {expected_type.__name__}"
                )

        # Optional validation for reserved or borrowed_items fields
        if "reserved" in item and not isinstance(item["reserved"], bool):
            raise ValueError("'reserved' must be a boolean if provided")
        if "borrowed_items" in item:
            borrowed = item["borrowed_items"]
            if not isinstance(borrowed, list) or not all(isinstance(i, str) for i in borrowed):
                raise ValueError("'borrowed_items' must be a list of strings")

        item_type = item["type"]

        if item_type == "Book":
            if "genre" not in item or not isinstance(item["genre"], str):
                raise ValueError("Book entry must have a 'genre' string field")
            item_obj = Book(
                item["title"], item["author"], item["year"], item["available"], item["genre"]
            )
        elif item_type == "Magazine":
            if "genre" not in item or not isinstance(item["genre"], str):
                raise ValueError("Magazine entry must have a 'genre' string field")
            item_obj = Magazine(
                item["title"], item["author"], item["year"], item["available"], item["genre"]
            )
        elif item_type == "DVD":
            if "duration" not in item or not isinstance(item["duration"], int):
                raise ValueError("DVD entry must have a numeric 'duration' field")
            item_obj = DVD(
                item["title"], item["author"], item["year"], item["available"], item["duration"]
            )
        else:
            raise ValueError(f"Unknown item type '{item_type}'")

        return item_obj
    
    def __load_items(self):
        """
        Load items from JSON file.
        Reads items.json to populate the library's items list.
        """
        self.__items = []  # Clearing the items list to avoid duplicates
        # FIXME: exception handling for file and data
        with open(self.__items_file, "r", encoding="utf-8") as f:
            items_data = json.load(f)

        for item in items_data:
            item_obj = self.__create_item(item)
            self.add_item(item_obj)

    def __load_users(self):
        """
        Loads users from JSON file.
        Reads users.json to populate the library's users list.
        """
        self.__users = []  # Clearing the items list to avoid duplicates

        # FIXME: exception handling for file and data
        with open(self.__users_file, "r", encoding="utf-8") as f:
            users_data = json.load(f)

        for user in users_data:
            user_obj = User(user["id"], user["first_name"], user["last_name"])

            # Add borrowed items by matching IDs with already loaded items
            for item_id in user.get("borrowed_items", []):
                # Find the corresponding item in the library
                for item in self.items:
                    if item.id == item_id:
                        user_obj.add_borrowed_item(item)
                        # Keep the item's availability in sync with the user
                        item.available = False
                        break

            self.add_user(user_obj)

    def load_data(self):
        """
        Load library data from JSON files.
        Reads items.json and users.json to populate the library's items and users.
        Raises FileNotFoundError if files don't exist.
        """
        try:
            self.__load_items()
            self.__load_users()
        except FileNotFoundError as exc:
            raise FileNotFoundError("Data files not found") from exc
        finally:
            print("Finished loading data")


    def __item_entry(self, item):
        entry = {
                "type": item.__class__.__name__,
                "title": item.title,
                "author": item.author,
                "year": item.year,
                "available": item.available,
                "id": item.id,
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

        # FIXME: add better exception handling for files and data
        try:
            os.makedirs(os.path.dirname(self.__items_file), exist_ok=True)
            with open(self.__items_file, "w", encoding="utf-8") as f:
                json.dump(items_data, f, indent=2)
        except OSError as exc:
            raise IOError("Failed to save data") from exc
        finally:
            print("Finished saving items")

    def __save_users(self):
        users_data = []
        for user in self.__users:
            entry = self.__user_entry(user)
            users_data.append(entry)

        # FIXME: add better exception handling for files and data
        try:
            os.makedirs(os.path.dirname(self.__users_file), exist_ok=True)
            with open(self.__users_file, "w", encoding="utf-8") as f:
                json.dump(users_data, f, indent=2)
        except OSError as exc:
            raise IOError("Failed to save data") from exc
        finally:
            print("Finished saving users")

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
        # Check if user exists in the library
        if user not in self.users:
            raise UserNotFoundError(f"User '{user.id}' not found in the library")
        
        # Check if item exists in the library
        if item not in self.items:
            raise ItemNotFoundError(f"Item '{item.id}' not found in the library")
        
        # Check if item is available
        if not item.available:
            raise ItemNotAvailableError(f"Item '{item.id}' is not available for borrowing")
        
        # Add item to user's borrowed items
        user.add_borrowed_item(item)
        
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
        # Check if user exists in the library
        if user not in self.users:
            raise UserNotFoundError(f"User '{user.id}' not found in the library")
        
        # Check if item exists in the library
        if item not in self.items:
            raise ItemNotFoundError(f"Item '{item.id}' not found in the library")
        
        # Check if user has borrowed the item
        if item not in user.borrowed_items:
            raise ItemNotBorrowedError(
                f"User '{user.id}' has not borrowed item '{item.id}'"
            )
        
        # Remove item from user's borrowed items
        user.remove_borrowed_item(item)
        
        # Mark item as available
        item.available = True
        
        return True
