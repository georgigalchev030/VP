from entities import *
from errors import *


class Menu:

    def __init__(self):
        self.bank = Bank()

    def print_menu(self):
        print("1. Create a new user")
        print("2. Create a new account for existing user")
        print("3. Print all users")
        print("4. Print all accounts for existing user")
        print("5. Deposit for existing user account")
        print("6. Withdrawal for existing user account")
        print("7. Exit")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")
            try:
                if choice == "1":
                    name = input("Enter the user name (name - EGN): ").split(' - ')
                    self.bank.add_user(name[0], name[1])
                elif choice == "2":
                    print("Currency must be: BGN, EUR, USD or YPJ")
                    print("Account type must be: CURRENT, SAVINGS, CREDIT")
                    name = input("Enter the new account for the user (user - balance - currency - account type): ").split(" - ")
                    self.bank.add_account(name[0], name[1], name[2], name[3])
                elif choice == "3":
                    print(self.bank.print_users())
                elif choice == "4":
                    name = input("Enter the new account for the user (balance - currency - account type): ").split(" - ")
                elif choice == "5":
                    name = input("Enter how much you want to deposit (user egn - account - deposit): ").split(" - ")
                elif choice == "6":
                    name = input("Enter how much you want to withdrawal (user egn - account - withdrawal): ").split(" - ")
                elif choice == "5":
                    name = input("Enter the character you want to delete (character): ")
                elif choice == "7":
                    break
                else:
                    raise InvalidCommand("Invalid choice")


            except Exception as ex:
                print(f"Error: {str(ex)}")

            print()


if __name__ == '__main__':
    menu = Menu()
    menu.run()