from library import Library
from book import Book
from dvd import DVD
from magazine import Magazine
from user import User
from exceptions import (
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
)
import json
import os

# IMPORTANT
def print_menu_header(title: str) -> None:
    """Print a formatted menu header."""
    print()
    separator = "=" * 40
    print(separator)
    print(title.center(len(separator)))
    print(separator)

# IMPORTANT
def print_menu_options(options: list[str]) -> None:
    """Print menu options using a consistent style."""
    for option in options:
        print(f"  {option}")


def insure_decision():
    while True:
        try:
            decision = input("  Yes or No? ").strip()
            if decision in {"yes", "y"}:
                return True            
            elif decision in {"no", "n"}:
                return False
            else:
                raise InvalidValueError("Your decision must be 'yes' or 'no'.")
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue

# IMPORTANT
def validate_choice(choice, expected_type, num_options):
    if not isinstance(choice, expected_type):
        raise InvalidDataTypeError("integer", type(choice).__name__)
    if choice <= 0 or choice > num_options:
        raise InvalidValueError("Your choice should be a number from the menu")

# IMPORTANT    
def validate_type(kind):
    if not isinstance(kind, str):
        raise InvalidDataTypeError("string", type(kind).__name__)
    if kind not in ["Book", "DVD", "Magazine"]:
        raise InvalidValueError("Item type must be 'Book', 'DVD', or 'Magazine'.")

# IMPORTANT
def validate_author(author):
    if not isinstance(author, str):
        raise InvalidDataTypeError("string", type(author).__name__)
    if len(author.strip()) < 2:
        raise InvalidValueError("Author's name must be a non-empty string with at least two characters.")

# IMPORTANT
def validate_title(title):
    if not isinstance(title, str):
        raise InvalidDataTypeError("string", type(title).__name__)
    if not title:
        raise InvalidValueError("Title's name must be a non-empty string.")
    
# IMPORTANT
def validate_available(available):
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
    if not year.isdigit():
        raise InvalidDataTypeError("integer", type(year).__name__)
    year = int(year)
    if year <= 0:
        raise InvalidValueError("Year must be a positive non-zero integer.")
    return year

# IMPORTANT
def validate_genre(genre):
    if not isinstance(genre, str):
        raise InvalidDataTypeError("string", type(genre).__name__)
    if not genre:
        raise InvalidValueError("Genre must be a non-empty string.")

# IMPORTANT
def validate_duration(duration):
    if not duration.isdigit():
        raise InvalidDataTypeError("integer", type(duration).__name__)
    duration = int(duration)
    if duration <= 0:
        raise InvalidValueError("Duration must be a positive non-zero integer.")
    return duration

# IMPORTANT
def validate_item_id(item_id):
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
    if len(aa) != 2 or not aa.isalpha() or not aa.isupper():
        raise InvalidItemIDFormatError(item_id)
    # YYYY: 4 digits
    if len(yyyy) != 4 or not yyyy.isdigit():
        raise InvalidItemIDFormatError(item_id)
    # N: positive integer
    if not n.isdigit() or int(n) <= 0:
        raise InvalidItemIDFormatError(item_id)

# IMPORTANT
def validate_user_name(name, kind):
    if not isinstance(name, str):
        raise InvalidDataTypeError("string", type(name).__name__)
    if len(name.strip()) < 2:
        raise InvalidValueError(f"User's {kind} must be a non-empty string with at least two characters.")

# IMPORTANT
def validate_user_id(user_id):
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
    while True:
        try:
            choice = int(input("  Enter choice: "))
            validate_choice(choice, int, num_options) # Raises InvalidDataTypeError
            return choice
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue

# IMPORTANT
def take_type():
    while True:
        try:
            kind = input("  Enter the item's type (Book/DVD/Magazine): ").strip()
            validate_type(kind)
            return kind
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue

# IMPORTANT
def take_author():
    while True:
        try:
            author = input("  Enter the item's author: ").strip()
            validate_author(author)
            return author
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue

# IMPORTANT
def take_title():
    while True:
        try:
            title = input("  Enter the item's title: ").strip()
            validate_title(title)
            return title
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue

# IMPORTANT
def take_available():
    while True:
        try:
            available = input("  Is the item available? ").strip()
            return validate_available(available)
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue

