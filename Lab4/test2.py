keys = input("Enter 3 keys: ").split()
values = input("Enter 3 values: ").split()
dic = {}
for i in range(3):
    if values[i].isnumeric():
        values[i] = int(values[i])
    dic[keys[i]] = values[i]
print(dic)