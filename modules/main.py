from library import Library

class Main:
    def __init__(self):
        library = Library()
    
    def main_menu(self):
        print("Main Menu")
        print("1- Items Menu")
        print("2- Users Menu")
        print("3- Borrow/Return Menu")
        print("4- Save and Exit")

    def run(self):
        print("Welcome to LMS")
        self.main_menu()