"""
Advent of Code 2022
Day 01
"""


def get_most_calories(data, number):
    # empty dict to store values
    elves_cals_dict = dict()
    # get number of elves
    elves = data.split('\n\n')
    # loop through each elf's calories
    for elf_id, elf_cals in enumerate(elves):
        temp_list = [int(elf_cals) for elf_cals in elves[elf_id].split('\n') if elf_cals != '']
        temp_elf_dict = dict()
        temp_elf_dict[elf_id] = sum(temp_list)
        elves_cals_dict.update(temp_elf_dict)

    elves_list = sorted(elves_cals_dict.items(), key=lambda x: x[1])
    total_calories = sum([top[1] for top in elves_list[-number:]])
    return total_calories


# get data
with open('day01_input.txt', 'r') as file:
    elf_data = file.read()

# get number of calories
get_most_calories(data=elf_data, number=1)

