import random


class InvalidParameterError(Exception):
    def __int__(self, expression, message):
        self.expression = expression
        self.message = "Invalid class parameter: name"


class InvalidAgeError(InvalidParameterError):
    def __init__(self, age):
        super().__init__(age)
        self.message = "Invalid parameter: age"

    def __str__(self):
        return f'{num} {name} {age} {sound} Invalid parameter: age'


class InvaliSoundError(InvalidParameterError):
    def __init__(self, sound, message="Invalid parameter: sound"):
        super().__init__(sound, message)

    def __str__(self):
        return f'{num} {name} {age} {sound} Invalid parameter: sound'


class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
        if type(name) != str:
            raise InvalidParameterError(name)
        if type(age) != int:
            raise InvalidAgeError(age)
        if type(sound) != str:
            raise InvaliSoundError(sound)

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    def print(self):
        pass

    def daily_task(self, *args):
        pass


class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 15:
            raise InvalidAgeError(age)
        if sound.count('r') <= 2:
            raise InvaliSoundError(sound)

    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals):
        for i, animal in enumerate(animals):
            if isinstance(animal, Lemur) or isinstance(animal, Human):
                class_name = animal.__class__.__name__
                print(f"{self.name} the Jaguar hunted down {animal.name} the {class_name}")
                del animals[i]


class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError(age)
        if 'e' not in sound:
            raise InvaliSoundError(sound)

    def print(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")

    def daily_task(self, count_food):
        if count_food >= 10:
            count_food -= 10
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            return count_food
        elif count_food > 0:
            print(f"{self.name} the Lemur could only find {count_food} fruits")
            count_food = 0
            return count_food
        else:
            super().make_sound()
            super().make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
            return 0


class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError(age)
        if 'e' not in sound:
            raise InvaliSoundError(sound)

    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})" )

    def daily_task(self, animals, buildings):
        isTrue = False
        for i, animal in enumerate(animals):
            if isinstance(animal, Human) and animal.name == self.name:
                if i != len(animals) - 1 and i != 0:
                    if isinstance(animals[i-1], Human) and isinstance(animals[i+1], Human):
                        isTrue = True
                elif i == 0:
                    if isinstance(animals[i+1], Human):
                        isTrue = True
                elif i == len(animals) - 1:
                    if isinstance(animals[i - 1], Human):
                        isTrue = True

                if isTrue:
                    building = Building("Sgrada")
                    buildings.append(building)


class Building:
    def __init__(self, type_building):
        self.type_building = type_building


fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]


for i in range(102):
    num = random.randint(0, 9)
    name = names[random.randrange(len(names))]
    age = random.randint(7, 20)
    sound = sounds[random.randrange(len(sounds))]
    try:
        if 0<=num<=3:
            animals.append(Lemur(name, age, sound))
        elif 4<=num<=7:
            animals.append(Jaguar(name, age, sound))
        elif 8<=num<=9:
            animals.append(Human(name, age, sound))
    except InvalidAgeError as ex:
        print(ex)
    except InvaliSoundError as ex:
        print(ex)


print(f"The jungle now has {len(animals)} animals")


for anim in animals:
    if isinstance(anim, Lemur):
        fruits = anim.daily_task(fruits)
    if isinstance(anim, Jaguar):
        anim.daily_task(animals)
    if isinstance(anim, Human):
        anim.daily_task(animals, buildings)


print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)


