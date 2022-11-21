def sum_nums(a, b):
    return a+b


def subtract_nums(a, b):
    return a-b


def mult_nums(a, b):
    return a*b


def divide_nums(a, b):
    return a/b


print("Enter operator: + - * /")
operation_type = input()
a, b = eval(input("Enter two inters (a,b): "))
if operation_type == "+":
    print(sum_nums(a, b))
elif operation_type == "-":
    print(subtract_nums(a, b))
elif operation_type == "*":
    print(mult_nums(a, b))
elif operation_type == "/":
    print(divide_nums(a, b))