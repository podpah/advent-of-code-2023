f = open("day6/input.txt")
data = f.read()

time, distance = [int(line.split(":")[1].replace(" ","")) for line in data.split("\n")]

sum = 0
for wait in range(time + 1):
    distance_travelled = (time-wait)*wait
    if distance_travelled > distance:
        sum += 1

print(sum)