import argparse
import itertools
import re



def get_adjacents(x0, max_x, y0, y1, max_y):
    xs = list(range(max(x0-1, 0), min(x0+2, max_x)))
    ys = list(range(max(y0-1, 0), min(y1+1, max_y)))
    adjacents = []
    for x, y in itertools.product(xs, ys):
        if not (x == x0 and y0 <= y < y1):
            adjacents.append((x, y))
    return adjacents


def part_1(input_string):
    maps = input_string.split('\n')
    numbers_data = []
    for row, map_row in enumerate(maps):
        for number_data in re.finditer(r'(\d+)', map_row):
            numbers_data.append((int(number_data.group()), row, number_data.span()))
    maps = list(map(list, maps))
    result = 0
    for number, row, number_span in numbers_data:
        adjacents = get_adjacents(row, len(maps), number_span[0], number_span[1], len(maps[0]))
        if any([maps[i][j] not in list('.0123456789') for i, j in adjacents]):
            result += number
    print(result)


def part_2(input_string):
    maps = input_string.split('\n')
    numbers_data = []
    for row, map_row in enumerate(maps):
        for number_data in re.finditer(r'(\d+)', map_row):
            numbers_data.append((int(number_data.group()), row, number_data.span()))
    maps = list(map(list, maps))
    gear_candidates = []
    for number, row, number_span in numbers_data:
        adjacents = get_adjacents(row, len(maps), number_span[0], number_span[1], len(maps[0]))
        for i, j in adjacents:
            if maps[i][j] == '*':
                gear_candidates.append((number, (i, j)))
    gear_candidates = sorted(gear_candidates, key=lambda g: g[1])
    result = 0
    i = 0
    while i < len(gear_candidates):
        if gear_candidates[i][1] == gear_candidates[i+1][1]:
            result += (gear_candidates[i][0] * gear_candidates[i+1][0])
            i += 2
            continue
        
        i += 1
    print(result)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2023/Input_03.txt', 'r')
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
