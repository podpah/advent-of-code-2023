f = open("day6/input.txt")
data = f.read()

times, distances = [line.split(":")[1].split() for line in data.split("\n")]
both = zip(times, distances)

total = 1
for each in both:
    sum = 0
    duration = int(each[0])
    distance = int(each[1])

    for wait in range(duration + 1):
        distance_travelled = (duration - wait) * wait
        if distance_travelled > distance:
            sum += 1
    total *= sum
print(total)
