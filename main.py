"""
Library Management System Main Application Module

This module contains the main application logic and user interface for the
Library Management System. It provides a comprehensive command-line interface
for managing library operations including item and user management, borrowing,
and returning.

The module consists of:
- Utility functions for input validation and user interaction
- The Main class that orchestrates the user interface
- Comprehensive menu system with multiple levels
- Input validation and error handling for all user inputs

Key Features:
- Interactive menu-driven interface
- Comprehensive input validation
- Error handling with user-friendly messages
- Data persistence through the Library class
- Support for all library operations

Menu Structure:
- Main Menu: Items, Users, Borrow/Return, Exit
- Items Menu: View, Add, Remove, Update
- Users Menu: View, Add, Remove, Update
- Borrow/Return Menu: Borrow Item, Return Item

All user inputs are validated and sanitized to ensure data integrity
and prevent system errors.
"""

from modules.library import Library
from modules.book import Book
from modules.dvd import DVD
from modules.magazine import Magazine
from modules.user import User
from modules.exceptions import (
    ItemNotAvailableError,
    ItemNotFoundError,
    UserNotFoundError,
    ItemAlreadyExistsError,
    UserAlreadyExistsError,
    InvalidDataTypeError,
    InvalidValueError,
    MissingFieldError,
    ItemNotBorrowedError,
    InvalidItemIDFormatError,
    InvalidUserIDFormatError,
    ItemNotAvailableForOperationError,
    UserHasBorrowedItemsError,
)
import json
import os

# IMPORTANT
def print_menu_header(title: str) -> None:
    """
    Print a formatted menu header with consistent styling.
    
    Creates a visually appealing header with separator lines and centered text.
    
    Args:
        title (str): The title to display in the header
    """
    print()
    separator = "=" * 40
    print(separator)
    print(title.center(len(separator)))
    print(separator)

# IMPORTANT
def print_menu_options(options: list[str]) -> None:
    """
    Print menu options using a consistent style.
    
    Displays numbered options with proper indentation for easy reading.
    
    Args:
        options (list[str]): List of menu options to display
    """
    for option in options:
        print(f"  {option}")


def insure_decision():
    """
    Get a yes/no decision from the user with validation.
    
    Prompts the user for a yes/no decision and validates the input.
    Accepts various forms of yes/no responses (yes, y, no, n).
    
    Returns:
        bool: True for yes, False for no
        
    Raises:
        InvalidValueError: If the input is not a valid yes/no response
    """
    while True:
        try:
            decision = input("  Yes or No? ").strip()
            if decision in {"yes", "y"}:
                print()
                return True            
            elif decision in {"no", "n"}:
                print()
                return False
            else:
                raise InvalidValueError("Your decision must be 'yes' or 'no'.")
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue

# IMPORTANT
def validate_choice(choice, num_options):
    """
    Validate a menu choice input.
    
    Ensures the choice is a valid integer within the range of available options.
    
    Args:
        choice: The user's choice input
        num_options (int): The number of available options
        
    Returns:
        int: The validated choice as an integer
        
    Raises:
        InvalidDataTypeError: If choice is not a valid integer
        InvalidValueError: If choice is outside the valid range
    """
    if not choice.isdigit():
        raise InvalidDataTypeError("integer", type(choice).__name__)
    choice = int(choice)
    if choice <= 0 or choice > num_options:
        raise InvalidValueError("Your choice should be a number from the menu")
    return choice

# IMPORTANT    
def validate_type(kind):
    """
    Validate an item type input.
    
    Ensures the type is one of the supported item types.
    
    Args:
        kind: The item type to validate
        
    Raises:
        InvalidDataTypeError: If kind is not a string
        InvalidValueError: If kind is not a supported item type
    """
    if not isinstance(kind, str):
        raise InvalidDataTypeError("string", type(kind).__name__)
    if kind not in ["Book", "DVD", "Magazine"]:
        raise InvalidValueError("Item type must be 'Book', 'DVD', or 'Magazine'.")

# IMPORTANT
def validate_author(author):
    """
    Validate an author name input.
    
    Ensures the author name is a non-empty string with at least 2 characters.
    
    Args:
        author: The author name to validate
        
    Raises:
        InvalidDataTypeError: If author is not a string
        InvalidValueError: If author is empty or too short
    """
    if not isinstance(author, str):
        raise InvalidDataTypeError("string", type(author).__name__)
    if len(author.strip()) < 2:
        raise InvalidValueError("Author's name must be a non-empty string with at least two characters.")

