def list_nums(a):
    result = 0
    for i in a:
        if type(i) == int:
            result += i
    return result


def input_nums(x):
    lst = []
    for i in range(x):
        lst.append(int(input("Input num: ")))
    return lst


print("Sum:", list_nums(input_nums(5)))

