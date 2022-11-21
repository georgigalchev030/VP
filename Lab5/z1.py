def input_nums(n):
    n = str(n)
    list_nums = []
    if n.isnumeric():
        n = int(n)
    else:
        return list_nums
    for i in range(n):
        list_element = input("Enter a list element: ")
        if list_element.isnumeric():
            list_nums.append(int(list_element))
    return list_nums


def sum_list(lst):
    result = 0
    for i in lst:
        if str(i).isdigit():
            result += int(i)
        elif str(i).replace('.', '', 1).isdigit():
            result += float(i)

    return result


def max_of_two(a, b):
    a = str(a)
    b = str(b)
    if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
        if float(a) >= float(b):
            return a
        return b
    if a.replace('.', '', 1).isdigit():
        return a
    if b.replace('.', '', 1).isdigit():
        return b
    return


num = input("Enter num: ")
print(input_nums(num))

num = int(input("Enter num: "))
list_nums = []
for i in range(num):
    list_nums.append(input())
print(sum_list(list_nums))

a = input("Enter a: ")
b = input("Enter b: ")
print(max_of_two(a, b))
print(max_of_two(sum_list(input_nums(4)), sum_list(input_nums(3))))