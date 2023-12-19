f = open("day-15/input.txt")
data = f.read()
array = data.split(",")

sum = 0
for each in array:
    current = 0
    for letter in each:
        current = (current + ord(letter)) * 17 % 256
    sum += current

print(sum)