def change_nums(list_nums, num):
    for i, v in enumerate(list_nums):
        if num > v:
            list_nums[i] = 0
    return list_nums


counter = int(input("Enter how many nums you want in the list: "))
list_nums = []
print("Enter the nums:")
for i in range(counter):
    n = int(input())
    list_nums.append(n)
num = int(input("Enter change num: "))
print(change_nums(list_nums, num))