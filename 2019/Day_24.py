import argparse

from copy import deepcopy


def get_adjacents(x, y):
    return [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]


def get_recursive_adjacents(l, y, x):
    # Each l level is 5x5, so x, y in [0, 4]
    adjacents = [(l, y, x) for y, x in get_adjacents(y, x)]
    if y == 0:
        adjacents.append((l-1, 1, 2))
    if x == 0:
        adjacents.append((l-1, 2, 1))
    if x == 4:
        adjacents.append((l-1, 2, 3))
    if y == 4:
        adjacents.append((l-1, 3, 2))
    if (y, x) == (1, 2):
        adjacents.extend([(l+1, 0, i) for i in range(5)])
    if (y, x) == (2, 1):
        adjacents.extend([(l+1, i, 0) for i in range(5)])
    if (y, x) == (2, 3):
        adjacents.extend([(l+1, i, 4) for i in range(5)])
    if (y, x) == (3, 2):
        adjacents.extend([(l+1, 4, i) for i in range(5)])
    return adjacents


def part_1(input_string):
    layout = list(map(list, input_string.split('\n')))
    x_range = len(layout[0])
    y_range = len(layout)
    layout_history = [layout]
    while True:
        new_layout = deepcopy(layout)
        for y in range(y_range):
            for x in range(x_range):
                adjacents = get_adjacents(y, x)
                bugs_count = 0
                for adj_y, adj_x in adjacents:
                    if 0 <= adj_y < y_range and 0 <= adj_x < x_range:
                        if layout[adj_y][adj_x] == '#':
                            bugs_count += 1
                if layout[y][x] == '#' and bugs_count != 1:
                    new_layout[y][x] = '.'
                if layout[y][x] == '.' and bugs_count in [1, 2]:
                    new_layout[y][x] = '#'
        
        if new_layout in layout_history:
            result = 0
            for y in range(y_range):
                for x in range(x_range):
                    if new_layout[y][x] == '#':
                        result += 2**(y*x_range+x)
            print(result)
            break
        layout_history.append(new_layout)
        layout = new_layout


def part_2(input_string):
    layout = list(map(list, input_string.split('\n')))
    x_range = len(layout[0])
    y_range = len(layout)
    empty_layout = [['.' for _ in range(x_range)] for _ in range(y_range)]
    layout[2][2] = '?'
    layouts = [layout]
    minutes = 200
    for t in range(minutes):
        layouts.insert(0, deepcopy(empty_layout))
        layouts.append(deepcopy(empty_layout))
        new_layouts = deepcopy(layouts)
        for i in range(len(new_layouts)):
            for y in range(y_range):
                for x in range(x_range):
                    if y == x == 2:
                        new_layouts[i][y][x] = '?'
                        continue
                    adjacents = get_recursive_adjacents(i, y, x)
                    bugs_count = 0
                    for level, adj_y, adj_x in adjacents:
                        if 0 <= level < len(layouts) and 0 <= adj_y < y_range and 0 <= adj_x < x_range:
                            if layouts[level][adj_y][adj_x] == '#':
                                bugs_count += 1
                    if layouts[i][y][x] == '#' and bugs_count != 1:
                        new_layouts[i][y][x] = '.'
                    if layouts[i][y][x] == '.' and bugs_count in [1, 2]:
                        new_layouts[i][y][x] = '#'
        layouts = new_layouts
        # print(len(layouts))

    result = 0
    for l in layouts:
        for line in l:
            result += line.count('#')
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_24.txt', 'r')
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
