from functools import reduce
from math import lcm #lowest common multiple
f = open("day8/input.txt")
data = f.read()
array = data.split("\n")

sequence, values = array[0].replace("L","0").replace("R","1"), array[2:]
vals = {}
for each in values:
    id, left_right = each.split(" = ")
    vals[id] = [value.strip() for value in (left_right[1:-1].split(","))]
ids = [id for id in vals.keys() if id[-1] == "A"]

totals = []
for index, current_id in enumerate(ids):
    steps = 0
    while current_id[-1] != "Z":
        for each in sequence:
            current_id = vals[current_id][int(each)]
            steps += 1
    ids[index] = current_id
    totals.append(steps)

print(reduce(lcm,totals))