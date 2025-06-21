from library import Library

class Main:
    def __init__(self):
        library = Library()
    
    def main_option(self):
        # FIXME: exeption handling for user's option
        main_option = int(input("Your Choice is: "))
        match main_option:
            case 1:
                self.items_menu()
            case 2:
                self.users_menu()
            case 3:
                self.borrow_return_menu()
            case 4:
                self.end()

    def main_menu(self):
        print("Main Menu")
        print("1- Items Menu")
        print("2- Users Menu")
        print("3- Borrow/Return Menu")
        print("4- Save and Exit")

    def run(self):
        print("Welcome to LMS")
        self.main_menu()