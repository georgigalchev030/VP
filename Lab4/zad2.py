import random

numbers, range_num = eval(input("How many random numbers and range (,): "))
counter = 0
list_random_nums = []
for i in range(numbers):
    list_random_nums.append(random.randrange(range_num))
print(list_random_nums)
length = len(list_random_nums)-1
for i in range(length):
    list_random_nums.insert(counter+1, list_random_nums[counter]+list_random_nums[counter+1])
    counter += 2
print(list_random_nums)