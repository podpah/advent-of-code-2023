f = open("day4/input.txt")
data = f.read()
array = data.split('\n')

sum = 0
for each in array:
    card, values = each.split(":")
    card_id = card[5:]

    winning_nums, guesses = values.split("|")
    winning_nums = [int(nums) for nums in winning_nums.strip().replace("  ", " ").split(" ")] # List Comprehension
    guesses = [int(nums) for nums in guesses.strip().replace("  ", " ").split(" ") ] # List Comprehension

    score = 0
    for num in guesses:
        if num in winning_nums:
            score += 1
    num = 1 if score else 0
    for r in range(score-1):
        num *= 2
    sum += num
print(sum)