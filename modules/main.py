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
)
import json


def print_menu_header(title: str) -> None:
    """Print a formatted menu header."""
    print()
    separator = "=" * 40
    print(separator)
    print(title.center(len(separator)))
    print(separator)


def print_menu_options(options: list[str]) -> None:
    """Print menu options using a consistent style."""
    for option in options:
        print(f"  {option}")


def parse_bool_input(prompt: str) -> bool:
    """Prompt the user for a boolean value until a valid entry is provided."""
    while True:
        value = input(f"  {prompt}: ").strip().lower()
        if value in {"true", "t", "yes", "y", "1"}:
            return True
        if value in {"false", "f", "no", "n", "0"}:
            return False
        print("  Please enter 'yes' or 'no'.")

class Main:
    def __init__(self):
        # FIXME: Handle data loading exceptions
        try:
            self.library = Library()
            # load_data()
                # __load_items()
                    # __create_item(item)
                        # InvalidDataTypeError
                        # MissingFieldError 
                        # InvalidValueError 

                    # add_item(item_obj)
                        # ItemAlreadyExistsError 

                # __load_users() 
                    # InvalidDataTypeError
                    # MissingFieldError 
                    # InvalidValueError  
                    # ItemNotFoundError 
        except FileNotFoundError:
            print("Warning: Data files not found. Starting with empty library.")
            self.library = Library()
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in data files: {e}")
            self.library = Library()
        except Exception as e:
            print(f"Error loading library data: {e}")
            self.library = Library()
    
    def items_summary(self, books, dvds, magazines):
        print("  SUMMARY:")
        print(f"    Books: {len(books)}")
        print(f"    Magazines: {len(magazines)}")
        print(f"    DVDs: {len(dvds)}")
        print(f"    Total: {len(self.library.items)}")
        
    def users_summary(self):
        print("  USERS SUMMARY:")
        print(f"    Total Users: {len(self.library.users)}")
        
    def users_view_all(self):
        print("  Viewing all library users")
        if not self.library.users:
            print("  No users found in the library.")
            return
        for user in self.library.users:
            print(user.display_info())
        self.users_summary()
    
    def view_all_books(self, books):
        for book in books:
            print(book.display_info())
    
    def view_all_dvds(self, dvds):
        for dvd in dvds:
            print(dvd.display_info())
    
    def view_all_magazines(self, magazines):
        for magazine in magazines:
            print(magazine.display_info())
            
    def group_by_type(self):
        books = []
        dvds = []
        magazines = []
        for item in self.library.items:
            if isinstance(item, Book):
                books.append(item)
            elif isinstance(item, DVD):
                dvds.append(item)
            elif isinstance(item, Magazine):
                magazines.append(item)
        return books, dvds, magazines

    def items_view_all(self):
        print("  Viewing all library items")
        if not self.library.items:
            print("  No items found in the library.")
            return
        books, dvds, magazines = self.group_by_type()
        self.view_all_books(books)
        self.view_all_dvds(dvds)
        self.view_all_magazines(magazines)
        self.items_summary(books, dvds, magazines)

    def items_view_type(self):
        # FIXME: exception handling for user's input (Book, DVD, Magazine)
        while True:
            type = input("  View all items of type (Book/DVD/Magazine): ").strip()
            if type not in ["Book", "DVD", "Magazine"]:
                print("  Invalid item type. Please enter Book, DVD, or Magazine.")
                continue
            break
        
        found = False
        match type:
            case "Book":
                print("📚 BOOKS")
                for item in self.library.items:
                    if isinstance(item, Book):
                        print(item.display_info())
                        found = True
            case "DVD":
                print("📀 DVDS")
                for item in self.library.items:
                    if isinstance(item, DVD):
                        print(item.display_info())
                        found = True
            case "Magazine":
                print("📰 MAGAZINES")
                for item in self.library.items:
                    if isinstance(item, Magazine):
                        print(item.display_info())
                        found = True
        if not found:
            print(f"  No items found of type: {type}")
                        
    def items_view_author(self):
        # FIXME: exception handling for user's input (author's format)
        author = input("  View all items of author: ").strip()
        if not author:
            print("  Error: Author name cannot be empty.")
            return
        
        found = False
        for item in self.library.items:
            if item.author.lower() == author.lower():
                print(item.display_info())
                found = True
        if not found:
            print(f"  No items found by author: {author}")

    def items_view_title(self):
        # FIXME: exception handling for user's input (title's format)
        title = input("  View all items of title: ").strip()
        if not title:
            print("  Error: Title cannot be empty.")
            return
        
        found = False
        for item in self.library.items:
            if item.title.lower() == title.lower():
                print(item.display_info())
                found = True
        if not found:
            print(f"  No items found with title: {title}")

    def items_view_id(self):
        # FIXME: exception handling for user's input (id's format)
        item_id = input("  View item with ID: ").strip()
        if not item_id:
            print("  Error: Item ID cannot be empty.")
            return
        
        found = False
        for item in self.library.items:
            if item.id == item_id:
                print(item.display_info())
                found = True
        if not found:
            print(f"  No item found with ID: {item_id}")

    def items_view_options(self):
        while True:
            try:
                items_view_option = int(input("  Enter choice: "))
            except ValueError:
                print("  ✗ Invalid input. Please enter a number.")
                continue
            finally:
                pass

            match items_view_option:
                case 1:
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
                    break  # TODO: BACK
                case _:
                    print("  ✗ Invalid choice. Please try again.")

    def items_view_menu(self):
        print_menu_header("Items Viewing Menu")
        print_menu_options([
            "1- View all items",
            "2- View by type",
            "3- View by author",
            "4- View by title",
            "5- View by Item ID",
            "6- Back",
        ])
        self.items_view_options()
        print()

    def get_item_data(self):
        while True:
            try:
                type = input("  Item type (Book/DVD/Magazine): ").strip()
                if type not in ["Book", "DVD", "Magazine"]:
                    raise InvalidValueError("Type must be: [Book or DVD or Magazine]")
                break

            except InvalidValueError as value:
                print(f"  Error: {value}")
                continue
            
        while True:
            try:
                title = input(f"  {type} title: ").strip()
                if not title:
                    raise InvalidValueError("Title must be a non-empty string")
                break

            except InvalidValueError as value:
                print(f"  Error: {value}")
                continue
    
        while True:
            try:
                author = input(f"  {type} author: ").strip()
                if not author or len(author) < 2:
                    raise InvalidValueError("Author's name must be a non-empty string with at least two characters.")
                break
            
            except InvalidValueError as value:
                print(f"  Error: {value}")
                continue
        
        while True:
            try:
                year = int(input(f"  {type} publish year: "))
                if year <= 0:
                    raise InvalidValueError("Year must be a positive non-zero integer")
                break
            
            except InvalidValueError as value:
                print(f"  Error: {value}")
                continue
        
        return type, title, author, year

    def create_item(self):
        type, title, author, year = self.get_item_data()
        # FIXME: ensure exception handled in parse_bool_input
        available = parse_bool_input(f"{type} available (True/False or Yes/No)")
        match type:
            case "Book":
                while True:
                    try:
                        genre = input(f"  {type} genre: ").strip()
                        if not genre:
                            raise InvalidValueError("Genre must be a non-empty string")
                        item = Book(title, author, year, available, genre)
                        break

                    except InvalidValueError as value:
                        print(f"  Error: {value}")
                        continue

            case "DVD":
                while True:
                    try:
                        duration = int(input(f"  {type} duration in minutes: "))
                        if duration <= 0:
                            raise InvalidValueError("Duration must be a positive non-zero integer")
                        item = DVD(title, author, year, available, duration)
                        break

                    except ValueError:
                        print("  Duration must be a number. Please try again.")
                        continue
                    except InvalidValueError as value:
                        print(f"  Error: {value}")
                        continue


            case "Magazine":
                while True:
                    try:
                        genre = input(f"  {type} genre: ").strip()
                        if not genre:
                            raise InvalidValueError("Genre must be a non-empty string")
                        item = Magazine(title, author, year, available, genre)
                        break
                    except InvalidValueError as value:
                        print(f"  Error: {value}")
                        continue
        return item
            
    def items_add_menu(self):
        print_menu_header("Adding an Item")
        item = self.create_item()
        try:
            if self.library.add_item(item):
                print(f"  ✓ Item '{item.title}' has been added successfully.")
            else:
                print(f"  ✗ Item '{item.title}' has NOT been added.")
        except ItemAlreadyExistsError as exists:
            print(f"  ✗ Error: {exists}")
        except InvalidDataTypeError as data_type:
            print(f"  ✗ Error: {data_type}")
        except InvalidValueError as value:
            print(f"  ✗ Error: {value}")
        except Exception as e:
            print(f"  ✗ Unexpected error: {e}")
        print()

    def get_item(self, item_id):
        if not item_id or not item_id.strip():
            print("  ✗ Error: Item ID cannot be empty.")
            return None
        
        item_id = item_id.strip()
        for item in self.library.items:
            if item.id == item_id:
                return item
        return None

    def items_remove_menu(self):
        print_menu_header("Removing an Item")
        while True:
            try:
                item_id = input("  Item ID: ").strip()
                if not item_id:
                    raise InvalidValueError("ID must be a non-empty string")
                break

            except InvalidValueError as value:
                print(f"  ✗ Error: {value}")
                continue
            
        try:    
            item = self.get_item(item_id)
            if item:
                if self.library.remove_item(item):
                    print(f"  ✓ Item '{item_id}' has been removed successfully.")
                else:
                    print(f"  ✗ Item '{item_id}' has NOT been removed.")
            else:
                print(f"  ✗ No item found with ID: {item_id}")
        except ItemNotFoundError as not_found:
            print(f"  ✗ Error: {not_found}")
        except InvalidDataTypeError as data_type:
            print(f"  ✗ Error: {data_type}")
        except Exception as e:
            print(f"  ✗ Unexpected error: {e}")
        print()

    def items_update_menu(self):
        # FIXME: Add comprehensive exception handling for all library operations
        print_menu_header("Updating an Item")
        try:
            item_id = input("  Item ID: ").strip()
            if not item_id:
                print("  ✗ Error: Item ID cannot be empty.")
                return
            
            item = self.get_item(item_id)
            if item:
                print(f"  Current item '{item_id}' info:")
                print(item.display_info())
                print("  Input the updated item data:")
                new_item = self.create_item()
                if new_item is None:
                    print("  ✗ Item creation failed.")
                    return
                
                self.library.update_item(item, new_item)
                print(f"  ✓ Item '{item_id}' has been updated successfully.")
            else:
                print(f"  ✗ No item found with ID: {item_id}")
        except ItemNotFoundError as e:
            print(f"  ✗ Error: {e}")
        except ItemAlreadyExistsError as e:
            print(f"  ✗ Error: {e}")
        except InvalidDataTypeError as e:
            print(f"  ✗ Error: {e}")
        except InvalidValueError as e:
            print(f"  ✗ Error: {e}")
        except Exception as e:
            print(f"  ✗ Unexpected error: {e}")
        print()

    def get_user(self, user_id):
        # FIXME: exception handling for user's input (id's format)
        if not user_id or not user_id.strip():
            print("  ✗ Error: User ID cannot be empty.")
            return None
        
        user_id = user_id.strip()
        for user in self.library.users:
            if user.id == user_id:
                return user
        return None

    def get_user_data(self):
        # FIXME: exception handling for user's input
        user_id = input("  User ID: ").strip()
        if not user_id:
            print("  ✗ Error: User ID cannot be empty.")
            return None, None, None
        
        first_name = input("  First name: ").strip()
        if not first_name:
            print("  ✗ Error: First name cannot be empty.")
            return None, None, None
        
        last_name = input("  Last name: ").strip()
        if not last_name:
            print("  ✗ Error: Last name cannot be empty.")
            return None, None, None
        
        return user_id, first_name, last_name

    def create_user(self):
        # FIXME: Add validation for user creation
        try:
            user_id, first_name, last_name = self.get_user_data()
            if user_id is None:
                return None
            
            return User(first_name, last_name, user_id)
        except InvalidDataTypeError as e:
            print(f"  ✗ Error: {e}")
            return None
        except InvalidValueError as e:
            print(f"  ✗ Error: {e}")
            return None
        except Exception as e:
            print(f"  ✗ Unexpected error creating user: {e}")
            return None

    def users_add_menu(self):
        # FIXME: Add comprehensive exception handling for all library operations
        print_menu_header("Adding a User")
        try:
            user = self.create_user()
            if user is None:
                print("  ✗ User creation failed.")
                return
            
            self.library.add_user(user)
            print(f"  ✓ User '{user.first_name} {user.last_name}' has been added successfully.")
        except UserAlreadyExistsError as e:
            print(f"  ✗ Error: {e}")
        except InvalidDataTypeError as e:
            print(f"  ✗ Error: {e}")
        except InvalidValueError as e:
            print(f"  ✗ Error: {e}")
        except Exception as e:
            print(f"  ✗ Unexpected error: {e}")
        print()

    def users_remove_menu(self):
        # FIXME: Add comprehensive exception handling for all library operations
        print_menu_header("Removing a User")
        try:
            user_id = input("  User ID: ").strip()
            if not user_id:
                print("  ✗ Error: User ID cannot be empty.")
                return
            
            user = self.get_user(user_id)
            if user:
                self.library.remove_user(user)
                print(f"  ✓ User '{user_id}' has been removed successfully.")
            else:
                print(f"  ✗ No user found with ID: {user_id}")
        except UserNotFoundError as e:
            print(f"  ✗ Error: {e}")
        except InvalidDataTypeError as e:
            print(f"  ✗ Error: {e}")
        except Exception as e:
            print(f"  ✗ Unexpected error: {e}")
        print()

    def users_update_menu(self):
        # FIXME: Add comprehensive exception handling for all library operations
        print_menu_header("Updating a User")
        try:
            user_id = input("  User ID: ").strip()
            if not user_id:
                print("  ✗ Error: User ID cannot be empty.")
                return
            
            user = self.get_user(user_id)
            if user:
                print(f"  Current user '{user_id}' info:")
                print(user.display_info())
                print("  Input the updated user data:")
                new_user = self.create_user()
                if new_user is None:
                    print("  ✗ User creation failed.")
                    return
                
                self.library.update_user(user, new_user)
                print(f"  ✓ User '{user_id}' has been updated successfully.")
            else:
                print(f"  ✗ No user found with ID: {user_id}")
        except UserNotFoundError as e:
            print(f"  ✗ Error: {e}")
        except UserAlreadyExistsError as e:
            print(f"  ✗ Error: {e}")
        except InvalidDataTypeError as e:
            print(f"  ✗ Error: {e}")
        except InvalidValueError as e:
            print(f"  ✗ Error: {e}")
        except Exception as e:
            print(f"  ✗ Unexpected error: {e}")
        print()

    def users_view_first_name(self):
        # FIXME: exception handling for user's input (first name's format)
        first_name = input("  View all users with first name: ").strip()
        if not first_name:
            print("  ✗ Error: First name cannot be empty.")
            return
        
        found = False
        for user in self.library.users:
            if user.first_name.lower() == first_name.lower():
                print(user.display_info())
                found = True
        if not found:
            print(f"  No users found with first name: {first_name}")

    def users_view_last_name(self):
        # FIXME: exception handling for user's input (last name's format)
        last_name = input("  View all users with last name: ").strip()
        if not last_name:
            print("  ✗ Error: Last name cannot be empty.")
            return
        
        found = False
        for user in self.library.users:
            if user.last_name.lower() == last_name.lower():
                print(user.display_info())
                found = True
        if not found:
            print(f"  No users found with last name: {last_name}")

    def users_view_id(self):
        # FIXME: exception handling for user's input (id's format)
        user_id = input("  View user with ID: ").strip()
        if not user_id:
            print("  ✗ Error: User ID cannot be empty.")
            return
        
        found = False
        for user in self.library.users:
            if user.id == user_id:
                print(user.display_info())
                found = True
        if not found:
            print(f"  No user found with ID: {user_id}")

    def users_view_options(self):
        while True:
            try:
                users_view_option = int(input("  Enter choice: "))
            except ValueError:
                print("  ✗ Invalid input. Please enter a number.")
                continue
            finally:
                pass

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
                    break  # TODO: BACK
                case _:
                    print("  ✗ Invalid choice. Please try again.")

    def users_view_menu(self):
        print_menu_header("Users Viewing Menu")
        print_menu_options([
            "1- View all users",
            "2- View by first name",
            "3- View by last name",
            "4- View by user ID",
            "5- Back",
        ])
        self.users_view_options()
        print()

    def items_options(self):
        while True:
            try:
                items_option = int(input("  Enter choice: "))
            except ValueError:
                print("  ✗ Invalid input. Please enter a number.")
                continue
            finally:
                pass

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
                case _:
                    print("  ✗ Invalid choice. Please try again.")
        return False

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

    def users_options(self):
        while True:
            try:
                users_option = int(input("  Enter choice: "))
            except ValueError:
                print("  ✗ Invalid input. Please enter a number.")
                continue
            finally:
                pass

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
                case _:
                    print("  ✗ Invalid choice. Please try again.")
        return False

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

    def borrow_item_menu(self):
        # FIXME: Add comprehensive exception handling for all library operations
        print_menu_header("Borrowing Menu")
        try:
            item_id = input("  Item ID: ").strip()
            if not item_id:
                print("  ✗ Error: Item ID cannot be empty.")
                return
            
            item = self.get_item(item_id)
            if not item:
                print(f"  ✗ No item found with ID: {item_id}")
                return
            
            user_id = input("  User ID: ").strip()
            if not user_id:
                print("  ✗ Error: User ID cannot be empty.")
                return
            
            user = self.get_user(user_id)
            if not user:
                print(f"  ✗ No user found with ID: {user_id}")
                return

            self.library.borrow_item(user, item)
            print(f"  ✓ User '{user_id}' borrowed Item '{item_id}' successfully")
        except ItemNotAvailableError as e:
            print(f"  ✗ Error: {e}")
        except ItemNotFoundError as e:
            print(f"  ✗ Error: {e}")
        except UserNotFoundError as e:
            print(f"  ✗ Error: {e}")
        except InvalidDataTypeError as e:
            print(f"  ✗ Error: {e}")
        except Exception as e:
            print(f"  ✗ Unexpected error: {e}")
        finally:
            print("  Returning to Borrow/Return menu...")
        print()

    def return_item_menu(self):
        # FIXME: Add comprehensive exception handling for all library operations
        print_menu_header("Returning Menu")
        try:
            item_id = input("  Item ID: ").strip()
            if not item_id:
                print("  ✗ Error: Item ID cannot be empty.")
                return
            
            item = self.get_item(item_id)
            if not item:
                print(f"  ✗ No item found with ID: {item_id}")
                return
            
            user_id = input("  User ID: ").strip()
            if not user_id:
                print("  ✗ Error: User ID cannot be empty.")
                return
            
            user = self.get_user(user_id)
            if not user:
                print(f"  ✗ No user found with ID: {user_id}")
                return
            
            self.library.return_item(user, item)
            print(f"  ✓ User '{user_id}' returned Item '{item_id}' successfully")
        except ItemNotFoundError as e:
            print(f"  ✗ Error: {e}")
        except UserNotFoundError as e:
            print(f"  ✗ Error: {e}")
        except InvalidDataTypeError as e:
            print(f"  ✗ Error: {e}")
        except Exception as e:
            print(f"  ✗ Unexpected error: {e}")
        print()

    def borrow_return_options(self):
        while True:
            try:
                borrow_return_option = int(input("  Enter choice: "))
            except ValueError:
                print("  ✗ Invalid input. Please enter a number.")
                continue
            finally:
                pass

            match borrow_return_option:
                case 1:
                    self.borrow_item_menu()
                    break
                case 2:
                    self.return_item_menu()
                    break
                case 3:
                    return True
                case _:
                    print("  ✗ Invalid choice. Please try again.")
        return False

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

    def main_options(self):
        while True:
            try:
                main_option = int(input("  Enter choice: "))
            except ValueError:
                print("  ✗ Invalid input. Please enter a number.")
                continue
            finally:
                pass

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
                case _:
                    print("  ✗ Invalid choice. Please try again.")
        return False

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

    def run(self):
        print("  Welcome to Library Management System (LMS)")
        print()
        self.main_menu()
        # TODO: Add graceful handling for data saving
        try:
            self.library.save_data()
            print("  ✓ Library data saved successfully.")
        except IOError as e:
            print(f"  ✗ Error saving library data: {e}")
        except Exception as e:
            print(f"  ✗ Unexpected error while saving: {e}")
        print("  Thank you for using LMS!")

if __name__ == "__main__":
    main = Main()
    main.run()