decimal_num=int(input("Enter decimal number: "))
type = input("binary or hexadecimal: ")
result = []
a = 0
isTrue = True
if type == "binary":
    while True:
        if decimal_num % 2 == 0:
            a = 0
            if decimal_num == 0:
                break
            result.insert(0, a)
        else:
            a = 1
            if decimal_num == 0:
                break
            result.insert(0, a)
        decimal_num //= 2
    for i in range(len(result)):
        if result[i] == 1:
            break
        result.pop(i)
elif type == "hexadecimal":
    while True:
        remainder = decimal_num % 16
        if decimal_num == 0:
            break
        if remainder == 10:
            a = "A"
            result.insert(0, a)
        elif remainder == 11:
            a = "B"
            result.insert(0, a)
        elif remainder == 12:
            a = "C"
            result.insert(0, a)
        elif remainder == 13:
            a = "D"
            result.insert(0, a)
        elif remainder == 14:
            a = "E"
            result.insert(0, a)
        elif remainder == 15:
            a = "F"
            result.insert(0, a)
        else:
            result.insert(0,remainder)
        decimal_num //= 16
    for i in range(len(result)):
        if result[i] != 0:
            break
        result.pop(i)
result = [str(num) for num in result]
print(f'{type}: {"".join(result)}')
