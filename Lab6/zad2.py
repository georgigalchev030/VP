import random


class Animal:
    def __init__(self, name, age, type_food):
        self.name = name
        self.age = age
        self.type_food = type_food
        self.count = 0

    def make_sound(self):
        pass

    def eat_food(self, capacity):
        pass


class Cat(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("Meow!")

    def eat_food(self, capacity):
        if capacity == 0 and self.count == 0:
            [self.make_sound() for _ in range(4)]
            return capacity
        self.count += 1
        result = capacity - 10
        if result < 0:
            self.make_sound()
            self.make_sound()
            return 0
        return result


class Dog(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("Bal-bal!")

    def eat_food(self, capacity, eat_quantity=5):
        result = capacity - eat_quantity
        if result >= 0:
            return result
        return 0


class Duck(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("Kvak-kvak!")

    def eat_food(self, capacity):
        self.make_sound()
        result = capacity - random.randrange(1, 9)
        if result >= 0:
            return result
        return 0


class Horse(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("Hrr-hrr!")

    def eat_food(self, capacity):
        if capacity > 30:
            result = capacity - 15
        else:
            result = capacity - 8
        if result < 0:
            return 0
        return result


animal1 = Cat("Goshko", 3, "riba")
animal2 = Dog("Valio", 2, "dog_food")
animal3 = Duck("Patio", 5, "patio_hrana")
animal4 = Horse("Mimi", 1, "konska_hrana")
animal5 = Duck("Svetlio", 2, "patio_hrana")
animal6 = Horse("Morki", 7, "konska_hrana")
animal7 = Cat("Momo", 5, "riba")
animal8 = Dog("Chari", 9, "dog_food")
animal9 = Cat("Beluga", 1, "riba")
animal10 = Duck("Patio", 5, "patio_hrana")
list_animals = [animal1, animal2, animal3, animal4, animal5, animal6, animal7, animal8, animal9, animal10]
dic_food = {"dog_food":455, "riba":299, "patio_hrana": 219, "konska_hrana": 250}
for _ in range(10):
    print("=======")
    for i in range(len(list_animals)):
        class_name = list_animals[i].__class__.__name__
        name_animal = list_animals[i].name
        food = list_animals[i].type_food
        left_food = list_animals[i].eat_food(dic_food[food])
        print(f"{name_animal} the {class_name} just ate {dic_food[food]-left_food} {food}, "
              f"there's {left_food} left")
        dic_food[food] = left_food
