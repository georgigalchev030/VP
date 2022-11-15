n = int(input("Enter how many nums you want to enter: "))
list_nums = []
for i in range(n):
    list_nums.append(int(input()))
zero_or_one = int(input("Enter 0/1: "))
if zero_or_one == 0:
    for i in range(len(list_nums)):
        if i % 2 == 0:
            list_nums[i] += 5
elif zero_or_one == 1:
    for i in range(len(list_nums)):
        if i % 2 == 1:
            list_nums[i] += 10
print(list_nums)