import argparse
import re


def traverse_wire(wire):
    wire_points = []
    directions = {'U': 1j, 'L': -1, 'R': 1, 'D': -1j}
    cur = 0
    for dir, dis in re.findall(r"([ULDR])(\d+)", wire):
        dis = int(dis)
        for _ in range(dis):
            cur += directions[dir]
            wire_points.append(cur)
    return wire_points


def part_1(input_string):
    wire_0, wire_1 = input_string.split('\n')
    wire_0_points = set(traverse_wire(wire_0))
    wire_1_points = set(traverse_wire(wire_1))
    intersects = list(wire_0_points.intersection(wire_1_points))
    print(min([int(abs(c.real)+abs(c.imag)) for c in intersects]))


def part_2(input_string):
    wire_0, wire_1 = input_string.split('\n')
    wire_0_points = traverse_wire(wire_0)
    wire_1_points = traverse_wire(wire_1)
    intersects = list(set(wire_0_points).intersection(set(wire_1_points)))
    print(min([int(2+wire_0_points.index(c)+wire_1_points.index(c)) for c in intersects]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_03.txt', 'r')
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
