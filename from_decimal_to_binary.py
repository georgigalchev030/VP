decimal_num=int(input("Enter decimal number: "))
type = input("binary or hexadecimal: ")
result = []
divider = 2
a = 0
isTrue = True
if type == "binary":
    while isTrue:
        if decimal_num % 2 == 0:
            a = 0
            result.insert(0,a)
            if decimal_num == 0:
                isTrue = False
            decimal_num //= 2
        else:
            a = 1
            result.insert(0,a)
            if decimal_num == 0:
                isTrue = False
            decimal_num //= 2
    for i in range(len(result)):
        if result[i] == 1:
            break
        result.pop(i)
elif type == "hexadecimal":
    while isTrue:
        remainder = decimal_num % 16
        if remainder == 10:
            a = "A"
            result.insert(0, a)
            if decimal_num == 0:
                isTrue = False
            decimal_num //= 16
        elif remainder == 11:
            a = "B"
            result.insert(0, a)
            if decimal_num == 0:
                isTrue = False
            decimal_num //= 16
        elif remainder == 12:
            a = "C"
            result.insert(0, a)
            if decimal_num == 0:
                isTrue = False
            decimal_num //= 16
        elif remainder == 13:
            a = "D"
            result.insert(0, a)
            if decimal_num == 0:
                isTrue = False
            decimal_num //= 16
        elif remainder == 14:
            a = "E"
            result.insert(0, a)
            if decimal_num == 0:
                isTrue = False
            decimal_num //= 16
        elif remainder == 15:
            a = "F"
            result.insert(0, a)
            if decimal_num == 0:
                isTrue = False
            decimal_num //= 16
        else:
            result.insert(0,remainder)
            if decimal_num == 0:
                isTrue = False
            decimal_num //= 16
    for i in range(len(result)):
        if result[i] != 0:
            break
        result.pop(i)
result = [str(num) for num in result]
print(f'Binary: {"".join(result)}')
