from collections import Counter

array = open("day-7/input.txt").read().split("\n")
hands = {
    "five_kind": [],
    "four_kind": [],
    "full_house": [],
    "three_kind": [],
    "two_pair": [],
    "one_pair": [],
    "high_card": [],
}

for index, each in enumerate(array):
    array[index] = each.split()[0], int(each.split()[1])

# Sort cards by hand type
for each in array:
    count = Counter(each[0])
    sorted_count = count.most_common()

    if sorted_count[0][1] == 5:
        hands["five_kind"].append(each)
    elif sorted_count[0][1] == 4:
        hands["four_kind"].append(each)
    elif sorted_count[0][1] == 3 and sorted_count[1][1] == 2:
        hands["full_house"].append(each)
    elif sorted_count[0][1] == 3:
        hands["three_kind"].append(each)
    elif sorted_count[0][1] == 2 and sorted_count[1][1] == 2:
        hands["two_pair"].append(each)
    elif sorted_count[0][1] == 2:
        hands["one_pair"].append(each)
    else:
        hands["high_card"].append(each)


def my_sort_key(hand):
    order = "AKQJT98765432"
    return [order.index(rank) for rank in hand[0]]


for key in hands.keys():
    hands[key] = sorted(hands[key], key=my_sort_key)
ordered = [values for sublist in hands.values() for values in sublist]

ranked_list = list(enumerate(reversed(ordered), 1))
sum = 0
for each in ranked_list:
    sum += each[1][1] * each[0]
print(sum)
