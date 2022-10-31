import math

r = float(input("Enter r: "))
perimeter = 2*math.pi*r
area = math.pi*r**2
print(f"Perimeter: {round(perimeter, 3)}")
print(f"Area: {round(area, 3)}")