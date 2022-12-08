"""
Advent of Code 2022
Day 05
"""
import re

with open('input.txt', 'r') as file:
    problem = file.read()

# set which crane used
cratemover_9001 = True
cratemover_9000 = False

# set up lists of crate stacks and moves
crates, move_commands = problem.split('\n\n')
stack_string_index = [1, 5, 9, 13, 17, 21, 25, 29, 33]
stacks = [[] for _ in stack_string_index]

for row in crates.splitlines(keepends=False)[:-1]:  # ignore numbers
    print(row)
    for stack_n, index in enumerate(stack_string_index):
        if row[index] != ' ':
            stacks[stack_n].append(row[index])

moves = [
    re.match(r'move (\d*) from (\d*) to (\d*)', row).groups()
    for row in move_commands.splitlines()
]

for move in moves:
    total, _from, to = move
    print(f'move: {total, _from, to}')
    crates_to_move = stacks[int(move[1]) - 1][:int(total)]
    print(f'crates to move: {crates_to_move}')
    # move x crates to new stack
    # pop into new list
    if cratemover_9000:
        for crate in crates_to_move:
            stacks[int(move[1]) - 1].pop(0)
            stacks[int(move[2]) - 1].insert(0, crate)
    if cratemover_9001:
        for crate in crates_to_move:
            stacks[int(move[1]) - 1].remove(crate)
        stacks[int(move[2]) - 1] = crates_to_move + stacks[int(move[2]) - 1]

top_crates = ''.join([c[0] for c in stacks])
