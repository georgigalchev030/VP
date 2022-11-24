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


class Lecture(Person):
    def __init__(self, name, last_name, age, nationality, university, experience):
        super().__init__(name, last_name, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        print(self.name, self.last_name, self.nationality, self.university, self.experience)


person1 = Person("Gosho", "Galchev", 35, "BG")
person2 = Person("Ivan", "Putkov", 34, "SB")
student1 = Student("Mira", "Plachkova", 18, "BG", "TU", 2028)
student2 = Student("Kalina", "Mitkova", 19, "SR", "UNSS", 2029)
lecturer1 = Student("Mrs", "Zaharieva", 45, "BG", "TU", 20)
lecturer2 = Student("Mr", "Tutukov", 67, "EN", "NB", 29)

person1.print()
person2.print()
student1.print()
student2.print()
lecturer1.print()
lecturer2.print()