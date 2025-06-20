import json
import os

from library_item import LibraryItem
from user import User
from book import Book
from magazine import Magazine
from dvd import DVD

class Library:
    def __init__(self):
        self.items_file = os.path.join("data", "items.json")
        self.users_file = os.path.join("data", "users.json")
        self.items = []
        self.users = []
        
        self.load_data()

    def load_data(self) -> None:
        """
        Load library data from JSON files.
        Reads items.json and users.json to populate the library's items and users.
        Raises FileNotFoundError if files don't exist.
        """
        # Load items
        self.items = []
        if os.path.exists(self.items_file):
            with open(self.items_file, "r", encoding="utf-8") as f:
                items_data = json.load(f)

            for item in items_data:
                item_type = item.get("type")

                if item_type == "Book":
                    obj = Book(item["title"], item["author"], item["year"], item["available"], item["genre"])

                elif item_type == "Magazine":
                    obj = Magazine(item["title"], item["author"], item["year"], item["available"], item["genre"])

                elif item_type == "DVD":
                    obj = DVD(item["title"], item["author"], item["year"], item["available"], item["duration"])
                    
                else:
                    continue

                self.items.append(obj)

        # Load users (kept as dictionaries since User class is not implemented)
        if os.path.exists(self.users_file):
            with open(self.users_file, "r", encoding="utf-8") as f:
                self.users = json.load(f)
        else:
            self.users = []

    def save_data(self) -> None:
        """
        Save library data to JSON files.
        Writes current items and users to items.json and users.json respectively.
        Raises IOError if writing to files fails.
        """
        items_data = []
        for item in self.items:
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
            items_data.append(entry)

        try:
            with open(self.items_file, "w", encoding="utf-8") as f:
                json.dump(items_data, f, indent=2)
            with open(self.users_file, "w", encoding="utf-8") as f:
                json.dump(self.users, f, indent=2)
        except OSError as exc:
            raise IOError("Failed to save data") from exc

    def display_all_items(self) -> None:
        """
        Display all items in the library.
        Prints formatted information about each item including availability status.
        """
        # TODO: Implement formatted display of all items
        pass

    def add_item(self, item: LibraryItem) -> bool:
        """
        Add a new item to the library.
        Args:
            item: LibraryItem object to add
        Returns:
            bool: True if item was added successfully, False otherwise
        Raises:
            ValueError: If item with same ID already exists
        """
        # TODO: Implement item addition with duplicate ID check
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
        # TODO: Implement formatted display of all users
        pass

    def add_user(self, user: User) -> bool:
        """
        Add a new user to the library.
        Args:
            user: User object to add
        Returns:
            bool: True if user was added successfully, False otherwise
        Raises:
            ValueError: If user with same ID already exists
        """
        # TODO: Implement user addition with duplicate ID check
        pass

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
