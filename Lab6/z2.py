class Person:
    def __init__(self, name, last_name, age,  nationality):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality

    def print(self):
        print(self.name, self.last_name, self.nationality)


class Student(Person):
    def __init__(self, name, last_name, age, nationality, university, yearofstudy):
        super().__init__(name, last_name, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def print(self):
        print(self.name, self.last_name, self.nationality, self.university, self.yearofstudy)


person1 = Person("Gosho", "Galchev", 35, "BG")
person2 = Person("Ivan", "Putkov", 34, "SB")
student1 = Student("Mira", "Plachkova", 18, "BG", "TU", 2028)
student2 = Student("Kalina", "Mitkova", 19, "SR", "UNSS", 2029)
person1.print()
person2.print()
student1.print()
student2.print()