# IMPORTANT
def validate_title(title):
    """
    Validate a title input.
    
    Ensures the title is a non-empty string.
    
    Args:
        title: The title to validate
        
    Raises:
        InvalidDataTypeError: If title is not a string
        InvalidValueError: If title is empty
    """
    if not isinstance(title, str):
        raise InvalidDataTypeError("string", type(title).__name__)
    if not title:
        raise InvalidValueError("Title's name must be a non-empty string.")
    
# IMPORTANT
def validate_available(available):
    """
    Validate an availability input.
    
    Converts various forms of yes/no responses to boolean values.
    
    Args:
        available: The availability input to validate
        
    Returns:
        bool: True for available, False for not available
        
    Raises:
        InvalidDataTypeError: If available is not a string
        InvalidValueError: If available is not a valid yes/no response
    """
    if not isinstance(available, str):
        raise InvalidDataTypeError("string", type(available).__name__)
    if available in {"true", "t", "yes", "y", "1"}:
        return True            
    elif available in {"false", "f", "no", "n", "0"}:
        return False
    else:
        raise InvalidValueError("Availability must be a 'yes' or 'no'.")

# IMPORTANT
def validate_year(year):
    """
    Validate a year input.
    
    Ensures the year is a positive integer.
    
    Args:
        year: The year to validate
        
    Returns:
        int: The validated year as an integer
        
    Raises:
        InvalidDataTypeError: If year is not a valid integer
        InvalidValueError: If year is not positive
    """
    if not year.isdigit():
        raise InvalidDataTypeError("integer", type(year).__name__)
    year = int(year)
    if year <= 0:
        raise InvalidValueError("Year must be a positive non-zero integer.")
    return year

# IMPORTANT
def validate_genre(genre):
    """
    Validate a genre input.
    
    Ensures the genre is a non-empty string.
    
    Args:
        genre: The genre to validate
        
    Raises:
        InvalidDataTypeError: If genre is not a string
        InvalidValueError: If genre is empty
    """
    if not isinstance(genre, str):
        raise InvalidDataTypeError("string", type(genre).__name__)
    if not genre:
        raise InvalidValueError("Genre must be a non-empty string.")

# IMPORTANT
def validate_duration(duration):
    """
    Validate a duration input.
    
    Ensures the duration is a positive integer.
    
    Args:
        duration: The duration to validate
        
    Returns:
        int: The validated duration as an integer
        
    Raises:
        InvalidDataTypeError: If duration is not a valid integer
        InvalidValueError: If duration is not positive
    """
    if not duration.isdigit():
        raise InvalidDataTypeError("integer", type(duration).__name__)
    duration = int(duration)
    if duration <= 0:
        raise InvalidValueError("Duration must be a positive non-zero integer.")
    return duration

# IMPORTANT
def validate_item_id(item_id):
    """
    Validate an item ID format.
    
    Ensures the item ID follows the required format: T-Aa-YYYY-N
    Where T is the item type (B/D/M), Aa are author initials,
    YYYY is the publication year, and N is a sequential number.
    
    Args:
        item_id: The item ID to validate
        
    Raises:
        InvalidDataTypeError: If item_id is not a string
        InvalidValueError: If item_id is empty or has invalid format
        InvalidItemIDFormatError: If item_id doesn't follow the required format
    """
    if not isinstance(item_id, str):
        raise InvalidDataTypeError("string", type(item_id).__name__)
    if not item_id:
        raise InvalidValueError("Item's ID must be a non-empty string.")
    parts = item_id.split('-')
    if len(parts) != 4:
        raise InvalidItemIDFormatError(item_id)
    t, aa, yyyy, n = parts
    # T: B, D, or M
    if t not in ['B', 'D', 'M']:
        raise InvalidItemIDFormatError(item_id)
    # Aa: two uppercase letters
    if len(aa) != 2 or not aa.isalpha():
        raise InvalidItemIDFormatError(item_id)
    # YYYY: 4 digits
    if not yyyy.isdigit():
        raise InvalidItemIDFormatError(item_id)
    # N: positive integer
    if not n.isdigit() or int(n) <= 0:
        raise InvalidItemIDFormatError(item_id)

