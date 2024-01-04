import argparse
import re


def get_scan(input_string, max_x, max_y):
    rock_paths = input_string.split('\n')
    rock_scan = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    rock_scan[0][500] = '+'
    for rock_path in rock_paths:
        rock_lines = rock_path.split(' -> ')
        for rock_line_start, rock_line_end in zip(rock_lines[:-1], rock_lines[1:]):
            rock_line_start_x, rock_line_start_y = tuple(map(int, eval(rock_line_start)))
            rock_line_end_x, rock_line_end_y = tuple(map(int, eval(rock_line_end)))
            if rock_line_start_x == rock_line_end_x:
                for y in range(min(rock_line_start_y, rock_line_end_y), max(rock_line_start_y, rock_line_end_y) + 1):
                    rock_scan[y][rock_line_start_x] = '#'
                continue
            if rock_line_start_y == rock_line_end_y:
                for x in range(min(rock_line_start_x, rock_line_end_x), max(rock_line_start_x, rock_line_end_x) + 1):
                    rock_scan[rock_line_end_y][x] = '#'
                continue
    return rock_scan


def get_next_sand_pos(rock_scan, sand_pos):
    sand_y, sand_x = sand_pos
    if rock_scan[sand_y + 1][sand_x] == '.':
        return (sand_y + 1, sand_x)
    if rock_scan[sand_y + 1][sand_x - 1] == '.':
        return (sand_y + 1, sand_x - 1)
    if rock_scan[sand_y + 1][sand_x + 1] == '.':
        return (sand_y + 1, sand_x + 1)
    return sand_pos


def part_1(input_string):
    max_rock_x = max([int(x) for x in re.findall(r'(\d+),', input_string)])
    max_rock_y = max([int(y) for y in re.findall(r',(\d+)', input_string)])
    rock_scan = get_scan(input_string, max_rock_x, max_rock_y)
    sand_src = (0, 500)
    sand_pos = sand_src
    settled_sand_count = 0
    while sand_pos[0] < max_rock_y and sand_pos[1] < max_rock_x:
        next_sand_pos = get_next_sand_pos(rock_scan, sand_pos)
        if next_sand_pos != sand_pos:
            sand_pos = next_sand_pos
            continue
        rock_scan[sand_pos[0]][sand_pos[1]] = 'o'
        settled_sand_count += 1
        sand_pos = sand_src
    print(settled_sand_count)


def part_2(input_string):
    max_rock_x = max([int(x) for x in re.findall(r'(\d+),', input_string)])
    max_rock_y = max([int(y) for y in re.findall(r',(\d+)', input_string)])
    max_rock_y += 2
    max_rock_x = max(500 + max_rock_y, max_rock_x)
    rock_scan = get_scan(input_string, max_rock_x, max_rock_y)
    rock_scan[max_rock_y] = ['#' for _ in range(max_rock_x + 1)]
    sand_src = (0, 500)
    sand_pos = sand_src
    settled_sand_count = 0
    while True:
        next_sand_pos = get_next_sand_pos(rock_scan, sand_pos)
        if next_sand_pos != sand_pos:
            sand_pos = next_sand_pos
            continue
        rock_scan[sand_pos[0]][sand_pos[1]] = 'o'
        settled_sand_count += 1
        if sand_pos == sand_src:
            break
        sand_pos = sand_src
        # Optional output
        # print('\n'.join([''.join(row) for row in rock_scan]))
    print(settled_sand_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2022/Input_14.txt', 'r')
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

