def digitize(num):
    if type(num) != int:
        return "Error"
    lst = []
    for i in str(num):
        lst.append(int(i))
    return tuple(lst)


a, b, c, d = digitize(1337)
print(a, b, c, d)
