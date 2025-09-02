import argparse

from itertools import combinations


def get_map_data(input_string):
    antennas_map = list(map(list, input_string.split('\n')))
    max_x = len(antennas_map)
    max_y = len(antennas_map[0])
    antennas = {}
    for x in range(max_x):
        for y in range(max_y):
            if antennas_map[x][y] != '.':
                if antennas_map[x][y] in antennas:
                    antennas[antennas_map[x][y]] += [(x, y)]
                else:
                    antennas[antennas_map[x][y]] = [(x, y)]
    return antennas_map, max_x, max_y, antennas


def part_1(input_string):
    _, max_x, max_y, antennas = get_map_data(input_string)
    antinodes = []
    for locations in antennas.values():
        for loc_0, loc_1 in combinations(locations, 2):
            antinode_0 = (2*loc_0[0]-loc_1[0], 2*loc_0[1]-loc_1[1])
            if 0 <= antinode_0[0] < max_x and 0 <= antinode_0[1] < max_y:
                antinodes.append(antinode_0)
            antinode_1 = (2*loc_1[0]-loc_0[0], 2*loc_1[1]-loc_0[1])
            if 0 <= antinode_1[0] < max_x and 0 <= antinode_1[1] < max_y:
                antinodes.append(antinode_1)
    print(len(set(antinodes)))


def part_2(input_string):
    _, max_x, max_y, antennas = get_map_data(input_string)
    antinodes = []
    for locations in antennas.values():
        for loc_0, loc_1 in combinations(locations, 2):
            if loc_1[0] < loc_0[0]: loc_0, loc_1 = loc_1, loc_0
            x_diff = loc_1[0]-loc_0[0]
            y_diff = loc_1[1]-loc_0[1]
            x, y = loc_0
            while 0 <= x < max_x and 0 <= y < max_y:
                antinodes.append((x, y))
                x -= x_diff
                y -= y_diff
            x, y = loc_0
            while 0 <= x < max_x and 0 <= y < max_y:
                antinodes.append((x, y))
                x += x_diff
                y += y_diff
            # slope = (loc_1[1]-loc_0[1]) / (loc_1[0]-loc_0[0])
            # # y-loc_0[1] = slope * (x-loc_0[0])
            # # y = slope * x + loc_0[1] - slope * loc_0[0]
            # for x in range(max_x):
            #     y = slope * x + loc_0[1] - slope * loc_0[0]
            #     if 0 <= y < max_y and int(y) == y:
            #         antinodes.append((x, y))
    print(len(set(antinodes)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_08.txt', 'r')
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
