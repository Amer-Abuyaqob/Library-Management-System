from library import Library
from book import Book
from modules.dvd import DVD
from modules.magazine import Magazine
from modules.user import User

class Main:
    def __init__(self):
        self.library = Library()
    
    def items_summary(self, books, dvds, magazines):
        print("SUMMARY:")
        print(f"   Books: {len(books)}")
        print(f"   Magazines: {len(magazines)}")
        print(f"   DVDs: {len(dvds)}")
        print(f"   Total: {len(self.library.items)}")
        
    def users_summary(self):
        print("USERS SUMMARY:")
        print(f"   Total Users: {len(self.library.users)}")
        
    def users_view_all(self):
        print("Viewing all library users")
        if not self.library.users:
            print("No users found in the library.")
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
        print("Viewing all library items")
        if not self.library.items:
            print("No items found in the library.")
            return
        books, dvds, magazines = self.group_by_type()
        self.view_all_books(books)
        self.view_all_dvds(dvds)
        self.view_all_magazines(magazines)
        self.items_summary(books, dvds, magazines)

    def items_view_type(self):
        # FIXME: exeption handling for user's input (Book, DVD, Magazine)
        type = input("View all items of type: ")
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
            print(f"No items found of type: {type}")
                        
    def items_view_author(self):
        # FIXME: exeption handling for user's input (author's format)
        author = input("View all items of author: ")
        found = False
        for item in self.library.items:
            if item.author == author:
                print(item.display_info())
                found = True
        if not found:
            print(f"No items found by author: {author}")

    def items_view_title(self):
        # FIXME: exeption handling for user's input (title's format)
        title = input("View all items of title: ")
        found = False
        for item in self.library.items:
            if item.title == title:
                print(item.display_info())
                found = True
        if not found:
            print(f"No items found with title: {title}")

    def items_view_id(self):
        # FIXME: exeption handling for user's input (id's format)
        id = input("View all item of id: ")
        found = False
        for item in self.library.items:
            if item.id == id:
                print(item.display_info())
                found = True
        if not found:
            print(f"No item found with ID: {id}")

    def items_view_options(self):
        # FIXME: exeption handling for user's option
        items_view_option = int(input("Your Choice is: "))
        match items_view_option:
            case 1:
                self.items_view_all()
            case 2:
                self.items_view_type()
            case 3:
                self.items_view_author()
            case 4:
                self.items_view_title()
            case 5:
                self.items_view_id()
            case 6:
                pass # TODO: BACK

    def items_view_menu(self):
        print("Items Viewing Menu")
        print("1- View all items")
        print("2- View by type")
        print("3- View by author")
        print("4- View by title")
        print("5- View by item_id")
        print("6- Back")
        self.items_view_options()

    def items_options(self):
        # FIXME: exeption handling for user's option
        items_option = int(input("Your Choice is: "))
        match items_option:
            case 1:
                self.items_view_menu()
            case 2:
                pass # TODO: self.items_add_menu()
            case 3:
                pass # TODO: self.items_remove_menu()
            case 4:
                pass # TODO: self.items_update_menu()
            case 5:
                pass # TODO: BACK

    def items_menu(self):
        print("Items Menu")
        print("1- View items")
        print("2- Add items")
        print("3- Remove items")
        print("4- Update items")
        print("5- Back")
        self.items_options()

    def users_view_first_name(self):
        # FIXME: exeption handling for user's input (first name's format)
        first_name = input("View all users with first name: ")
        found = False
        for user in self.library.users:
            if user.first_name == first_name:
                print(user.display_info())
                found = True
        if not found:
            print(f"No users found with first name: {first_name}")

    def users_view_last_name(self):
        # FIXME: exeption handling for user's input (last name's format)
        last_name = input("View all users with last name: ")
        found = False
        for user in self.library.users:
            if user.last_name == last_name:
                print(user.display_info())
                found = True
        if not found:
            print(f"No users found with last name: {last_name}")

    def users_view_id(self):
        # FIXME: exeption handling for user's input (id's format)
        user_id = input("View user with ID: ")
        found = False
        for user in self.library.users:
            if user.id == user_id:
                print(user.display_info())
                found = True
        if not found:
            print(f"No user found with ID: {user_id}")

    def users_view_options(self):
        # FIXME: exeption handling for user's option
        users_view_option = int(input("Your Choice is: "))
        match users_view_option:
            case 1:
                self.users_view_all()
            case 2:
                self.users_view_first_name()
            case 3:
                self.users_view_last_name()
            case 4:
                self.users_view_id()
            case 5:
                pass # TODO: BACK

    def users_view_menu(self):
        print("Users Viewing Menu")
        print("1- View all users")
        print("2- View by first name")
        print("3- View by last name")
        print("4- View by user ID")
        print("5- Back")
        self.users_view_options()

    def users_options(self):
        # FIXME: exeption handling for user's option
        users_option = int(input("Your Choice is: "))
        match users_option:
            case 1:
                self.users_view_menu()
            case 2:
                pass # TODO: self.users_add_menu()
            case 3:
                pass # TODO: self.users_remove_menu()
            case 4:
                pass # TODO: self.users_update_menu()
            case 5:
                pass # TODO: BACK

    def users_menu(self):
        print("Users Menu")
        print("1- View users")
        print("2- Add users")
        print("3- Remove users")
        print("4- Update users")
        print("5- Back")
        self.users_options()

    def main_options(self):
        # FIXME: exeption handling for user's option
        main_option = int(input("Your Choice is: "))
        match main_option:
            case 1:
                self.items_menu()
            case 2:
                self.users_menu()
            case 3:
                pass # TODO: self.borrow_return_menu()
            case 4:
                pass # TODO: self.end()

    def main_menu(self):
        print("Main Menu")
        print("1- Items Menu")
        print("2- Users Menu")
        print("3- Borrow/Return Menu")
        print("4- Save and Exit")
        self.main_options()

    def run(self):
        print("Welcome to LMS")
        self.main_menu()