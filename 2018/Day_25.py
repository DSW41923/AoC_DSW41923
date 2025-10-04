import argparse
import re


def manhatton_distance(p_0, p_1):
    return sum([abs(a - b) for a, b in zip(p_0, p_1)])


def part_1(input_string):
    points = []
    for x, y, z, w in re.findall(r"([\d-]+),([\d-]+),([\d-]+),([\d-]+)", input_string):
        x, y, z, w = tuple(map(int, (x, y, z, w)))
        points.append((x, y, z, w))

    constellations = [[points[0]]]
    points.pop(0)
    not_connected_count = 0
    while points:
        new_point = points.pop(0)
        connected = False
        for constellation in constellations:
            for point in constellation:
                if manhatton_distance(point, new_point) <= 3:
                    constellation.append(new_point)
                    connected = True
                    break
            if connected:
                break
        if not connected:
            not_connected_count += 1
            points.append(new_point)
        else:
            not_connected_count = 0
        if not_connected_count == len(points):
            constellations.append([points[0]])
            points.pop(0)
            not_connected_count = 0
    print(len(constellations))


def part_2(input_string):
    print("Merry Christmas!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_25.txt', 'r')
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
