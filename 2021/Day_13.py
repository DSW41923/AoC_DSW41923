import argparse
import itertools
import re


def set_dots(dots):
    positions = [[0 for _ in range(max([d[0] for d in dots]) + 1)]
                 for _ in range(max([d[1] for d in dots]) + 1)]
    for dot_x, dot_y in dots:
        positions[dot_y][dot_x] = 1

    return positions


def fold_dots(positions, instructions):
    for axis, axis_num in instructions:
        if axis == 'x':
            new_positions = [[0 for _ in range(axis_num)] for _ in range(len(positions))]
            for y, x in itertools.product(range(len(positions)), range(len(positions[0]))):
                if x < axis_num:
                    new_positions[y][x] = positions[y][x]
                    continue

                if x > axis_num:
                    new_positions[y][2 * axis_num - x] |= positions[y][x]
                    continue

            positions = new_positions
            continue

        if axis == 'y':
            new_positions = [[0 for _ in range(len(positions[0]))] for _ in range(axis_num)]
            for y, x in itertools.product(range(len(positions)), range(len(positions[0]))):
                if y < axis_num:
                    new_positions[y][x] = positions[y][x]
                    continue

                if y > axis_num:
                    new_positions[2 * axis_num - y][x] |= positions[y][x]
                    continue

            positions = new_positions
            continue

        raise

    return positions


def part_1(input_string):
    dots = [tuple(map(int, dot)) for dot in re.findall(r'(\d+),(\d+)', input_string)]
    fold_instructions = [(axis, int(num)) for axis, num in re.findall(r'fold along ([xy])=(\d+)', input_string)]
    positions = set_dots(dots)
    positions = fold_dots(positions, fold_instructions[:1])
    print(sum([sum(row) for row in positions]))


def part_2(input_string):
    dots = [tuple(map(int, dot)) for dot in re.findall(r'(\d+),(\d+)', input_string)]
    fold_instructions = [(axis, int(num)) for axis, num in re.findall(r'fold along ([xy])=(\d+)', input_string)]
    positions = set_dots(dots)
    positions = fold_dots(positions, fold_instructions)

    for r in positions:
        print(''.join(map(str, r)).replace('0', '.').replace('1', '#'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2021/Input_13.txt', 'r')
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
