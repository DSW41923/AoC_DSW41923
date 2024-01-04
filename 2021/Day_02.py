import argparse
import re


SUPPORTED_COMMANDS = ['forward', 'up', 'down']


def part_1(input_string):
    horizontal_pos, depth = 0, 0
    for command, num in re.findall(r'(\w+) (\d+)', input_string):

        if command not in SUPPORTED_COMMANDS:
            raise NotImplementedError

        if command == 'forward':
            horizontal_pos += int(num)
            continue

        if command == 'up':
            depth -= int(num)
            continue

        if command == 'down':
            depth += int(num)
            continue

    print(horizontal_pos * depth)


def part_2(input_string):
    horizontal_pos, depth, aim = 0, 0, 0
    for command, num in re.findall(r'(\w+) (\d+)', input_string):

        if command not in SUPPORTED_COMMANDS:
            raise NotImplementedError

        if command == 'forward':
            horizontal_pos += int(num)
            depth += aim * int(num)
            continue

        if command == 'up':
            aim -= int(num)
            continue

        if command == 'down':
            aim += int(num)
            continue

    print(horizontal_pos * depth)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2021/Input_02.txt', 'r')
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
