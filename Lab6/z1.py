class Person:
    def __init__(self, name, last_name, age,  nationality):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality

    def print(self):
        print(self.name, self.last_name, self.nationality)


person1 = Person("Gosho", "Galchev", 35, "BG")
person2 = Person("Ivan", "Putkov", 34, "SB")
person3 = Person("Mira", "Plachkova", 12, "EN")
person1.print()
person2.print()
person3.print()