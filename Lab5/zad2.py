def polindrom(n):
    if n == n[::-1]:
        return 1
    else:
        return 0


num = input("Enter num: ")
if num.isnumeric():
    print(polindrom(num))
else:
    print("Enter valid num")