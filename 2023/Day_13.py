import argparse

from copy import deepcopy


def get_row_reflection(pattern):
    row_range = len(pattern)
    for r in range(row_range-1):
        reflecting_row = (r, r+1)
        while 0 <= reflecting_row[0] and reflecting_row[1] < row_range:
            if pattern[reflecting_row[0]] == pattern[reflecting_row[1]]:
                reflecting_row = (reflecting_row[0]-1, reflecting_row[1]+1)
            else:
                reflecting_row = (row_range, row_range)
        if reflecting_row != (row_range, row_range):
            return r
    return -1

def get_column_reflection(pattern):
    column_range = len(pattern[0])
    for c in range(column_range-1):
        reflecting_column = (c, c+1)
        while 0 <= reflecting_column[0] and reflecting_column[1] < column_range:
            if [p[reflecting_column[0]] for p in pattern] == [p[reflecting_column[1]] for p in pattern]:
                reflecting_column = (reflecting_column[0]-1, reflecting_column[1]+1)
            else:
                reflecting_column = (column_range, column_range)
        if reflecting_column != (column_range, column_range):
            return c
    return -1

def part_1(input_string):
    patterns = [[list(p) for p in pattern.split('\n')] for pattern in input_string.split('\n\n')]
    result = 0
    for pattern in patterns:
        result += 100 * (get_row_reflection(pattern)+1)
        result += (get_column_reflection(pattern)+1)
    print(result)


def part_2(input_string):
    patterns = [[list(p) for p in pattern.split('\n')] for pattern in input_string.split('\n\n')]
    result = 0
    for p, pattern in enumerate(patterns):
        old_reflection = ('r', get_row_reflection(pattern))
        if old_reflection[1] == -1:
            old_reflection = ('c', get_column_reflection(pattern))
        new_reflection = None
        row_range = len(pattern)
        column_range = len(pattern[0])
        for r in range(row_range-1):
            reflecting_row = (r, r+1)
            while 0 <= reflecting_row[0] and reflecting_row[1] < row_range:
                if len([c for c in range(column_range) if pattern[reflecting_row[0]][c] != pattern[reflecting_row[1]][c]]) <= 1:
                    reflecting_row = (reflecting_row[0]-1, reflecting_row[1]+1)
                else:
                    reflecting_row = (row_range, row_range)
            if reflecting_row != (row_range, row_range) and ('r', r) != old_reflection:
                new_reflection = ('r', r)
        for c in range(column_range-1):
            reflecting_column = (c, c+1)
            while 0 <= reflecting_column[0] and reflecting_column[1] < column_range:
                if len([r for r in range(row_range) if pattern[r][reflecting_column[0]] != pattern[r][reflecting_column[1]]]) <= 1:
                    reflecting_column = (reflecting_column[0]-1, reflecting_column[1]+1)
                else:
                    reflecting_column = (column_range, column_range)
            if reflecting_column != (column_range, column_range) and ('c', c) != old_reflection:
                new_reflection = ('c', c)
        if new_reflection[0] == 'r':
            result += 100 * (new_reflection[1]+1)
        elif new_reflection[0] == 'c':
            result += (new_reflection[1]+1)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2023/Input_13.txt', 'r')
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
