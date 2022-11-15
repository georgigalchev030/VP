num = int(input("Enter num: "))
dic_num = {}
for i in range(1, num+1):
    dic_num[i] = (num+1)-i
print(dic_num)