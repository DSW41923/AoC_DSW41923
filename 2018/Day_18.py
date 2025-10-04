import argparse

from copy import deepcopy


def get_adjacents(x, y, max_x, max_y):
    adjacents = []
    if y > 0:
        adjacents.append((x, y-1))
    if y < max_y-1:
        adjacents.append((x, y+1))
    if x > 0:
        adjacents.append((x-1, y))
        if y > 0:
            adjacents.append((x-1, y-1))
        if y < max_y-1:
            adjacents.append((x-1, y+1))
    if x < max_x-1:
        adjacents.append((x+1, y))
        if y > 0:
            adjacents.append((x+1, y-1))
        if y < max_y-1:
            adjacents.append((x+1, y+1))

    return adjacents


def area_changing_v1(area, minutes):
    x_range = len(area)
    y_range = len(area[0])
    for _ in range(minutes):
        new_area = deepcopy(area)
        for x in range(x_range):
            for y in range(y_range):
                area_type = area[x][y]
                adj = get_adjacents(x, y, x_range, y_range)
                adj_type = [area[adj_x][adj_y] for adj_x, adj_y in adj]
                if area_type == '.':
                    if adj_type.count('|') >= 3:
                        new_area[x][y] = '|'
                elif area_type == '|':
                    if adj_type.count('#') >= 3:
                        new_area[x][y] = '#'
                elif area_type == '#':
                    if not(adj_type.count('#') >= 1 and adj_type.count('|') >= 1):
                        new_area[x][y] = '.'
        area = new_area
    return area


def area_changing_v2(area):
    x_range = len(area)
    y_range = len(area[0])
    new_area = deepcopy(area)
    for x in range(x_range):
        for y in range(y_range):
            area_type = area[x][y]
            adj = get_adjacents(x, y, x_range, y_range)
            adj_type = [area[adj_x][adj_y] for adj_x, adj_y in adj]
            if area_type == '.':
                if adj_type.count('|') >= 3:
                    new_area[x][y] = '|'
            elif area_type == '|':
                if adj_type.count('#') >= 3:
                    new_area[x][y] = '#'
            elif area_type == '#':
                if not(adj_type.count('#') >= 1 and adj_type.count('|') >= 1):
                    new_area[x][y] = '.'
    area = new_area
    return area


def resource_value(area):
    wooded, lumberyards = 0, 0
    for line in area:
        wooded += line.count('|')
        lumberyards += line.count('#')
    return wooded * lumberyards


def part_1(input_string):
    area = list(map(list, input_string.split('\n')))
    area = area_changing_v1(area, 10)
    print(resource_value(area))


def part_2(input_string):
    area = list(map(list, input_string.split('\n')))
    minutes = 1000000000
    area_history = [input_string]
    for m in range(1, minutes+1):
        area = area_changing_v2(area)
        area_string = '\n'.join(list(map(lambda l: ''.join(l), area)))
        if area_string in area_history:
            existed_area_index = area_history.index(area_string)
            result_area_index = existed_area_index + (minutes - existed_area_index) % (m-existed_area_index)
            result_area = list(map(list, area_history[result_area_index].split('\n')))
            print(resource_value(result_area))
            break
        area_history.append(area_string)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_18.txt', 'r')
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
