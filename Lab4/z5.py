s1 = {2, 3}
s2 = {1, 2, 3, 4}
if s1.issubset(s2):
    s2 = s2.difference(s1)
    print(s2)
else:
    s2.update(s1)
    print(s2)
s1 = {1, 7, 5}
s2 = {1, 2, 3, 4}
if s1.issubset(s2):
    s2 = s2.difference(s1)
    print(s2)
else:
    s2.update(s1)
    print(s2)

n = int(input("Enter num: "))
dic_kv = {}
for i in range(n):
    key = input("Key: ")
    value = input("Value: ")
    dic_kv[key] = value
n = int(input("Enter num: "))
list_k = []
for i in range(n):
    keys = input()
    if keys in dic_kv:
        list_k.append(dic_kv[keys])
        del dic_kv[keys]
    else:
        list_k.append(keys)

print(dic_kv)
print(list_k)