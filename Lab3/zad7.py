num = int(input("Enter num: "))
counter = 0
for i in range(1, num):
    if num % i == 0:
        counter+=1
if counter==1:
    print("Prosto")
else:
    print("Slojno")