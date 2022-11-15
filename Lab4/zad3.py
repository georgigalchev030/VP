text = input("Enter text: ")
text_dic = {}
for i in text:
    if i not in text_dic:
        text_dic[i] = 1
    else:
        text_dic[i] += 1

for k, v in text_dic.items():
    print(f"{k}:{v}", end=" ")
    