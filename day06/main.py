"""
Advent of Code 2022
Day 06
"""


def get_first_marker(filepath, window):
    with open(filepath, 'r') as file:
        buffer = file.read()
    for n in range(0, len(buffer)):
        char_window = buffer[n:n+window]
        chars_set = set(char_window)
        if len(chars_set) == window:
            return chars_set, n+window


if __name__ == "__main__":

    window = 14

    chars, marker_position = get_first_marker(filepath='input.txt', window=window)
    print(chars, marker_position)
