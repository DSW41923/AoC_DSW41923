import argparse

from collections import Counter


def get_cave_map(input_string):
    cave_connections = input_string.split('\n')
    cave_map = {}
    for connection in cave_connections:
        cave_0, cave_1 = connection.split('-')
        if cave_0 != 'end' and cave_1 != 'start':
            cave_map.update({cave_0: cave_map.get(cave_0, []) + [cave_1]})
        if cave_0 != 'start' and cave_1 != 'end':
            cave_map.update({cave_1: cave_map.get(cave_1, []) + [cave_0]})

    return cave_map


def part_1(input_string):
    cave_map = get_cave_map(input_string)
    paths = ['start']
    while not all(path.endswith('end') for path in paths):
        unended_paths = [path for path in paths if not path.endswith('end')]
        new_paths = []
        for path in unended_paths:
            next_caves = cave_map[path.split(',')[-1]]
            for cave in next_caves:
                if cave.lower() == cave and cave in path:
                    continue
                new_paths.append(path + ',' + cave)
        paths = [path for path in paths if path.endswith('end')] + new_paths

    print(len(paths))


def part_2(input_string):
    cave_map = get_cave_map(input_string)
    paths_count = 0
    paths = ['start']
    while paths:
        new_paths = []
        for path in paths:
            visited_caves = path.split(',')
            next_caves = cave_map[visited_caves[-1]]
            for cave in next_caves:
                if cave == 'end':
                    paths_count += 1
                    continue

                if cave.lower() == cave:
                    cave_visited_count = Counter(visited_caves)
                    if cave_visited_count.get(cave) == 2:
                        continue

                    if any(cv == 2 for ck, cv in cave_visited_count.items() if ck.lower() == ck)\
                            and cave_visited_count.get(cave) == 1:
                        continue

                new_paths.append(path + ',' + cave)

        paths = new_paths

    print(paths_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2021/Input_12.txt', 'r')
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