# IMPORTANT
def take_item_id():
    while True:
        try:
            item_id = input("  Enter the item's ID: ").strip()
            validate_item_id(item_id)
            return item_id
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue
        except InvalidItemIDFormatError as e:
            print(f"  ✗ Invalid input: {e}")
            continue

# IMPORTANT
def take_year():
    while True:
        try:
            year = input("  Enter the item's publish year: ").strip()
            year = validate_year(year)
            return year
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue

# IMPORTANT
def take_genre():
    while True:
        try:
            genre = input("  Enter the item's genre: ").strip()
            genre = validate_genre(genre)
            return genre
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue

# IMPORTANT
def take_duration():
    while True:
        try:
            duration = input("  Enter DVD duration in minutes: ").strip()
            duration = validate_duration(duration)
            return duration
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue

# IMPORTANT
def get_item_data():
    type = take_type()
    title = take_title()
    author = take_author()
    year = take_year()
    available = take_available()
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
            validate_user_name(user_name, kind)
            return user_name
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue

# IMPORTANT
def take_user_id():
    while True:
        try:
            user_id = input("  Enter the uaer's ID: ").strip()
            validate_user_id(user_id)
            return user_id
        except InvalidDataTypeError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue
        except InvalidValueError as e:
            print(f"  ✗ Invalid input: {e}.")
            continue
        except InvalidUserIDFormatError as e:
            print(f"  ✗ Invalid input: {e}")
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
    def __init__(self):
        try:
            self.library = Library()
            self.group_by_type()
        except FileNotFoundError:
            print("Warning: Data files not found. Starting with empty library.")
            self.library = Library()
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except MissingFieldError as e:
            print(f"Error: Missing required field in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except InvalidDataTypeError as e:
            print(f"Error: Invalid data type in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except InvalidValueError as e:
            print(f"Error: Invalid value in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except ItemNotFoundError as e:
            print(f"Error: Item not found in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except ItemAlreadyExistsError as e:
            print(f"Error: Duplicate item in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except UserAlreadyExistsError as e:
            print(f"Error: Duplicate user in data files: {e}")
            print("Starting with empty library.")
            self.library = Library()
        except Exception as e:
            print(f"Error loading library data: {e}")
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
        else:
            self.display_info(self.books)
            
        print("📀 DVDS")
        if not self.dvds:
            print("  No dvds to display.")
        else:
            self.display_info(self.dvds)

        print("📰 MAGAZINES")
        if not self.magazines:
            print("  No magazines to display.")
        else:
            self.display_info(self.magazines)

        self.items_summary(self.books, self.dvds, self.magazines)

    # IMPORTANT
    def items_view_type(self):
        type = take_type()
        print(f"  Viewing all items of type: {type}...")
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

    # IMPORTANT
    def items_view_title(self):
        title = take_title()
        print(f"  Viewing all items of title: {title}...")
        found = False
        for item in self.library.items:
            if item.title.lower() == title.lower():
                print(item.display_info())
                found = True
        if not found:
            print(f"  No items found with title: {title}")
    
    # IMPORTANT
    def items_view_author(self):
        author = take_author()        
        print(f"  Viewing all items of author: {author}...")
        found = False
        for item in self.library.items:
            if item.author.lower() == author.lower():
                print(item.display_info())
                found = True
        if not found:
            print(f"  No items found by author: {author}")
    
    # IMPORTANT
    def items_view_id(self):
        item_id = take_item_id()
        print(f"  Viewing the item with ID: {item_id}...")
        found = False
        for item in self.library.items:
            if item.id == item_id:
                print(item.display_info())
                found = True
        if not found:
            print(f"  No item found with ID: {item_id}")

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
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}")
                continue
            except ItemAlreadyExistsError as e:
                print(f"  ✗ Error: {e}")
                continue
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                continue
        print()

    # IMPORTANT
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
                    print(f"  Are sure you wnat to remove item '{item_id}'? ")
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
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}")
                continue
            except ItemNotFoundError as e:
                print(f"  ✗ Error: {e}")
                continue
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                continue
        print()

    # IMPORTANT
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
                    print(f"  Are sure you wnat to update item '{item_id}'? ")
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
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}")
                continue
            except ItemNotFoundError as e:
                print(f"  ✗ Error: {e}")
                continue
            except ItemAlreadyExistsError as e:
                print(f"  ✗ Error: {e}")
                continue
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                continue
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
                    print(f"  ✓ User '{user.first_name} {user.last_name}' has NOT been added.")
                    break
            except InvalidDataTypeError as e:
                print(f"  ✗ Error: {e}")
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}")
                continue
            except UserAlreadyExistsError as e:
                print(f"  ✗ Error: {e}")
                continue
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                continue
        print()

    # IMPORTANT
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
                    print(f"  Are sure you wnat to remove user '{user_id}'? ")
                    if insure_decision():
                        if self.library.remove_user(user):
                            print(f"  ✓ User '{user_id}' has been removed successfully.")
                            break
                        else:
                            print(f"  ✓ User '{user_id}' has NOT been removed.")
                            break
                    else:
                        break
                else:
                    raise UserNotFoundError(user_id)
            except InvalidDataTypeError as e:
                print(f"  ✗ Error: {e}")
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}")
                continue
            except UserNotFoundError as e:
                print(f"  ✗ Error: {e}")
                continue
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                continue
        print()

    # IMPORTANT
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
                    print(f"  Are sure you wnat to update user '{user_id}'? ")
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
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}")
                continue
            except UserNotFoundError as e:
                print(f"  ✗ Error: {e}")
                continue
            except UserAlreadyExistsError as e:
                print(f"  ✗ Error: {e}")
                continue
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                continue
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
        self.users_summary()
    
    # IMPORTANT
    def users_view_first_name(self):
        first_name = take_user_name("first name")
        print(f"  Viewing all users with first name: {first_name}...")
        found = False
        for user in self.library.users:
            if user.first_name.lower() == first_name.lower():
                found = True
                print(user.display_info())
        if not found:
            print(f"  No users found with first name: {first_name}")

    # IMPORTANT
    def users_view_last_name(self):
        last_name = take_user_name("last name")
        print(f"  Viewing all users with last name: {last_name}...")
        found = False
        for user in self.library.users:
            if user.last_name.lower() == last_name.lower():
                found = True
                print(user.display_info())
        if not found:
            print(f"  No users found with last name: {last_name}")

    # IMPORTANT
    def users_view_id(self):
        user_id = take_user_id()
        print(f"  Viewing the user with ID: {user_id}...")
        found = False
        for user in self.library.users:
            if user.id == user_id:
                found = True
                print(user.display_info())
        if not found:
            print(f"  No user found with ID: {user_id}")

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
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}.")
                continue
            except ItemNotFoundError as e:
                print(f"  ✗ Error: {e}")
                continue
            except UserNotFoundError as e:
                print(f"  ✗ Error: {e}")
                continue
            except ItemNotAvailableError as e:
                print(f"  ✗ Error: {e}")
                continue
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                continue
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
                continue
            except InvalidValueError as e:
                print(f"  ✗ Error: {e}.")
                continue
            except ItemNotFoundError as e:
                print(f"  ✗ Error: {e}")
                continue
            except UserNotFoundError as e:
                print(f"  ✗ Error: {e}")
                continue
            except ItemNotBorrowedError as e:
                print(f"  ✗ Error: {e}")
                continue
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                continue
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
                    # FIXME: to be checked
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
                    # FIXME: to be checked
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
        # while True:
        #     try:
        #         self.library.save_data()
        #         print("  ✓ Library data saved successfully.")
        #         break
        #     except IOError as e:
        #         print(f"  ✗ Error saving library data: {e}")
        #         print("  Please check file permissions and try again.")
        #         retry = input("  Retry saving? (y/n): ").strip().lower()
        #         if retry not in ['y', 'yes']:
        #             break
        #     except OSError as e:
        #         print(f"  ✗ Error creating directories: {e}")
        #         print("  Please check directory permissions and try again.")
        #         retry = input("  Retry saving? (y/n): ").strip().lower()
        #         if retry not in ['y', 'yes']:
        #             break
        #     except Exception as e:
        #         print(f"  ✗ Unexpected error while saving: {e}")
        #         print("  Please try again.")
        #         retry = input("  Retry saving? (y/n): ").strip().lower()
        #         if retry not in ['y', 'yes']:
        #             break
        print("  Thank you for using LMS!")

# IMPORTANT
if __name__ == "__main__":
    main = Main()
    main.run()