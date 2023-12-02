f = open("day2/input.txt")
data = f.read()
array = data.split('\n')

# This took me so long to do because I was checking games that would've been impossible instead
sum = 0
for each in array:
    game_id = int(each.split(":")[0].split(" ")[1])
    sum += game_id
    values = each.split(":")[1].replace(";",",").split(",")
    for value in values:
        num, colour = value.strip().split(" ")
        num = int(num)
        if (colour == "red" and num > 12) or (colour == "green" and num > 13) or (colour == "blue" and num > 14):
            sum -= game_id
            break

print(sum)