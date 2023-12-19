f = open("day-6/input.txt")
data = f.read()

time, distance = [int(line.split(":")[1].replace(" ", "")) for line in data.split("\n")]

start, end = 0, 0
for wait in range(time + 1):
    distance_travelled = (time - wait) * wait
    if distance_travelled > distance:
        start = wait
        break

for wait in reversed(range(time + 1)):
    distance_travelled = (time - wait) * wait
    if distance_travelled > distance:
        end = wait
        break

print(end - start + 1)
