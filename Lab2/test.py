a = bin(int(input()))
bit = int(input())
print(a)
if a[-(bit+1)] == 0:
    print("True")
else:
    print("False")