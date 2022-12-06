dic_test = {"Gosho": 3, "Ivan": 32, "Sasho": 23}
try:
    f = dic_test["Petar"]
except KeyError as ex:
    print(ex, "Key not found")

try:
    x = 102
    x.append(6)
except AttributeError as ex:
    print(ex, "Not possible doing this operation")

try:
    i = int(input("Enter integer: "))
except ValueError as ex:
    print(ex)

try:
    x = 56
    print(q)
except NameError as ex:
    print(ex)

try:
    i = 5
    text_ex = "Gosho"
    result = i + text_ex
except TypeError as ex:
    print(ex)

try:
    list_ex = [12, 32, "d", "eds"]
    i = list_ex[6]
except IndexError as ex:
    print(ex)

try:
    import maht
except ModuleNotFoundError as ex:
    print(ex)

try:
    i = 5
    print(i / 0)
except ZeroDivisionError as ex:
    print(ex, "error")

try:
    f = open("tex.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("We don't find the file")
else:
    f.close()


import os


try:
    file_path = 'demo.txt'
    fileDescriptor = os.open(file_path, os.O_RDWR)
    os.close(fileDescriptor)
except os.error:
    print("Error in file:", file_path)
