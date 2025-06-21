from library import Library

class Main:
    def __init__(self):
        library = Library()
    
    def items_view_all(self):
        print("Viewing all library items")
        # TODO: self.view_all_books()
        # TODO: self.view_all_dvds()
        # TODO: self.view_all_magazines()

    def items_view_options(self):
        # FIXME: exeption handling for user's option
        items_view_option = int(input("Your Choice is: "))
        match items_view_option:
            case 1:
                self.items_view_all()
            case 2:
                pass # TODO: self.items_view_type()
            case 3:
                pass # TODO: self.items_view_author()
            case 4:
                pass # TODO: self.items_view_title()
            case 5:
                pass # TODO: self.items_view_id()
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

    def main_options(self):
        # FIXME: exeption handling for user's option
        main_option = int(input("Your Choice is: "))
        match main_option:
            case 1:
                self.items_menu()
            case 2:
                pass # TODO: self.users_menu()
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