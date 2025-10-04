import argparse
import re

from math import ceil, inf


def print_layout(layout, y, x, max_x):
    print(''.join(layout[y][max(0, x-50):min(max_x, x+50)]))

def get_range(layout, y, x, max_x, bound_chars):
    left, right = x, x
    while layout[y][left] not in bound_chars:
        left -= 1
        if left < 0:
            left = 0
            break
    while layout[y][right] not in bound_chars:
        right += 1
        if right > max_x:
            right = max_x
            break
    return left, right


def parse_data(input_string):
    min_x, max_x = inf, 0
    min_y, max_y = inf, 0
    clays = []
    for type_a, start, type_b, begin, end in re.findall(r"([xy])=(\d+), ([xy])=(\d+)..(\d+)", input_string):
        start, begin, end = tuple(map(int, (start, begin, end)))
        clays.append((type_a, start, type_b, begin, end))
        assert end > begin
        if type_a == 'x':
            min_x = min(min_x, start)
            max_x = max(max_x, start)
            min_y = min(min_y, begin)
            max_y = max(max_y, end)
        if type_a == 'y':
            min_x = min(min_x, begin)
            max_x = max(max_x, end)
            min_y = min(min_y, start)
            max_y = max(max_y, start)
    
    return clays, min_x, max_x, min_y, max_y


def flowing(clays, min_x, max_x, max_y):
    offset = min_x - 1
    layout = [['.' for _ in range(100*ceil(max_x / 100.0)-offset)] for _ in range(max_y + 1)]
    layout_max_x = len(layout[0])-1
    layout[0][500-offset] = '+'
    for type_a, start, type_b, begin, end in clays:
        if type_a == 'x':
            for y in range(begin, end+1):
                layout[y][start-offset] = '#'
        if type_a == 'y':
            for x in range(begin, end+1):
                layout[start][x-offset] = '#'
    flow = [(0, 500-offset)]
    while flow:
        flow_y, flow_x = flow.pop(0)
        if flow_y+1 <= max_y:
            if layout[flow_y+1][flow_x] == '.':
                layout[flow_y+1][flow_x] = '|'
                flow.append((flow_y+1, flow_x))
                # print(flow_y+1, flow_x)
                # print_layout(layout, flow_y+1, flow_x, layout_max_x)
            elif layout[flow_y+1][flow_x] == '#':
                # print(flow_y+1, flow_x)
                # print_layout(layout, flow_y, flow_x, layout_max_x)
                # print_layout(layout, flow_y+1, flow_x, layout_max_x)
                left, right = get_range(layout, flow_y, flow_x, layout_max_x, ['#'])
                deeper_left, deeper_right = get_range(layout, flow_y+1, flow_x, layout_max_x, ['.', '|'])
                deeper_left += 1
                deeper_right -= 1
                # print(left, right)
                # print(deeper_left, deeper_right)
                if left >= deeper_left and right <= deeper_right:
                    for x in range(left+1, right):
                        layout[flow_y][x] = '~'
                    flow.append((flow_y-1, flow_x))
                elif left < deeper_left and right > deeper_right:
                    for x in range(deeper_left-1, deeper_right+2):
                        layout[flow_y][x] = '|'
                    flow.append((flow_y, deeper_left-1))
                    flow.append((flow_y, deeper_right+1))
                # print_layout(layout, flow_y, flow_x, layout_max_x)
                # print_layout(layout, flow_y+1, flow_x, layout_max_x)
            elif layout[flow_y+1][flow_x] == '~':
                # print(flow_y+1, flow_x)
                # print_layout(layout, flow_y, flow_x, layout_max_x)
                # print_layout(layout, flow_y+1, flow_x, layout_max_x)
                left, right = get_range(layout, flow_y, flow_x, layout_max_x, ['#'])
                deeper_left, deeper_right = get_range(layout, flow_y+1, flow_x, layout_max_x, ['.', '|'])
                deeper_left += 1
                deeper_right -= 1
                # print(left, right)
                # print(deeper_left, deeper_right)
                if left >= deeper_left and right <= deeper_right:
                    for x in range(left+1, right):
                        layout[flow_y][x] = '~'
                    flow.append((flow_y-1, flow_x))
                elif left >= deeper_left and right > deeper_right:
                    for x in range(left+1, deeper_right+2):
                        layout[flow_y][x] = '|'
                    flow.append((flow_y, deeper_right+1))
                elif left < deeper_left and right <= deeper_right:
                    for x in range(deeper_left-1, right):
                        layout[flow_y][x] = '|'
                    flow.append((flow_y, deeper_left-1))
                elif left < deeper_left and right > deeper_right:
                    for x in range(deeper_left-1, deeper_right+2):
                        layout[flow_y][x] = '|'
                    flow.append((flow_y, deeper_left-1))
                    flow.append((flow_y, deeper_right+1))
                # print_layout(layout, flow_y, flow_x, layout_max_x)
                # print_layout(layout, flow_y+1, flow_x, layout_max_x)

    return layout


def part_1(input_string):
    clays, min_x, max_x, min_y, max_y = parse_data(input_string)
    layout = flowing(clays, min_x, max_x, max_y)
    # for line in layout:
    #     print(''.join(line[:200]))
    # print()
    # for line in layout:
    #     print(''.join(line[200:]))
    result = 0
    for line in layout[min_y:]:
        result += line.count('|') + line.count('~')
    print(result)

def part_2(input_string):
    clays, min_x, max_x, min_y, max_y = parse_data(input_string)
    layout = flowing(clays, min_x, max_x, max_y)
    result = 0
    for line in layout[min_y:]:
        result += line.count('~')
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_17.txt', 'r')
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
