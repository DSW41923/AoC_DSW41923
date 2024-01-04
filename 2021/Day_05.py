import argparse
import re


def part_1(input_string):
    vents_considered = []
    max_x, max_y = 0, 0
    for vent0_x, vent0_y, vent1_x, vent1_y in re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', input_string):
        vent0_x, vent0_y, vent1_x, vent1_y = map(int, (vent0_x, vent0_y, vent1_x, vent1_y))
        max_x = max(vent1_x, max_x)
        max_y = max(vent1_y, max_y)

        if vent0_x != vent1_x and vent0_y != vent1_y:
            continue

        vents_considered.append((
            (min(vent0_x, vent1_x), min(vent0_y, vent1_y)),
            (max(vent0_x, vent1_x), max(vent0_y, vent1_y))))

    diagram = [[0 for _ in range(max_y+1)] for _ in range(max_x+1)]
    for vent in vents_considered:
        if (x := vent[0][0]) == vent[1][0]:
            for y in range(vent[0][1], vent[1][1] + 1):
                diagram[x][y] += 1
            continue

        if (y := vent[0][1]) == vent[1][1]:
            for x in range(vent[0][0], vent[1][0] + 1):
                diagram[x][y] += 1
            continue

    danger_count = 0
    for x in range(max_x+1):
        for y in range(max_y+1):
            if diagram[x][y] >= 2:
                danger_count += 1

    print(danger_count)


def part_2(input_string):
    vents = []
    max_x, max_y = 0, 0
    for vent0_x, vent0_y, vent1_x, vent1_y in re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', input_string):
        vent0_x, vent0_y, vent1_x, vent1_y = map(int, (vent0_x, vent0_y, vent1_x, vent1_y))
        max_x = max(vent1_x, max_x)
        max_y = max(vent1_y, max_y)

        if vent0_x == vent1_x or vent0_y == vent1_y:
            vents.append((
                (min(vent0_x, vent1_x), min(vent0_y, vent1_y)),
                (max(vent0_x, vent1_x), max(vent0_y, vent1_y))))
            continue

        vents.append(((vent0_x, vent0_y), (vent1_x, vent1_y)))

    diagram = [[0 for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    for vent in vents:
        if (x := vent[0][0]) == vent[1][0]:
            for y in range(vent[0][1], vent[1][1] + 1):
                diagram[x][y] += 1
            continue

        if (y := vent[0][1]) == vent[1][1]:
            for x in range(vent[0][0], vent[1][0] + 1):
                diagram[x][y] += 1
            continue

        x_range = range(vent[0][0], vent[1][0] + 1)
        if vent[0][0] > vent[1][0]:
            x_range = range(vent[0][0], vent[1][0] - 1, -1)
        y_range = range(vent[0][1], vent[1][1] + 1)
        if vent[0][1] > vent[1][1]:
            y_range = range(vent[0][1], vent[1][1] - 1, -1)

        for x, y in zip(x_range, y_range):
            diagram[x][y] += 1

    danger_count = 0
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if diagram[x][y] >= 2:
                danger_count += 1

    print(danger_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2021/Input_05.txt', 'r')
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
