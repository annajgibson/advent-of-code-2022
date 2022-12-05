"""
Advent of Code 2022
Day 03
"""
from collections import Counter
from string import ascii_letters

with open('input.txt', 'r') as file:
    rucksacks = file.read()

# part 1

priorities = dict(zip([letter for letter in ascii_letters], [n for n in range(1, 53)]))
rucksack_list = [sack for sack in rucksacks.split('\n') if sack != '']

total_priorities = 0
for each_sack in rucksack_list:
    print(each_sack)
    compartment_1_count = Counter(each_sack[:round(len(each_sack)/2)])
    compartment_2_count = Counter(each_sack[round(len(each_sack)/2):])
    # check if any shared characters by getting intersection
    for item in compartment_1_count:
        if item in compartment_2_count.keys():
            total_priorities += priorities[item[0]]

# part 2

start = 0
end = 3
increment = 3
three_sack_priorities = 0

for selection in range(round(len(rucksack_list)/3)):
    three_sacks = rucksack_list[start:end]
    sack_1 = Counter(three_sacks[0])
    sack_2 = Counter(three_sacks[1])
    sack_3 = Counter(three_sacks[2])
    # check if any shared characters by getting intersection
    for item in sack_1:
        if item in sack_2.keys():
            if item in sack_3.keys():
                three_sack_priorities += priorities[item[0]]
    start += increment
    end += increment
