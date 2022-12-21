from entities import *
from errors import *


class Menu:
    all_chars = {}

    def print_menu(self):
        print("1. Create a new character")
        print("2. Create a new weapon for existing character")
        print("3. Create a new item for existing character")
        print("4. Print all characters")
        print("5. Delete character")
        print("6. Exit")

    def command_create_character(self, name, sex, ch_class, weapon=None, item=None):
        if weapon!=None or item!=None:
            raise InvalidCharacterClass("weapon and item must be None for the moment")
        self.all_chars[name] = {"sex": sex, "ch_class": ch_class, "weapon": {"type": weapon, "attack": 0}, "item": {"type": item}, "durability": 100}

    def command_add_weapon(self, name, weapon, attack):
        self.all_chars[name]["weapon"]["type"] = weapon
        self.all_chars[name]["weapon"]["attack"] = attack

    def command_add_item(self,name, item, durability):
        self.all_chars[name]["item"]["type"] = item
        self.all_chars[name]["item"]["durability"] = durability

    def run(self):
        # infinite menu loop
        while True:
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")
            try:
                if choice == "1":
                    print("Class must be: Warrior, Mage, Piest or Rogue")
                    name = input("Enter the character name (alpha-numeric - sex - class): ").split(' - ')
                    if len(name) != 3:
                        raise InvalidDataFormat("Must be tree words")
                    for i, v in enumerate(name):
                        if i > 0:
                            if any(map(str.isdigit, v)):
                                raise InvalidDataFormat("Must not containing digits")
                elif choice == "2":
                    name = input("Enter the new weapon for the character (character - weapon - attackPoints): ").split(" - ")
                    if len(name) != 3:
                        raise InvalidDataFormat("Must be tree words")
                    for i, v in enumerate(name):
                        if i != 2:
                            if any(map(str.isdigit, v)):
                                raise InvalidDataFormat("Must not containing digits")
                elif choice == "3":
                    name = input("Enter the new item for the character (character - item - durability): ").split(" - ")
                    if len(name) != 3:
                        raise InvalidDataFormat("Must be tree words")
                    for i, v in enumerate(name):
                        if i != 2:
                            if any(map(str.isdigit, v)):
                                raise InvalidDataFormat("Must not containing digits")
                elif choice == "4":
                    print(self.all_chars)
                elif choice == "5":
                    name = input("Enter the character you want to delete (character): ")
                elif choice == "6":
                    break
                else:
                    raise InvalidCommand("Invalid choice")

                if type(name) != list and len(name) < 4:
                    raise InvalidDataFormat("Word must be over 4 char")
                elif type(name) == list:
                    for n in name:
                        if len(n) < 4:
                            raise InvalidDataFormat("Words must be over 4 char")

                if choice == "1" and name[0] in self.all_chars:
                    raise CharacterExists("Name exist")

                if choice != "1" and name[0] not in self.all_chars:
                    raise CharacterNotFound("Didn't find the name")
                    # char = self.command_create_character(....)

                if choice == "1":
                    self.command_create_character(name[0], name[1], name[2])
                elif choice == "2":
                    self.command_add_weapon(name[0], name[1], int(name[2]))
                elif choice == "3":
                    self.command_add_item(name[0], name[1], int(name[2]))
                elif choice == "5":
                    del self.all_chars[name]

            except Exception as ex:
                print(f"Error: {str(ex)}")

            print()


if __name__ == '__main__':
    menu = Menu()
    menu.run()