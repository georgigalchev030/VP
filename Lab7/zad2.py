try:
    f = open("text.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("We don't find the file")
else:
    f.close()
