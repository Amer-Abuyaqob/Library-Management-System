import json
import os

from library_item import LibraryItem
from user import User
from book import Book
from magazine import Magazine
from dvd import DVD

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
        """
        # FIXME: exeption handling
        self.items.append(item)

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
        # FIXME: exeption handling
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
        # FIXME: exeption handling
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
        """
        # FIXME: exeption handling
        self.users.append(user)
    
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
        # FIXME: exeption handling
        self.users.remove(user)
        pass

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
        # FIXME: exeption handling
        index = self.users.index(user)
        self.users[index] = new_user

    def __create_item(self, item):
        item_type = item.get("type")
        if item_type == "Book":
            item_obj = Book(item["title"], item["author"], item["year"], item["available"], item["genre"])
        elif item_type == "Magazine":
            item_obj = Magazine(item["title"], item["author"], item["year"], item["available"], item["genre"])
        elif item_type == "DVD":
            item_obj = DVD(item["title"], item["author"], item["year"], item["available"], item["duration"])
        return item_obj
    
    def __load_items(self):
        """
        Load items from JSON file.
        Reads items.json to populate the library's items list.
        """
        self.__items = []  # Clearing the items list to avoid duplicates
        # FIXME: exeption handling for file and data
        if os.path.exists(self.__items_file):
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

<<<<<<< HEAD
=======
        # FIXME: exeption handling for file and data
        if os.path.exists(self.__users_file):
            with open(self.__users_file, "r", encoding="utf-8") as f:
                users_data = json.load(f)

            for user in users_data:
                user_obj = User(user["id"], user["first_name"], user["last_name"])

                # FIXME: currently causes error 
                # FIXME: insure compatibility with User class
                # Load borrowed items if they exist
                if "borrowed_items" in user:
                    for item_id in user["borrowed_items"]:
                        user_obj.borrow_item(item_id)
                
                self.add_user(user_obj)

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

        # FIXME: add better exeption handling for files and data
        try:
            with open(self.__items_file, "w", encoding="utf-8") as f:
                json.dump(items_data, f, indent=2)
        except OSError as exc:
            raise IOError("Failed to save data") from exc

    def __save_users(self):
        users_data = []
        for user in self.__users:
            entry = self.__user_entry(user)
            users_data.append(entry)

        # FIXME: add better exeption handling for files and data
        try:
            with open(self.__users_file, "w", encoding="utf-8") as f:
                json.dump(users_data, f, indent=2)
        except OSError as exc:
            raise IOError("Failed to save data") from exc

    def save_data(self):
        """
        Saves library data to JSON files.
        Writes current items and users to items.json and users.json respectively.
        Raises IOError if writing to files fails.
        """
        self.__save_items()
        self.__save_users()

>>>>>>> bb67d8d7bbdd252cf36c7dd5e96820884624b83f
    def borrow_item(self, user, item):
        """
        Borrow an item for a user.
        Args:
            user: User object borrowing the item
            item: LibraryItem object to borrow
        Returns:
            bool: True if item was borrowed successfully, False otherwise
        Raises:
            ValueError: If user doesn't exist, item doesn't exist, or item is not available
        """
        # Check if user exists in the library
        if user not in self.users:
            raise ValueError(f"User '{user.id}' not found in the library")
        
        # Check if item exists in the library
        if item not in self.items:
            raise ValueError(f"Item '{item.id}' not found in the library")
        
        # Check if item is available
        if not item.available:
            raise ValueError(f"Item '{item.id}' is not available for borrowing")
        
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
            ValueError: If user doesn't exist, item doesn't exist, or user hasn't borrowed the item
        """
        # Check if user exists in the library
        if user not in self.users:
            raise ValueError(f"User '{user.id}' not found in the library")
        
        # Check if item exists in the library
        if item not in self.items:
            raise ValueError(f"Item '{item.id}' not found in the library")
        
        # Check if user has borrowed the item
        if item not in user.borrowed_items:
            raise ValueError(f"User '{user.id}' has not borrowed item '{item.id}'")
        
        # Remove item from user's borrowed items
        user.remove_borrowed_item(item)
        
        # Mark item as available
        item.available = True
        
        return True