# IMPORTANT
def validate_user_name(name, kind):
    """
    Validate a user name input.
    
    Ensures the name is a non-empty string with at least 2 characters.
    
    Args:
        name: The name to validate
        kind: The type of name (e.g., "first", "last") for error messages
        
    Raises:
        InvalidDataTypeError: If name is not a string
        InvalidValueError: If name is empty or too short
    """
    if not isinstance(name, str):
        raise InvalidDataTypeError("string", type(name).__name__)
    if len(name.strip()) < 2:
        raise InvalidValueError(f"User's {kind} must be a non-empty string with at least two characters.")

# IMPORTANT
def validate_user_id(user_id):
    """
    Validate a user ID format.
    
    Ensures the user ID follows the required format: U-Ff-Ll-N
    Where U is the user identifier, Ff are first name initials,
    Ll are last name initials, and N is a sequential number.
    
    Args:
        user_id: The user ID to validate
        
    Raises:
        InvalidDataTypeError: If user_id is not a string
        InvalidValueError: If user_id is empty or has invalid format
        InvalidUserIDFormatError: If user_id doesn't follow the required format
    """
    if not isinstance(user_id, str):
        raise InvalidDataTypeError("string", type(user_id).__name__)
    if not user_id:
        raise InvalidValueError("User's ID must be a non-empty string.")
    parts = user_id.split('-')
    if len(parts) != 4:
        raise InvalidUserIDFormatError(user_id)
    u, ff, ll, n = parts
    # U: must be 'U'
    if u != 'U':
        raise InvalidUserIDFormatError(user_id)
    # Ff: two letters
    if len(ff) != 2 or not ff.isalpha():
        raise InvalidUserIDFormatError(user_id)
    # Ll: two letters
    if len(ll) != 2 or not ll.isalpha():
        raise InvalidUserIDFormatError(user_id)
    # N: positive integer
    if not n.isdigit() or int(n) <= 0:
        raise InvalidUserIDFormatError(user_id)

# IMPORTANT
def take_choice(num_options):
    """
    Get a validated menu choice from the user.
    
    Prompts the user for input and validates it against the available options.
    Continues prompting until a valid choice is provided.
    
    Args:
        num_options (int): The number of available menu options
        
    Returns:
        int: The validated user choice
    """
    while True:
        try:
            choice = input("  Enter choice: ")
            return validate_choice(choice, num_options)
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue

# IMPORTANT
def take_type():
    """
    Get a validated item type from the user.
    
    Prompts the user for an item type and validates it against supported types.
    Continues prompting until a valid type is provided.
    
    Returns:
        str: The validated item type (Book, DVD, or Magazine)
    """
    while True:
        try:
            kind = input("  Enter the item's type (Book/DVD/Magazine): ").strip()
            print()
            validate_type(kind)
            return kind
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue

# IMPORTANT
def take_author():
    while True:
        try:
            author = input("  Enter the item's author: ").strip()
            print()
            validate_author(author)
            return author
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue

# IMPORTANT
def take_title():
    while True:
        try:
            title = input("  Enter the item's title: ").strip()
            print()
            validate_title(title)
            return title
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue

# IMPORTANT
def take_available():
    while True:
        try:
            available = input("  Is the item available? ").strip()
            print()
            return validate_available(available)
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue

# IMPORTANT
def take_item_id():
    while True:
        try:
            item_id = input("  Enter the item's ID: ").strip()
            print()
            validate_item_id(item_id)
            return item_id
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue
        except InvalidItemIDFormatError as e:
            print(f"  ✗ Invalid input: {e}")
            print()
            continue

# IMPORTANT
def take_year():
    while True:
        try:
            year = input("  Enter the item's publish year: ").strip()
            print()
            return validate_year(year)
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue

# IMPORTANT
def take_genre():
    while True:
        try:
            genre = input("  Enter the item's genre: ").strip()
            print()
            validate_genre(genre)
            return genre
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue

# IMPORTANT
def take_duration():
    while True:
        try:
            duration = input("  Enter DVD duration in minutes: ").strip()
            print()
            return validate_duration(duration)
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue

# IMPORTANT
def get_item_data():
    type = take_type()
    title = take_title()
    author = take_author()
    year = take_year()
    available = take_available()
    special = ""
    if type in ["Book", "Magazine"]:
        special = take_genre()
    else:
        special = take_duration()
    return type, title, author, year, available, special

