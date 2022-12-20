import Calculator


a = float(input("a: "))
b = float(input("b: "))
sign = input("+ - * / ")
if sign == "+":
    print(Calculator.sumNums(a, b))
elif sign == "-":
    print(Calculator.subNums(a, b))
elif sign == "*":
    print(Calculator.multNums(a, b))
elif sign == "/":
    print(Calculator.devideNums(a, b))
else:
    print("Error")

