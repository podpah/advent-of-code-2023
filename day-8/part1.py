f = open("day-8/input.txt")
data = f.read()
array = data.split("\n")

sequence, values = array[0].replace("L", "0").replace("R", "1"), array[2:]
steps = 0
current_id = "AAA"
vals = {}
for each in values:
    id, left_right = each.split(" = ")
    vals[id] = [value.strip() for value in (left_right[1:-1].split(","))]

while current_id != "ZZZ":
    for each in sequence:
        current_id = vals[current_id][int(each)]
        steps += 1
print(steps)
