f = open("day-1/input.txt")
data = f.read()
array = data.split("\n")

result = 0
for each in array:
    nums = "".join(letter for letter in each if letter.isdigit())
    str = nums[0]
    str += nums[len(nums) - 1]
    result += int(str)
print(result)
