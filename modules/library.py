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
        # FIXME: duplicate item_id check
        # FIXME: exeption handling
        self.__item.append(item)

    def update_item(self, item_id: str, **kwargs) -> bool:
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
        # TODO: Implement item attribute updates
        pass

    def remove_item(self, item_id: str) -> bool:
        """
        Remove an item from the library.
        Args:
            item_id: ID of the item to remove
        Returns:
            bool: True if item was removed successfully, False otherwise
        Raises:
            ItemNotFoundError: If item doesn't exist
        """
        # TODO: Implement item removal with existence check
        pass

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
        # FIXME: duplicate user_id check
        # FIXME: exeption handling
        self.__users.append(user)
    
    def remove_user(self, user_id: str) -> bool:
        """
        Remove a user from the library.
        Args:
            user_id: ID of the user to remove
        Returns:
            bool: True if user was removed successfully, False otherwise
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        # TODO: Implement user removal with existence check
        pass

    def update_user(self, user_id: str, **kwargs) -> bool:
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
        # TODO: Implement user attribute updates
        pass

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

        # FIXME: exeption handling for file and data
        if os.path.exists(self.__users_file):
            with open(self.__users_file, "r", encoding="utf-8") as f:
                users_data = json.load(f)

            for user in users_data:
                user_obj = User(user["id"], user["first_name"], user["last_name"])

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

    def display_all_items(self) -> None:
        """
        Display all items in the library.
        Prints formatted information about each item including availability status.
        """
        # FIXME: might be moved to Main class
        # TODO: Implement formatted display of all items
        pass

    def search_item_by_id(self, item_id: str) -> LibraryItem:
        """
        Search for an item by its ID.
        Args:
            item_id: ID of the item to find
        Returns:
            LibraryItem: The found item
        Raises:
            ItemNotFoundError: If item doesn't exist
        """
        # TODO: Implement item search by ID
        pass

    def search_item_by_title(self, title: str) -> list[LibraryItem]:
        """
        Search for items by title.
        Args:
            title: Title to search for
        Returns:
            list[LibraryItem]: List of items matching the title
        """
        # TODO: Implement case-insensitive title search
        pass

    def search_item_by_author(self, author: str) -> list[LibraryItem]:
        """
        Search for items by author.
        Args:
            author: Author name to search for
        Returns:
            list[LibraryItem]: List of items by the author
        """
        # TODO: Implement case-insensitive author search
        pass

    def search_item_by_type(self, item_type: str) -> list[LibraryItem]:
        """
        Search for items by type (Book, Magazine, DVD).
        Args:
            item_type: Type of item to search for
        Returns:
            list[LibraryItem]: List of items of the specified type
        """
        # TODO: Implement type-based item filtering
        pass

    def display_all_users(self) -> None:
        """
        Display all users in the library.
        Prints formatted information about each user including their borrowed items.
        """
        # FIXME: might be moved to Main class
        # TODO: Implement formatted display of all users
        pass

    def search_user_by_id(self, user_id: str) -> User:
        """
        Search for a user by their ID.
        Args:
            user_id: ID of the user to find
        Returns:
            User: The found user
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        # TODO: Implement user search by ID
        pass

    def search_user_by_first_name(self, first_name: str) -> list[User]:
        """
        Search for users by first name.
        Args:
            first_name: First name to search for
        Returns:
            list[User]: List of users with matching first name
        """
        # TODO: Implement case-insensitive first name search
        pass

    def search_user_by_last_name(self, last_name: str) -> list[User]:
        """
        Search for users by last name.
        Args:
            last_name: Last name to search for
        Returns:
            list[User]: List of users with matching last name
        """
        # TODO: Implement case-insensitive last name search
        pass

    def borrow_item(self, user_id: str, item_id: str) -> bool:
        """
        Borrow an item for a user.
        Args:
            user_id: ID of the user borrowing the item
            item_id: ID of the item to borrow
        Returns:
            bool: True if item was borrowed successfully, False otherwise
        Raises:
            UserNotFoundError: If user doesn't exist
            ItemNotFoundError: If item doesn't exist
            ItemNotAvailableError: If item is not available
        """
        # TODO: Implement item borrowing with all necessary checks
        pass

    def return_item(self, user_id: str, item_id: str) -> bool:
        """
        Return an item from a user.
        Args:
            user_id: ID of the user returning the item
            item_id: ID of the item to return
        Returns:
            bool: True if item was returned successfully, False otherwise
        Raises:
            UserNotFoundError: If user doesn't exist
            ItemNotFoundError: If item doesn't exist
            ValueError: If user hasn't borrowed the item
        """
        # TODO: Implement item return with all necessary checks
        pass
