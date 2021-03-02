import argparse
import re
import sys


FACINGS = ['N', 'E', 'S', 'W']


def turn(turn_direction, old_facing):
    if turn_direction == 'L':
        new_facing = FACINGS[(FACINGS.index(old_facing) - 1) % 4]
    elif turn_direction == 'R':
        new_facing = FACINGS[(FACINGS.index(old_facing) + 1) % 4]
    else:
        sys.exit()
    return new_facing


def move(x, y, facing, value):
    if facing == 'E':
        return x + value, y
    if facing == 'W':
        return x - value, y
    if facing == 'N':
        return x, y + value
    if facing == 'S':
        return x, y - value


def part_1(instruction_string):
    x, y = 0, 0
    facing = 'N'
    for turn_direction, num in re.findall(r'([LR])(\d+)', instruction_string):
        facing = turn(turn_direction, facing)
        num = int(num)
        x, y = move(x, y, facing, num)
    print("Easter Bunny HQ is {} blocks away!".format(abs(x) + abs(y)))


def part_2(instruction_string):
    x, y = 0, 0
    facing = 'N'
    visited_locations = [(0, 0)]
    for turn_direction, num in re.findall(r'([LR])(\d+)', instruction_string):
        facing = turn(turn_direction, facing)
        for _ in range(int(num)):
            x, y = move(x, y, facing, 1)
            if (x, y) in visited_locations:
                print("Easter Bunny HQ is actually {} blocks away!".format(abs(x) + abs(y)))
                return
            else:
                visited_locations.append((x, y))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_01.txt', 'r')
    instruction_string = file_input.read()
    file_input.close()

    if args.part == '1':
        part_1(instruction_string)
    elif args.part == '2':
        part_2(instruction_string)
    else:
        part_1(instruction_string)
        part_2(instruction_string)


if __name__ == "__main__":
    main()