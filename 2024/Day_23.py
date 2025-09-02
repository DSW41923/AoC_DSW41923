import argparse
import re

from itertools import combinations


def get_connections_data(input_string):
    connections = {}
    for computer_0, computer_1 in re.findall(r"(\w+)\-(\w+)", input_string):
        if computer_0 not in connections:
            connections[computer_0] = []
        if computer_1 not in connections:
            connections[computer_1] = []
        connections[computer_0].append(computer_1)
        connections[computer_1].append(computer_0)
    return connections


def part_1(input_string):
    connections = get_connections_data(input_string)
    result = 0
    for c0, c1, c2 in combinations(connections.keys(), 3):
        if c0 in connections[c1] and c1 in connections[c2] and c2 in connections[c0]:
            if any([c.startswith('t') for c in (c0, c1, c2)]):
                result += 1
    print(result)


def part_2(input_string):
    connections = get_connections_data(input_string)
    interconnected = []
    for c0, c1, c2 in combinations(connections.keys(), 3):
        if c0 in connections[c1] and c1 in connections[c2] and c2 in connections[c0]:
            interconnected.append((c0, c1, c2))
    full_interconnections = set()
    for c0, c1, c2 in interconnected:
        if any([c0 in c and c1 in c and c2 in c for c in full_interconnections]):
            continue
        interconnections = set([(c0, c1, c2)])
        while interconnections:
            icc = interconnections.pop()
            interconnected_candidates = set(connections[icc[0]])
            for c in icc[1:]:
                interconnected_candidates = interconnected_candidates.intersection(set(connections[c]))
            if len(interconnected_candidates) == 0:
                full_interconnections.add(icc)
            for c in interconnected_candidates:
                new_icc = tuple(list(icc)+[c])
                if not any([set(new_icc).issubset(ic) for ic in interconnections]):
                    interconnections.add(new_icc)
    full_interconnections = list(full_interconnections)
    full_interconnections.sort(key=lambda i: len(i), reverse=True)
    full_interconnection_computers = list(full_interconnections[0])
    full_interconnection_computers.sort()
    print(','.join(full_interconnection_computers))



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_23.txt', 'r')
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