# IMPORTANT
def create_item():
    type, title, author, year, available, special = get_item_data()
    match type:
        case "Book":
            item = Book(title, author, year, available, special)

        case "DVD":
            item = DVD(title, author, year, available, special)

        case "Magazine":
            item = Magazine(title, author, year, available, special)
    return item

# IMPORTANT
def take_user_name(kind):
    while True:
        try:
            user_name = input(f"  Enter the user's {kind}: ").strip()
            print()
            validate_user_name(user_name, kind)
            return user_name
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue

# IMPORTANT
def take_user_id():
    while True:
        try:
            user_id = input("  Enter the uaer's ID: ").strip()
            print()
            validate_user_id(user_id)
            return user_id
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            print()
            continue
        except InvalidUserIDFormatError as e:
            print(f"  ✗ Invalid input: {e}")
            print()
            continue

# IMPORTANT
def get_user_data():
    first_name = take_user_name("first name")
    last_name = take_user_name("last name")
    return first_name, last_name

# IMPORTANT
def create_user():
    first_name, last_name = get_user_data()
    return User(first_name, last_name)

# ===================== INIT & DATA LOADING =====================
class Main:
    """
    Main application controller class.
    
    This class orchestrates the entire user interface and manages the interaction
    between the user and the library system. It provides a comprehensive menu
    system with multiple levels of navigation and handles all user interactions.
    
    The Main class is responsible for:
    - Displaying menus and handling user navigation
    - Collecting and validating user input
    - Coordinating with the Library class for all operations
    - Providing user-friendly error messages
    - Managing the application lifecycle
    
    Attributes:
        library (Library): The main library instance that manages all data
    """
    
    def __init__(self):
        try:
            self.library = Library()
            self.group_by_type()
        except FileNotFoundError:
            print("Warning: Data files not found. Starting with empty library.")
            self.library = Library()
        except json.JSONDecodeError as e:
            print(f"  ✗ Error: Invalid JSON in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except MissingFieldError as e:
            print(f"  ✗ Error: Missing required field in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except InvalidDataTypeError as e:
            print(f"  ✗ Error: Invalid data type in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except InvalidValueError as e:
            print(f"  ✗ Error: Invalid value in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except ItemNotFoundError as e:
            print(f"  ✗ Error: Item not found in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except ItemAlreadyExistsError as e:
            print(f"  ✗ Error: Duplicate item in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except UserAlreadyExistsError as e:
            print(f"  ✗ Error: Duplicate user in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except Exception as e:
            print(f"  ✗ Error loading library data: {e}")
            print("Starting with empty library.")
            self.library = Library()
    
    # ===================== ITEM GROUPING & SUMMARY =====================
    # IMPORTANT
    def group_by_type(self):
        self.books = []
        self.dvds = []
        self.magazines = []
        for item in self.library.items:
            if isinstance(item, Book):
                self.books.append(item)
            elif isinstance(item, DVD):
                self.dvds.append(item)
            elif isinstance(item, Magazine):
                self.magazines.append(item)

    # IMPORTANT
    def items_summary(self, books, dvds, magazines):
        print("  SUMMARY:")
        print(f"    Books: {len(books)}")
        print(f"    Magazines: {len(magazines)}")
        print(f"    DVDs: {len(dvds)}")
        print(f"    Total: {len(self.library.items)}")
        
    # IMPORTANT
    def users_summary(self):
        print("  USERS SUMMARY:")
        print(f"    Total Users: {len(self.library.users)}")
        
    # ===================== ITEM VIEWING =====================
    # IMPORTANT
    def display_info(self, items):
        for item in items:
            print(item.display_info())
            print()
           
    # IMPORTANT
    def items_view_all(self):
        print_menu_header("  Viewing all library items...")
        print()
        if not self.library.items:
            print("  No items found in the library.")
            return
        self.group_by_type()

        print("📚 BOOKS")
        if not self.books:
            print("  No books to display.")
            print()
        else:
            self.display_info(self.books)
            
        print("📀 DVDS")
        if not self.dvds:
            print("  No dvds to display.")
            print()
        else:
            self.display_info(self.dvds)

        print("📰 MAGAZINES")
        if not self.magazines:
            print("  No magazines to display.")
            print()
        else:
            self.display_info(self.magazines)

        self.items_summary(self.books, self.dvds, self.magazines)
        print()

    # IMPORTANT
    def items_view_type(self):
        print_menu_header("Viewing items by type")
        type = take_type()
        print(f"  Viewing all items of type: {type}...")
        print()
        found = False
        self.group_by_type()
        match type:
            case "Book":
                if self.books:
                    found = True
                    print("📚 BOOKS")
                    self.display_info(self.books)
            case "DVD":
                if self.dvds:
                    found = True
                    print("📀 DVDS")
                    self.display_info(self.dvds)
            case "Magazine":
                if self.magazines:
                    found = True
                    print("📰 MAGAZINES")
                    self.display_info(self.magazines)
        if not found:
            print(f"  No items found of type: {type}")
        print()

    # IMPORTANT
    def items_view_title(self):
        print_menu_header("Viewing items by title")
        title = take_title()
        print(f"  Viewing all items of title: {title}...")
        print()
        found = False
        for item in self.library.items:
            if item.title.lower() == title.lower():
                print(item.display_info())
                found = True
        if not found:
            print(f"  No items found with title: {title}")
        print()
    
    # IMPORTANT
    def items_view_author(self):
        print_menu_header("Viewing items by author")
        author = take_author()        
        print(f"  Viewing all items of author: {author}...")
        print()
        found = False
        for item in self.library.items:
            if item.author.lower() == author.lower():
                print(item.display_info())
                found = True
        if not found:
            print(f"  No items found by author: {author}")
        print()
    
    # IMPORTANT
    def items_view_id(self):
        print_menu_header("Viewing item by ID")
        item_id = take_item_id()
        print(f"  Viewing the item with ID: {item_id}...")
        print()
        found = False
        for item in self.library.items:
            if item.id == item_id:
                print(item.display_info())
                found = True
        if not found:
            print(f"  No item found with ID: {item_id}")
        print()

    # IMPORTANT
    def items_view_options(self):
        while True:
            items_view_option = take_choice(6)

            match items_view_option:
                case 1:
                    print()
                    self.items_view_all()
                    break
                case 2:
                    self.items_view_type()
                    break
                case 3:
                    self.items_view_author()
                    break
                case 4:
                    self.items_view_title()
                    break
                case 5:
                    self.items_view_id()
                    break
                case 6:
                    return True
        return False

    # IMPORTANT
    def items_view_menu(self):
        while True:
            print_menu_header("Items Viewing Menu")
            print_menu_options([
                "1- View all items",
                "2- View by type",
                "3- View by author",
                "4- View by title",
                "5- View by Item ID",
                "6- Back",
            ])
            if self.items_view_options():
                break
            print()
        print()

    # ===================== ITEM CREATION & MODIFICATION =====================

    # IMPORTANT
    def items_add_menu(self):
        print_menu_header("Adding an Item")
        while True:
            try:
                item = create_item()
                if self.library.add_item(item):
                    print(f"  ✓ Item '{item.title}' has been added successfully.")
                    break
                else:
                    print(f"  ✗ Item '{item.title}' has NOT been added.")
                    break
            except InvalidDataTypeError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except ItemAlreadyExistsError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ Item '{item.title}' has NOT been added.")
                print()
                break
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                print(f"  ✗ Item '{item.title}' has NOT been added.")
                print()
                break
        print()

    def items_remove_menu(self):
        print_menu_header("Removing an Item")
        while True:
            try:
                item_id = take_item_id()
                item = self.library.get_item(item_id)
                if item:
                    print(f"  Item '{item_id}' info:")
                    print(item.display_info())
                    print()
                    
                    # Check if item is available (not borrowed)
                    if not item.available:
                        raise ItemNotAvailableForOperationError(item_id, "removed")
                    
                    print(f"  Are sure you want to remove item '{item_id}'? ")
                    if insure_decision():
                        if self.library.remove_item(item):
                            print(f"  ✓ Item '{item_id}' has been removed successfully.")
                            break
                        else:
                            print(f"  ✗ Item '{item_id}' has NOT been removed.")
                            break
                    else:
                        break
                else:
                    raise ItemNotFoundError(item_id)
            except InvalidDataTypeError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except ItemNotFoundError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ Item '{item_id}' has NOT been removed.")
                print()
                break
            except ItemNotAvailableForOperationError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ Item '{item_id}' has NOT been removed.")
                print()
                break
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                print(f"  ✗ Item '{item_id}' has NOT been removed.")
                print()
                break
        print()

    def items_update_menu(self):
        print_menu_header("Updating an Item")
        while True:
            try:
                item_id = take_item_id()
                item = self.library.get_item(item_id)
                if item:
                    print(f"  Current item '{item_id}' info:")
                    print(item.display_info())
                    print()
                    
                    # Check if item is available (not borrowed)
                    if not item.available:
                        raise ItemNotAvailableForOperationError(item_id, "updated")
                    
                    print(f"  Are sure you want to update item '{item_id}'? ")
                    if insure_decision():
                        print("  Input the updated item data:")
                        new_item = create_item()
                        print()
                        if self.library.update_item(item, new_item):
                            print(f"  ✓ Item '{item_id}' has been updated successfully.")
                            break
                        else:
                            print(f"  ✗ Item '{item_id}' has NOT been updated.")
                            break
                    else:
                        break
                else:
                    raise ItemNotFoundError(item_id)
            except InvalidDataTypeError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except ItemNotFoundError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ Item '{item_id}' has NOT been updated.")
                print()
                break
            except ItemAlreadyExistsError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ Item '{item_id}' has NOT been updated.")
                print()
                break
            except ItemNotAvailableForOperationError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ Item '{item_id}' has NOT been updated.")
                print()
                break
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                print(f"  ✗ Item '{item_id}' has NOT been updated.")
                print()
                break
        print()

    # ===================== USER MANAGEMENT MENUS =====================
    # IMPORTANT
    def users_add_menu(self):
        print_menu_header("Adding a User")
        while True:
            try:
                user = create_user()
                if self.library.add_user(user):
                    print(f"  ✓ User '{user.first_name} {user.last_name}' has been added successfully.")
                    break
                else:
                    print(f"  ✗ User '{user.first_name} {user.last_name}' has NOT been added.")
                    break
            except InvalidDataTypeError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except UserAlreadyExistsError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ User '{user.first_name} {user.last_name}' has NOT been added.")
                print()
                break
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                print(f"  ✗ User '{user.first_name} {user.last_name}' has NOT been added.")
                print()
                break
        print()

    def users_remove_menu(self):
        print_menu_header("Removing a User")
        while True:
            try:
                user_id = take_user_id()
                user = self.library.get_user(user_id)
                if user:
                    print(f"  User '{user_id}' info:")
                    print(user.display_info())
                    print()
                    
                    # Check if user has borrowed items
                    if user.borrowed_items:
                        raise UserHasBorrowedItemsError(user_id, "removed", user.borrowed_items)
                    
                    print(f"  Are sure you want to remove user '{user_id}'? ")
                    if insure_decision():
                        if self.library.remove_user(user):
                            print(f"  ✓ User '{user_id}' has been removed successfully.")
                            break
                        else:
                            print(f"  ✗ User '{user_id}' has NOT been removed.")
                            break
                    else:
                        break
                else:
                    raise UserNotFoundError(user_id)
            except InvalidDataTypeError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except UserNotFoundError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ User '{user_id}' has NOT been removed.")
                print()
                break
            except UserHasBorrowedItemsError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ User '{user_id}' has NOT been removed.")
                print()
                break
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                print(f"  ✗ User '{user_id}' has NOT been removed.")
                print()
                break
        print()

    def users_update_menu(self):
        print_menu_header("Updating a User")
        while True:
            try:
                user_id = take_user_id()
                user = self.library.get_user(user_id)
                if user:
                    print(f"  Current user '{user_id}' info:")
                    print(user.display_info())
                    print()
                    
                    # Check if user has borrowed items
                    if user.borrowed_items:
                        raise UserHasBorrowedItemsError(user_id, "updated", user.borrowed_items)
                    
                    print(f"  Are sure you want to update user '{user_id}'? ")
                    if insure_decision():
                        print("  Input the updated user data:")
                        new_user = create_user()
                        print()
                        if self.library.update_user(user, new_user):
                            print(f"  ✓ User '{user_id}' has been updated successfully.")
                            break
                        else:
                            print(f"  ✗ User '{user_id}' has NOT been updated.")
                            break
                    else:
                        break
                else:
                    raise UserNotFoundError(user_id)
            except InvalidDataTypeError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except UserNotFoundError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ User '{user_id}' has NOT been updated.")
                print()
                break
            except UserAlreadyExistsError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ User '{user_id}' has NOT been updated.")
                print()
                break
            except UserHasBorrowedItemsError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ User '{user_id}' has NOT been updated.")
                print()
                break
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                print(f"  ✗ User '{user_id}' has NOT been updated.")
                print()
                break
        print()

    # ===================== USER VIEWING =====================
    # IMPORTANT
    def users_view_all(self):
        print_menu_header("  Viewing all library users...")
        print()
        if not self.library.users:
            print("  No users found in the library.")
            return
        for user in self.library.users:
            print(user.display_info())
            print()
        self.users_summary()
        print()
    
    # IMPORTANT
    def users_view_first_name(self):
        print_menu_header("Viewing users by first name")
        first_name = take_user_name("first name")
        print(f"  Viewing all users with first name: {first_name}...")
        print()
        found = False
        for user in self.library.users:
            if user.first_name.lower() == first_name.lower():
                found = True
                print(user.display_info())
        if not found:
            print(f"  No users found with first name: {first_name}")
        print()

    # IMPORTANT
    def users_view_last_name(self):
        print_menu_header("Viewing users by last name")
        last_name = take_user_name("last name")
        print(f"  Viewing all users with last name: {last_name}...")
        print()
        found = False
        for user in self.library.users:
            if user.last_name.lower() == last_name.lower():
                found = True
                print(user.display_info())
        if not found:
            print(f"  No users found with last name: {last_name}")
        print()

    # IMPORTANT
    def users_view_id(self):
        print_menu_header("Viewing users by first name")
        user_id = take_user_id()
        print(f"  Viewing the user with ID: {user_id}...")
        print()
        found = False
        for user in self.library.users:
            if user.id == user_id:
                found = True
                print(user.display_info())
        if not found:
            print(f"  No user found with ID: {user_id}")
        print()

    # IMPORTANT
    def users_view_options(self):
        while True:
            users_view_option = take_choice(5)
            match users_view_option:
                case 1:
                    self.users_view_all()
                    break
                case 2:
                    self.users_view_first_name()
                    break
                case 3:
                    self.users_view_last_name()
                    break
                case 4:
                    self.users_view_id()
                    break
                case 5:
                    return True
        return False

    # IMPORTANT
    def users_view_menu(self):
        while True:
            print_menu_header("Users Viewing Menu")
            print_menu_options([
                "1- View all users",
                "2- View by first name",
                "3- View by last name",
                "4- View by user ID",
                "5- Back",
            ])
            if self.users_view_options():
                break
            print()
        print()

    # ===================== MENU NAVIGATION =====================
    # IMPORTANT
    def items_options(self):
        while True:
            items_option = take_choice(5)

            match items_option:
                case 1:
                    self.items_view_menu()
                    break
                case 2:
                    self.items_add_menu()
                    break
                case 3:
                    self.items_remove_menu()
                    break
                case 4:
                    self.items_update_menu()
                    break
                case 5:
                    return True
        return False

    # IMPORTANT
    def items_menu(self):
        while True:
            print_menu_header("Items Menu")
            print_menu_options([
                "1- View items",
                "2- Add items",
                "3- Remove items",
                "4- Update items",
                "5- Back",
            ])
            if self.items_options():
                break
            print()
        print()

    # IMPORTANT
    def users_options(self):
        while True:
            users_option = take_choice(5)
            match users_option:
                case 1:
                    self.users_view_menu()
                    break
                case 2:
                    self.users_add_menu()
                    break
                case 3:
                    self.users_remove_menu()
                    break
                case 4:
                    self.users_update_menu()
                    break
                case 5:
                    return True
        return False

    # IMPORTANT
    def users_menu(self):
        while True:
            print_menu_header("Users Menu")
            print_menu_options([
                "1- View users",
                "2- Add users",
                "3- Remove users",
                "4- Update users",
                "5- Back",
            ])
            if self.users_options():
                break
            print()
        print()

    # IMPORTANT
    def borrow_item_menu(self):
        print_menu_header("Borrowing Menu")
        while True:
            try:
                item_id = take_item_id()
                item = self.library.get_item(item_id)
                if not item:
                    raise ItemNotFoundError(item_id)
                user_id = take_user_id()
                user = self.library.get_user(user_id)
                if not user:
                    raise UserNotFoundError(user_id)
                if self.library.borrow_item(user, item):
                    print(f"  ✓ User '{user_id}' has borrowed Item '{item_id}' successfully.")
                    break
                else:
                    print(f"  ✗ User '{user_id}' has NOT borrowed Item '{item_id}'.")
                    break
            except InvalidDataTypeError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}.")
                print()
                continue
            except ItemNotFoundError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ Item '{item_id}' has NOT been borrowed.")
                print()
                break
            except UserNotFoundError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ User '{user_id}' has NOT borrowed Item '{item_id}'.")
                print()
                break
            except ItemNotAvailableError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ User '{user_id}' has NOT borrowed Item '{item_id}'.")
                print()
                break
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                print(f"  ✗ User '{user_id}' has NOT borrowed Item '{item_id}'.")
                print()
                break
        print()

    # IMPORTANT
    def return_item_menu(self):
        print_menu_header("Returning Menu")
        while True:
            try:
                item_id = take_item_id()
                item = self.library.get_item(item_id)
                if not item:
                    raise ItemNotFoundError(item_id)
                user_id = take_user_id()
                user = self.library.get_user(user_id)
                if not user:
                    raise UserNotFoundError(user_id)
                if self.library.return_item(user, item):
                    print(f"  ✓ User '{user_id}' has returned Item '{item_id}' successfully.")
                    break
                else: 
                    print(f"  ✗ User '{user_id}' has NOT returned Item '{item_id}'.")
                    break
            except InvalidDataTypeError as e:
                print(f"  ✗ Error: {e}")
                print()
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}.")
                print()
                continue
            except ItemNotFoundError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ Item '{item_id}' has NOT been returned.")
                print()
                break
            except UserNotFoundError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ User '{user_id}' has NOT returned Item '{item_id}'.")
                print()
                break
            except ItemNotBorrowedError as e:
                print(f"  ✗ Error: {e}")
                print(f"  ✗ User '{user_id}' has NOT returned Item '{item_id}'.")
                print()
                break
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                print(f"  ✗ User '{user_id}' has NOT returned Item '{item_id}'.")
                print()
                break
        print()

    # IMPORTANT
    def borrow_return_options(self):
        while True:
            borrow_return_option = take_choice(3)
            match borrow_return_option:
                case 1:
                    self.borrow_item_menu()
                    break
                case 2:
                    self.return_item_menu()
                    break
                case 3:
                    return True
        return False

    # IMPORTANT
    def borrow_return_menu(self):
        while True:
            print_menu_header("Borrow/Return Menu")
            print_menu_options([
                "1- Borrow an Item",
                "2- Return an Item",
                "3- Back",
            ])
            if self.borrow_return_options():
                break
            print()
        print()

    # IMPORTANT
    def main_options(self):
        while True:
            main_option = take_choice(4)

            match main_option:
                case 1:
                    self.items_menu()
                    break
                case 2:
                    self.users_menu()
                    break
                case 3:
                    self.borrow_return_menu()
                    break
                case 4:
                    return True
        return False

    # IMPORTANT
    def main_menu(self):
        while True:
            print_menu_header("Main Menu")
            print_menu_options([
                "1- Items Menu",
                "2- Users Menu",
                "3- Borrow/Return Menu",
                "4- Save and Exit",
            ])
            if self.main_options():
                break
            print()
        print()

    # IMPORTANT
    def run(self):
        print("  Welcome to Library Management System (LMS)")
        print()
        self.main_menu()

        while True:
            try:
                self.library.save_data()
                print("  ✓ Library data saved successfully.")
                break
            except OSError as e:
                print(f"  ✗ Error saving library data: {e}")
                print("  Please check file permissions and try again.")
                retry = input("  Retry saving? (y/n): ").strip().lower()
                if retry not in ['y', 'yes']:
                    break
            except Exception as e:
                print(f"  ✗ Unexpected error while saving: {e}")
                print("  Please try again.")
                retry = input("  Retry saving? (y/n): ").strip().lower()
                if retry not in ['y', 'yes']:
                    break
        print("  Thank you for using LMS!")

# IMPORTANT
if __name__ == "__main__":
    main = Main()
    main.run()