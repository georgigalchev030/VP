class InvalidParameterError(Exception):
    def __int__(self, expression):
        self.expression = expression

    def __str__(self):
        return f'Nums is not float'


class NutrientError(Exception):
    def __int__(self, expression):
        self.expression = expression

    def __str__(self):
        return f'Nums must be under 100'


class InvalidFoodError(Exception):
    def __int__(self, expression):
        self.expression = expression

    def __str__(self):
        return f'Num must be over 0'


class Food:
    def __init__(self, carbs, protein, fats, salt):
        self.carbs = carbs
        self.protein = protein
        self.fats = fats
        self.salt = salt
        self.name = __class__.__name__

    def print_info(self):
        print(self.name, f"{self.carbs}, {self.protein}, {self.fats}, {self.salt}")


for x in range(0, 120, 10):
    x = float(x)
    food = Food(1+x, 4+x, 2+x, 4+x)
    element_in_food = [1+x, 4+x, 2+x, 4+x]
    try:
        if type(x) != float:
            raise InvalidParameterError
        if max(element_in_food) > 100:
            raise NutrientError
        if sum(element_in_food) == 0:
            raise InvalidFoodError
    except InvalidParameterError as ex:
        print(ex)
    except NutrientError as ex:
        print(ex)
    except InvalidFoodError as ex:
        print(ex)
    else:
        food.print_info()



