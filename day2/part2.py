f = open("day2/input.txt")
data = f.read()
array = data.split('\n')

sum = 0
for each in array:
    game_id = int(each.split(":")[0].split(" ")[1])
    values = each.split(":")[1].replace(";",",").split(",")
    rgb = {"red":0, "green":0, "blue":0}
    for value in values:
        num, colour = value.strip().split(" ")
        num = int(num)
        rgb[colour] = max(rgb[colour],num)
    sum += rgb["green"] * rgb["red"]*rgb["blue"]

print(sum)