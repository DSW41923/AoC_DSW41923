import argparse
import re


def part_1(input_string):
    objects = []
    orbits_map = {}
    for a, b in re.findall(r"(\w+)\)(\w+)", input_string):
        objects.extend([a, b])
        if a not in orbits_map:
            orbits_map.update({
                a: [b]
            })
            continue
        orbits_map[a].append(b)
    objects = list(set(objects))
    orbits_count = {"COM": 0}
    fronts = ["COM"]
    while len(orbits_count) < len(objects):
        cur = fronts.pop(0)
        if cur not in orbits_count: raise
        cur_step = orbits_count[cur]
        if cur in orbits_map:
            next_objects = orbits_map[cur]
            for obj in next_objects:
                orbits_count.update({obj: cur_step+1})
                fronts.append(obj)
    print(sum(list(orbits_count.values())))


def part_2(input_string):
    objects = []
    orbits_map = {}
    for a, b in re.findall(r"(\w+)\)(\w+)", input_string):
        objects.extend([a, b])
        if a not in orbits_map:
            orbits_map.update({
                a: [b]
            })
            continue
        orbits_map[a].append(b)
    objects = list(set(objects))
    orbits_count = {"COM": 0}
    paths = [["COM"]]
    you_path = None
    san_path = None
    while len(orbits_count) < len(objects):
        cur_path = paths.pop(0)
        cur = cur_path[-1]
        if cur == "YOU":
            you_path = cur_path
        if cur == "SAN":
            san_path = cur_path
        if cur not in orbits_count: raise
        cur_step = orbits_count[cur]
        if cur in orbits_map:
            next_objects = orbits_map[cur]
            for obj in next_objects:
                orbits_count.update({obj: cur_step+1})
                paths.append(cur_path+[obj])
    last_common = None
    for a, b in zip(you_path, san_path):
        if a == b:
            last_common = a
        else:
            break
    print((orbits_count["YOU"]-orbits_count[last_common])+(orbits_count["SAN"]-orbits_count[last_common]) - 2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_06.txt', 'r')
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
