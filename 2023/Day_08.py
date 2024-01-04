import argparse
import re

from math import gcd


def part_1(input_string):
    instructions = list(input_string.split('\n')[0])
    maps = {}
    for node, left_node, right_node in re.findall(r"(\w{3}) = \((\w{3}), (\w{3})\)", input_string):
        maps.update({node: {'L': left_node, 'R': right_node}})
    steps = 0
    cur = 'AAA'
    while cur != 'ZZZ':
        cur = maps[cur][instructions[steps % len(instructions)]]
        steps += 1
    print(steps)


def part_2(input_string):
    instructions = list(input_string.split('\n')[0])
    maps = {}
    curs = []
    for node, left_node, right_node in re.findall(r"(\w{3}) = \((\w{3}), (\w{3})\)", input_string):
        maps.update({node: {'L': left_node, 'R': right_node}})
        if node.endswith('A'):
            curs.append(node)

    paths_steps = []
    for cur in curs:
        steps = 0
        first_z_steps = 0
        visited_z = 0
        path = [cur]
        while visited_z != 2 or not path[-1].endswith('Z'):
            cur = maps[cur][instructions[steps % len(instructions)]]
            steps += 1
            if cur.endswith('Z'):
                visited_z += 1
                if visited_z == 1:
                    first_z_steps = steps
            path.append(cur)
        paths_steps.append(steps - first_z_steps)

    while len(paths_steps) > 1:
        s0 = paths_steps.pop(0)
        s1 = paths_steps.pop(0)
        paths_steps.append(s0*s1//gcd(s0, s1))

    print(paths_steps[0])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2023/Input_08.txt', 'r')
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
