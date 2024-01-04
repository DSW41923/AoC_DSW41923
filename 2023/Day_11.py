import argparse

from itertools import combinations


def part_1(input_string):
    universe = []
    for line in input_string.split('\n'):
        if all([l == '.' for l in line]):
            universe.append(line)
        universe.append(line)
    expanded_ys = []
    for y in range(len(universe[0])):
        ys = [l[y] for l in universe]
        if all([l == '.' for l in ys]):
            expanded_ys.append(y)
    expanded_ys.insert(0, 0)
    expanded_ys.append(len(universe[0]))
    for x, line in enumerate(universe):
        new_line = '.'.join([line[y0:y1] for y0, y1 in zip(expanded_ys[:-1], expanded_ys[1:])])
        universe[x] = list(new_line)
    galaxies = []
    for x in range(len(universe)):
        for y in range(len(universe[0])):
            if universe[x][y] == '#':
                galaxies.append((x, y))
    length = 0
    for galaxy_0, galaxy_1 in combinations(galaxies, 2):
        length += (abs(galaxy_1[0]-galaxy_0[0]) + abs(galaxy_1[1]-galaxy_0[1]))
    print(length)


def part_2(input_string):
    universe = [list(line) for line in input_string.split('\n')]
    expanded_xs = []
    for x in range(len(universe)):
        if all([l == '.' for l in universe[x]]):
            expanded_xs.append(x)
    expanded_ys = []
    for y in range(len(universe[0])):
        ys = [l[y] for l in universe]
        if all([l == '.' for l in ys]):
            expanded_ys.append(y)
    galaxies = []
    for x in range(len(universe)):
        for y in range(len(universe[0])):
            if universe[x][y] == '#':
                galaxies.append((x, y))
    length = 0
    expand = 1000000
    for galaxy_0, galaxy_1 in combinations(galaxies, 2):
        for i in range(min(galaxy_0[0], galaxy_1[0])+1, max(galaxy_0[0], galaxy_1[0])+1):
            if i in expanded_xs:
                length += expand
            else:
                length += 1
        for i in range(min(galaxy_0[1], galaxy_1[1])+1, max(galaxy_0[1], galaxy_1[1])+1):
            if i in expanded_ys:
                length += expand
            else:
                length += 1
    print(length)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_11.txt', 'r')
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
