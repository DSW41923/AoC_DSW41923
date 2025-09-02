import argparse
import re

from collections import Counter

def part_1(input_string):
    left = []
    right = []
    for left_num, right_num in re.findall(r'(\d+) +(\d+)', input_string):
        left.append(int(left_num))
        right.append(int(right_num))
    left.sort()
    right.sort()
    result = 0
    for l, r in zip(left, right):
        result += abs(r - l)
    print(result)


def part_2(input_string):
    left = []
    right = []
    for left_num, right_num in re.findall(r'(\d+) +(\d+)', input_string):
        left.append(int(left_num))
        right.append(int(right_num))
    right_counter = Counter(right)
    result = 0
    for l in left:
        result += l * right_counter[l]
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_01.txt', 'r')
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
