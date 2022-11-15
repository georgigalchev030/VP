n = input("Enter num: ")
sum = 0
for i in range(1, int(n)+1):
    sum += int(n * i)
    if i == int(n):
        print(n*i, "=", sum)
        break
    print(n*i, end="+")
