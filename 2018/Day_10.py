import argparse
import re

from collections import namedtuple


def part_1(input_string):
    Position = namedtuple('Position', 'x, y')
    Velocity = namedtuple('Velocity', 'x, y')
    Point = namedtuple('Point', 'pos, vel')
    points = []
    for pos_x, pos_y, v_x, v_y in re.findall(r"position=<( ?\-?\d+), ( ?\-?\d+)> velocity=<( ?\-?\d+), ( ?\-?\d+)>", input_string):
        pos_x, pos_y, v_x, v_y = tuple(map(int, (pos_x, pos_y, v_x, v_y)))
        points.append(Point(Position(pos_x, pos_y), Velocity(v_x, v_y)))

    while max([point.pos.y for point in points]) - min([point.pos.y for point in points]) >= 10:
        new_points = []
        for point in points:
            new_points.append(Point(Position(point.pos.x+point.vel.x, point.pos.y+point.vel.y), Velocity(point.vel.x, point.vel.y)))
        points = new_points

    points_pos = [(point.pos.x, point.pos.y) for point in points]
    xs = [point.pos.x for point in points]
    ys = [point.pos.y for point in points]
    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)
    for y in range(min_y-1, max_y+2):
        for x in range(min_x-1, max_x+2):
            if (x, y) in points_pos:
                print('#', end='')
            else:
                print('.', end='')
        print()


def part_2(input_string):
    Position = namedtuple('Position', 'x, y')
    Velocity = namedtuple('Velocity', 'x, y')
    Point = namedtuple('Point', 'pos, vel')
    points = []
    for pos_x, pos_y, v_x, v_y in re.findall(r"position=<( ?\-?\d+), ( ?\-?\d+)> velocity=<( ?\-?\d+), ( ?\-?\d+)>", input_string):
        pos_x, pos_y, v_x, v_y = tuple(map(int, (pos_x, pos_y, v_x, v_y)))
        points.append(Point(Position(pos_x, pos_y), Velocity(v_x, v_y)))

    result = 0
    while max([point.pos.y for point in points]) - min([point.pos.y for point in points]) >= 10:
        new_points = []
        for point in points:
            new_points.append(Point(Position(point.pos.x+point.vel.x, point.pos.y+point.vel.y), Velocity(point.vel.x, point.vel.y)))
        points = new_points
        result += 1
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_10.txt', 'r')
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
