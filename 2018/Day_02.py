import argparse

from collections import Counter
from itertools import combinations
from string import ascii_lowercase


def part_1(input_string):
    two_counts = 0
    three_counts = 0
    for ids in input_string.split('\n'):
        char_counts = Counter(list(ids))
        if any([char_count == 2 for char_count in char_counts.values()]):
            two_counts += 1
        if any([char_count == 3 for char_count in char_counts.values()]):
            three_counts += 1
    print(three_counts*two_counts)


def part_2(input_string):
    ids = []
    for id in input_string.split('\n'):
        ids.append(id)

    id_len = len(ids[0])
    for id_0, id_1 in combinations(ids, 2):
        diff_count = 0
        diff_index = -1
        for i in range(id_len):
            if id_0[i] != id_1[i]:
                diff_count += 1
                diff_index = i
                if diff_count > 1:
                    break
        
        if diff_count == 1:
            id_char_list = list(id_0)
            id_char_list.pop(diff_index)
            print(''.join(id_char_list))
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_02.txt', 'r')
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
