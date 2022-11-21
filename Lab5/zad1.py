def square(x):
    return x**2


def triangle(a, ha):
    return a*ha/2


def rec_triangle(a, b):
    return a*b/2


type_figure = input("Enter figure: ")
if type_figure == "square":
    print(square(int(input("Enter x: "))))
elif type_figure == "triangle":
    a = int(input("Enter a: "))
    ha = int(input("Enter ha: "))
    print(triangle(a, ha))
elif type_figure == "rec triangle":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(rec_triangle(a, b))

