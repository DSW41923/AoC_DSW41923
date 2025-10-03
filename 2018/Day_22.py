import argparse
import heapq

from functools import lru_cache
from math import ceil


def parse_data(input_string):
    depth, target = input_string.split('\n')
    depth = int(depth.split(' ')[-1])
    target = tuple(map(int, target.split(' ')[-1].split(',')))
    x_range, y_range = target[0] + 1, target[1] + 1
    return depth, target, x_range, y_range


def get_risk_levels(target, depth, x_range, y_range):
    risk_levels = [[-1 for _ in range(y_range)] for _ in range(x_range)]
    risk_levels[0][0] = depth % 20183
    for x in range(x_range):
        risk_levels[x][0] = x*16807
        risk_levels[x][0] += depth
        risk_levels[x][0] %= 20183
    for y in range(y_range):
        risk_levels[0][y] = y*48271
        risk_levels[0][y] += depth
        risk_levels[0][y] %= 20183
    for x in range(1, x_range):
        for y in range(1, y_range):
            risk_levels[x][y] = risk_levels[x-1][y] * risk_levels[x][y-1]
            risk_levels[x][y] += depth
            risk_levels[x][y] %= 20183
    risk_levels[target[0]][target[1]] = depth % 20183
    for x in range(x_range):
        for y in range(y_range):
            risk_levels[x][y] %= 3
    return risk_levels

@lru_cache(maxsize=None)
def get_erosion_levels(target, depth, x, y):
    if (x, y) in [(0, 0), target]:
        return depth % 20183
    if x == 0:
        return (y*48271 + depth) % 20183
    if y == 0:
        return (x*16807 + depth) % 20183
    return (get_erosion_levels(target, depth, x-1, y)*get_erosion_levels(target, depth, x, y-1)+depth) % 20183


def part_1(input_string):
    depth, target, x_range, y_range = parse_data(input_string)
    risk_levels = get_risk_levels(target, depth, x_range, y_range)
    print(sum((map(sum, risk_levels))))


def part_2(input_string):
    depth, target, x_range, y_range = parse_data(input_string)
    # risk_str = ['.', '=', '|']
    # for i in range(20):
    #     for j in range(20):
    #         cur_risk_level = get_erosion_levels(target, depth, j, i) % 3
    #         print(risk_str[cur_risk_level], end='')
    #     print()
    tools = ["neither", "torch", "climbing gear"]
    src = (0, 0)
    minute_records = {}
    minute_records = {(src, 'torch'): 0}
    front_pos = [(0, src, 'torch')]
    while front_pos:
        minutes, pos, tool = heapq.heappop(front_pos)
        if minutes > minute_records[(pos, tool)]:
            continue
        if (target, 'torch') in minute_records:
            if minutes >= minute_records[(target, 'torch')]:
                continue
        pos_x, pos_y = pos
        cur_risk_level = get_erosion_levels(target, depth, pos_x, pos_y) % 3
        for t, new_tool in enumerate(tools):
            new_minutes = minutes + 7
            if new_tool != tool:
                if t != cur_risk_level:
                    heapq.heappush(front_pos, (new_minutes, pos, new_tool))
                    if (pos, new_tool) in minute_records:
                        if new_minutes < minute_records[(pos, new_tool)]:
                            minute_records[(pos, new_tool)] = new_minutes
                    else:
                        minute_records.update({
                            (pos, new_tool): new_minutes
                        })

        possible_next_pos = [(pos_x + 1, pos_y), (pos_x, pos_y + 1)]
        if 0 < pos_x:
            possible_next_pos.append((pos_x - 1, pos_y))
        if 0 < pos_y:
            possible_next_pos.append((pos_x, pos_y - 1))

        for next_pos in possible_next_pos:
            new_minutes = minutes + 1
            next_pos_x, next_pos_y = next_pos
            next_risk_level = get_erosion_levels(target, depth, next_pos_x, next_pos_y) % 3
            if tool == 'torch':
                if next_risk_level == 1:
                    continue
            if tool == 'climbing gear':
                if next_risk_level == 2:
                    continue
            if tool == 'neither':
                if next_risk_level == 0:
                    continue
            if (next_pos, tool) in minute_records:
                if new_minutes < minute_records[(next_pos, tool)]:
                    minute_records[(next_pos, tool)] = new_minutes
                    heapq.heappush(front_pos, (new_minutes, next_pos, tool))
            else:
                minute_records.update({
                    (next_pos, tool): new_minutes
                })
                heapq.heappush(front_pos, (new_minutes, next_pos, tool))
    print(minute_records[(target, 'torch')])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_22.txt', 'r')
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
