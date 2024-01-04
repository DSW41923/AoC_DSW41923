import argparse
import re

from functools import cache


def part_1(input_string):
    records = [(record[0], tuple(map(int, record[1].split(',')))) for record in re.findall(r"([.#?]+) ([\d,]+)", input_string)]
    possible_arrangements_count = 0
    for record in records:
        unknown_index = [m.start() for m in re.finditer(r'\?', record[0])]
        max_arrangements = 1 << len(unknown_index)
        total_damaged_springs_count = sum(record[1])
        cur_damaged_springs_count = record[0].count('#')
        unkown_damaged_springs_count = total_damaged_springs_count - cur_damaged_springs_count
        for i in range(max_arrangements):
            arrangement = bin(i)[2:].zfill(len(unknown_index)).replace('0', '.').replace('1', '#')
            if arrangement.count('#') == unkown_damaged_springs_count:
                new_arrangement = list(record[0])
                for j in range(len(arrangement)):
                    new_arrangement[unknown_index[j]] = arrangement[j]
                new_arrangement = ''.join(new_arrangement)
                new_damaged_springs = tuple(map(lambda g: g.count('#'), re.split(r"\.+", new_arrangement.strip('.'))))
                if new_damaged_springs == record[1]:
                    possible_arrangements_count += 1
    print(possible_arrangements_count)


def part_2(input_string):
    records = [('?'.join([record[0] for _ in range(5)]).strip('.') + '.', tuple(map(int, record[1].split(',') * 5))) for record in re.findall(r"([.#?]+) ([\d,]+)", input_string)]
    possible_arrangements_count = 0
    for record in records:
        @cache
        def possible_arrangements(cur_arrangement, groups):
            if len(cur_arrangement) * len(groups) == 0:
                if len(cur_arrangement) != 0: return int('#' not in cur_arrangement)
                if len(groups) != 0: return 0
                return 1
            if cur_arrangement.startswith('.'): return possible_arrangements(cur_arrangement[1:], groups)
            elif cur_arrangement.startswith('?'): 
                return possible_arrangements(cur_arrangement[1:], groups) + possible_arrangements('#' + cur_arrangement[1:], groups)
            group_str = '#' * groups[0] + '.'
            for i in range(groups[0] + 1):
                if cur_arrangement[i] == '?':
                    cur_arrangement = cur_arrangement[:i] + group_str[i] + cur_arrangement[i + 1:]
                    continue
                if group_str[i] != cur_arrangement[i]:
                    return 0
            return possible_arrangements(cur_arrangement[groups[0] + 1:], groups[1:])
        possible_arrangements_count += possible_arrangements(record[0], record[1])
    print(possible_arrangements_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2023/Input_12.txt', 'r')
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
