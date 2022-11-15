num = int(input("Enter range: ")) + 2
nums = [0,1]
for i in range(1, num):
    nums.append(nums[i-1]+nums[i])
print(nums)