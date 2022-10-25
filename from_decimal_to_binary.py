decimal_num=int(input("Enter decimal number: "))
result = []
divider = 2
a = 0
isTrue = True
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
result = [str(num) for num in result]
print(f'Binary: {"".join(result)}')
