import argparse


def part_1(input_string):
    height_map = list(map(list, input_string.split('\n')))
    max_x, max_y = len(height_map) - 1, len(height_map[0]) - 1
    low_sum = 0
    for x, row in enumerate(height_map):
        for y, h, in enumerate(row):
            adjacent = [h]
            if x > 0:
                adjacent.append(height_map[x-1][y])

            if x < max_x:
                adjacent.append(height_map[x+1][y])

            if y > 0:
                adjacent.append(height_map[x][y-1])

            if y < max_y:
                adjacent.append(height_map[x][y+1])

            if int(h) == min(map(int, adjacent)) and adjacent.count(h) == 1:
                low_sum += (int(h) + 1)
    print(low_sum)


def part_2(input_string):
    height_map = list(map(list, input_string.split('\n')))
    max_x, max_y = len(height_map) - 1, len(height_map[0]) - 1
    visited_points = []
    basins = []
    for x, row in enumerate(height_map):
        for y, h, in enumerate(row):
            if (x, y) not in visited_points:
                visited_points.append((x, y))
                if h == '9':
                    continue

                new_basin = [(x, y)]
                for point in new_basin:
                    if point[0] > 0 and ((point[0] - 1, point[1]) not in visited_points):
                        visited_points.append((point[0] - 1, point[1]))
                        if height_map[point[0] - 1][point[1]] != '9':
                            new_basin.append((point[0] - 1, point[1]))

                    if point[0] < max_x and ((point[0] + 1, point[1]) not in visited_points):
                        visited_points.append((point[0] + 1, point[1]))
                        if height_map[point[0] + 1][point[1]] != '9':
                            new_basin.append((point[0] + 1, point[1]))

                    if point[1] > 0 and ((point[0], point[1] - 1) not in visited_points):
                        visited_points.append((point[0], point[1] - 1))
                        if height_map[point[0]][point[1] - 1] != '9':
                            new_basin.append((point[0], point[1] - 1))

                    if point[1] < max_y and ((point[0], point[1] + 1) not in visited_points):
                        visited_points.append((point[0], point[1] + 1))
                        if height_map[point[0]][point[1] + 1] != '9':
                            new_basin.append((point[0], point[1] + 1))

                basins.append(new_basin)

    basins_area = list(map(len, basins))
    basins_area.sort(reverse=True)
    print(basins_area[0] * basins_area[1] * basins_area[2])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_09.txt', 'r')
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
