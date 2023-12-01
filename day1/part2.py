# This took me surprisingly long and was an immense headache due to the edge cases
import re

f = open("day1/input.txt")
data = f.read()
array = data.split("\n")

num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

split_dict = list(num_dict.items())

result = 0
arr = []
for each in array:
    str = ""
    
    for ran in range(len(each) + 1):
        for num1 in range(len(split_dict)):
            regcheck = re.search(split_dict[num1][0], each[:ran])
            regcheck1 = re.search(split_dict[num1][1], each[:ran])
            if regcheck or regcheck1:
                str += split_dict[num1][1]
                break
        if regcheck or regcheck1:
            break

    for ran in reversed(range(len(each))):
        for num1 in range(len(split_dict)):
            regcheck = re.search(split_dict[num1][0], each[ran:])
            regcheck1 = re.search(split_dict[num1][1], each[ran:])
            if regcheck or regcheck1:
                str += split_dict[num1][1]
                break
        if regcheck or regcheck1:
            break
    
    arr.append(str)
    result += int(str)

print(result)
