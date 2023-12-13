f = open("day4/input.txt")
data = f.read()
array = data.split("\n")

sum = 0
objs = []
for index, each in enumerate(array):
    winning_nums, guesses = each.split(":")[1].split("|")
    winning_nums = [int(nums) for nums in winning_nums.strip().split()]  # List Comprehension
    guesses = [int(nums) for nums in guesses.strip().split()]  # List Comprehension
    objs.append({"id": index, "winning_nums": winning_nums, "guesses": guesses, "amount": 1})

for each in objs:
    sum += each["amount"]
    score = 0
    for num in each["guesses"]:
        if num in each["winning_nums"]:
            score += 1

    for r in range(score):
        objs[each["id"] + r + 1]["amount"] += each["amount"]

print(sum)
