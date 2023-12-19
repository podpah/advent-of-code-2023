f = open("day-4/input.txt")
data = f.read()
array = data.split("\n")

sum = 0
for each in array:
    winning_nums, guesses = each.split(":")[1].split("|")
    winning_nums = [int(nums) for nums in winning_nums.strip().split()]  # List Comprehension
    guesses = [int(nums) for nums in guesses.strip().split()]  # List Comprehension

    score = 0
    for num in guesses:
        if num in winning_nums:
            score += 1
    num = 1 if score else 0
    for r in range(score - 1):
        num *= 2
    sum += num
print(sum)
