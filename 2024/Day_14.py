import argparse
import re

from math import inf
from statistics import mean, stdev

def get_robots_data(input_string):
    robots = []
    for pos_x, pos_y, v_x, v_y in re.findall(r"p=(\d+),(\d+) v=([-\d]+),([-\d]+)", input_string):
        pos_x, pos_y, v_x, v_y = int(pos_x), int(pos_y), int(v_x), int(v_y)
        robots.append(
            {
                'pos': {
                    'x': pos_x,
                    'y': pos_y
                },
                'velocity': {
                    'x': v_x,
                    'y': v_y
                }
            }
        )
    return robots


def part_1(input_string):
    robots = get_robots_data(input_string)
    robots_num = len(robots)
    space_x_range = 101
    space_y_range = 103
    for _ in range(robots_num):
        robot = robots.pop(0)
        robot['pos']['x'] += 100 * robot['velocity']['x']
        robot['pos']['x'] %= space_x_range
        robot['pos']['y'] += 100 * robot['velocity']['y']
        robot['pos']['y'] %= space_y_range
        robots.append(robot)
        assert(len(robots) == robots_num)
    robots_top_left = [robot for robot in robots if robot['pos']['x'] < 50 and robot['pos']['y'] < 51]
    robots_top_right = [robot for robot in robots if robot['pos']['x'] < 50 and robot['pos']['y'] > 51]
    robots_bottom_left = [robot for robot in robots if robot['pos']['x'] > 50 and robot['pos']['y'] < 51]
    robots_bottom_right = [robot for robot in robots if robot['pos']['x'] > 50 and robot['pos']['y'] > 51]
    print(len(robots_top_left) * len(robots_top_right) * len(robots_bottom_left) * len(robots_bottom_right))


def part_2(input_string):
    robots = get_robots_data(input_string)
    robots_num = len(robots)
    space_x_range = 101
    space_y_range = 103
    x_second = 0
    y_second = 0
    for i in range(space_y_range):
        row_robots = [[] for _ in range(space_y_range)]
        col_robots = [[] for _ in range(space_x_range)]
        for robot in robots:
            row_robots[robot['pos']['y']].append(robot['pos']['x'])
            col_robots[robot['pos']['x']].append(robot['pos']['y'])
        row_robots = [list(map(lambda r: r - mean(row), row)) if len(row) > 0 else [inf] for row in row_robots]
        col_robots = [list(map(lambda c: c - mean(col), col)) if len(col) > 0 else [inf] for col in col_robots]
        row_robots_std = [stdev(row_robots[i]) if len(row_robots[i]) > 2 else inf for i in range(space_y_range)]
        col_robots_std = [stdev(col_robots[i]) if len(col_robots[i]) > 2 else inf for i in range(space_x_range)]

        if len([s for s in row_robots_std if s < 10]) > 10:
            x_second = i
        if len([s for s in col_robots_std if s < 10]) > 10:
            y_second = i

        for _ in range(robots_num):
            robot = robots.pop(0)
            robot['pos']['x'] += robot['velocity']['x']
            robot['pos']['x'] %= space_x_range
            robot['pos']['y'] += robot['velocity']['y']
            robot['pos']['y'] %= space_y_range
            robots.append(robot)

    # Target second = t
    # t % space_x_range = x_second
    # t % space_y_range = y_second
    # t = space_x_range * space_y_range * k + c * space_x_range + x_second
    # k = 0, t = c * space_x_range + x_second
    result = 0
    for c in range(100):
        if (c*space_x_range+x_second)%space_y_range == y_second:
            result = c*space_x_range+x_second
            print(result)
            break
            # Print robots at after {{result}} seconds
            # robots = get_robots_data(input_string)
            # for _ in range(robots_num):
            #     robot = robots.pop(0)
            #     robot['pos']['x'] += result * robot['velocity']['x']
            #     robot['pos']['x'] %= space_x_range
            #     robot['pos']['y'] += result * robot['velocity']['y']
            #     robot['pos']['y'] %= space_y_range
            #     robots.append(robot)
            #     assert(len(robots) == robots_num)
            # spaces = [['.' for _ in range(space_x_range)] for _ in range(space_y_range)]
            # for robot in robots:
            #     spaces[robot['pos']['y']][robot['pos']['x']] = '*'
            # print('\n'.join(list(map(lambda s: ''.join(s), spaces))))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_14.txt', 'r')
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
