import math


try:
    x = int(input("Enter num: "))
    if x < 0:
        raise ValueError
    print(math.sqrt(x))
except ValueError:
    print("Invalid Number")
finally:
    print("Good Bye")