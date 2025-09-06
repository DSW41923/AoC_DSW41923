import argparse
import re


def part_1(input_string):
    areas = {}
    min_x, min_y = 1000, 1000
    max_x, max_y = 0, 0
    for x, y in re.findall(r"(\d+), (\d+)", input_string):
        x, y = tuple(map(int, (x, y)))
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        if (x, y) not in areas:
            areas[(x, y)] = [(x, y)]

    for x in range(min_x-100, max_x+100):
        for y in range(min_y-100, max_y+100):
            if (x, y) in areas:
                continue
            min_distance = 1000
            distances = [abs(area_x-x)+abs(area_y-y) for area_x, area_y in areas]
            min_distance = min(distances)
            if distances.count(min_distance) == 1:
                for area_x, area_y in areas:
                    if abs(area_x-x)+abs(area_y-y) == min_distance:
                        areas[(area_x, area_y)].append((x, y))

    max_area = 0
    for area_x, area_y in areas:
        if any([x == (min_x-100) or x == (max_x+99) or y == (min_y-100) or y == (max_y+99) for x, y in areas[(area_x, area_y)]]):
            continue
        max_area = max(max_area, len(areas[(area_x, area_y)]))
    print(max_area)


def part_2(input_string):
    coordinates = []
    min_x, min_y = 1000, 1000
    max_x, max_y = 0, 0
    for x, y in re.findall(r"(\d+), (\d+)", input_string):
        x, y = tuple(map(int, (x, y)))
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        coordinates.append((x, y))

    result = 0
    for x in range(min_x-100, max_x+100):
        for y in range(min_y-100, max_y+100):
            all_distance = 0
            for area_x, area_y in coordinates:
                all_distance += abs(area_x-x)+abs(area_y-y)
            if all_distance < 10000:
                result += 1
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_06.txt', 'r')
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
