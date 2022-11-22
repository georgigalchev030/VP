def list_avg(lst, multiplier="1"):
    multiplier = str(multiplier)
    lst = [str(s) for s in lst]
    if multiplier == "":
        multiplier = "1"
    if not multiplier.isnumeric():
        return "Error"
    multiplier = int(multiplier)
    result = 0
    i = 0
    for i, v in enumerate(lst):
        if v.isdigit():
            result += int(v) * multiplier
    return result / (i+1)


n = int(input("Enter n: "))
nums = []
for i in range(n):
    nums.append(input("Enter list num: "))
mult = input("Enter multiplier: ")
print(list_avg(nums, mult))
print(list_avg([2, 4, 21, 5, "3", "e"]))
print(list_avg([2, 4, 21, 5, "3", "e"], 2))
