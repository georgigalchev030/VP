import math

n = int(input("How many numbers: "))
result = -math.inf
while n < 0:
    print("Enter num above 0")
    n = int(input("Enter: "))
for i in range(n):
    num = int(input(f"Enter num {i+1}: "))
    if num > result:
        result = num
print(f"Max num: {result}")


