import re

f = open("day1/input.txt")
data = f.read()
array = data.split("\n")

num_dict = {
    "one": "o1ne",
    "two": "t2wo",
    "three": "t3hree",
    "four": "f4our",
    "five": "f5ive",
    "six": "s6ix",
    "seven": "s7even",
    "eight": "e8ight",
    "nine": "n9ine",
}
split_dict = list(num_dict.items())

arra = []
result = 0
for each in array:
    for num in range(len(split_dict)):
        each = re.sub(split_dict[num][0], split_dict[num][1], each)

    nums = "".join(letter for letter in each if letter.isdigit())
    str = nums[0]
    str += nums[len(nums) - 1]
    arra.append(str)
    result += int(str)
