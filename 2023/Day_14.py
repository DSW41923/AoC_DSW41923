import argparse
import re

from copy import deepcopy


def part_1(input_string):
    platform = [list(row) for row in input_string.split('\n')]
    for r, row in enumerate(platform[1:]):
        for c, column in enumerate(row):
            if column == 'O' and platform[r][c] == '.': # Rolling stone found!
                dest_row = 0
                if r > 0:
                    ahead_row = [rr[c] for rr in platform[:r+1]]
                    if not all([ar == '.' for ar in ahead_row]):
                        dest_row = ([m.start() for m in re.finditer(r'[#O]\.', ''.join(ahead_row))])[-1] + 1
                platform[dest_row][c] = 'O'
                platform[r+1][c] = '.'
    load = 0
    for r, row in enumerate(platform):
        for space in row:
            if space == 'O':
                load += (len(platform)-r)
    print(load)


def part_2(input_string):
    def update_platform(platform):
        # Roll north
        for r, row in enumerate(platform[1:]):
            for c, column in enumerate(row):
                if column == 'O' and platform[r][c] == '.': # Rolling stone found!
                    dest_row = 0
                    if r > 0:
                        ahead_row = [rr[c] for rr in platform[:r+1]]
                        if not all([ar == '.' for ar in ahead_row]):
                            dest_row = ([m.start() for m in re.finditer(r'[#O]\.', ''.join(ahead_row))])[-1] + 1
                    platform[dest_row][c] = 'O'
                    platform[r+1][c] = '.'
        # Roll west
        for c in range(len(platform[0])):
            if c == 0: # No need to move for the first column
                continue
            for r in range(len(platform)):
                if platform[r][c] == 'O' and platform[r][c-1] == '.': # Rolling stone found!
                    dest_column = 0
                    if c > 1:
                        ahead_column = platform[r][:c]
                        if not all([ar == '.' for ar in ahead_column]):
                            dest_column = ([m.start() for m in re.finditer(r'[#O]\.', ''.join(ahead_column))])[-1] + 1
                    platform[r][dest_column] = 'O'
                    platform[r][c] = '.'
        # Roll south
        for r in range(len(platform)-1, -1, -1):
            if r == len(platform) - 1: # No need to move for the first row
                continue
            row = platform[r]
            for c, column in enumerate(row):
                if column == 'O' and platform[r+1][c] == '.': # Rolling stone found!
                    dest_row = len(platform) - 1
                    if r < (len(platform) - 2):
                        ahead_row = [rr[c] for rr in platform[r+1:]]
                        if not all([ar == '.' for ar in ahead_row]):
                            dest_row = (r+1)+([m.start() for m in re.finditer(r'\.[#O]', ''.join(ahead_row))])[0]
                    platform[dest_row][c] = 'O'
                    platform[r][c] = '.'
        # Roll east
        for c in range(len(platform[0])-1, -1, -1):
            if c == len(platform[0]) - 1: # No need to move for the first column
                continue
            for r in range(len(platform)):
                if platform[r][c] == 'O' and platform[r][c+1] == '.': # Rolling stone found!
                    dest_column = len(platform[0]) - 1
                    if c < (len(platform[0]) - 2):
                        ahead_column = platform[r][c+1:]
                        if not all([ar == '.' for ar in ahead_column]):
                            dest_column = (c+1)+([m.start() for m in re.finditer(r'\.[#O]', ''.join(ahead_column))])[0]
                    platform[r][dest_column] = 'O'
                    platform[r][c] = '.'
        return platform

    platform = [list(row) for row in input_string.split('\n')]
    platforms = [platform]
    loop_len = 0
    loop_start = 0
    for k in range(1000000000):
        next_platform = deepcopy(platform)
        next_platform = update_platform(next_platform)
        if next_platform not in platforms:
            platforms.append(next_platform)
            platform = next_platform
        else:
            loop_start = platforms.index(next_platform)
            loop_len = k - loop_start + 1
            break
    result_index = (1000000000 - loop_start) % loop_len + loop_start
    load = 0
    for r, row in enumerate(platforms[result_index]):
        for space in row:
            if space == 'O':
                load += (len(platform)-r)
    print(load)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_14.txt', 'r')
    input_string = file_input.read()
    file_input.close()

    if args.part == '1':
        part_1(input_string)
    elif args.part == '2':
        part_2(input_string)
    else:
        part_1(input_string)
        part_2(input_string)


if __name__ == "__main__":
    main()
