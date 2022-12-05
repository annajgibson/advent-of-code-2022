"""
Advent of Code 2022
Day 04
"""


def get_sections(sections):
    start_stop = sections.split('-')
    section_list = [n for n in range(int(start_stop[0]), int(start_stop[1]) + 1)]
    return set(section_list)


with open('input.txt', 'r') as file:
    pairs = file.read()

# compare lists
pair_list = [pair for pair in pairs.split('\n') if pair != '']
pair_list_nested = [each_pair.split(',') for each_pair in pair_list]

# part 1
# create list of numbers for each nested pair
number_full_overlaps = 0
for sections in pair_list_nested:
    elf_1_list = get_sections(sections[0])
    elf_2_list = get_sections(sections[1])
#     compare lists
    if (elf_1_list <= elf_2_list) | (elf_2_list <= elf_1_list):
        number_full_overlaps += 1
        print(elf_1_list, elf_2_list)
print(number_full_overlaps)

# part 2
number_overlaps_anywhere = 0
for sections in pair_list_nested:
    print(sections)
    elf_1_list = get_sections(sections[0])
    elf_2_list = get_sections(sections[1])
    # get intersects
    overlaps = elf_1_list & elf_2_list
    if overlaps:
        number_overlaps_anywhere += 1
        print(overlaps)
print(number_overlaps_anywhere)
