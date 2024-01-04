import argparse
import copy
import itertools
import re


FACING = [(1, 1, 1), (-1, 1, -1), (1, -1, -1), (-1, -1, 1)]


def get_pos(data):
    scanned_scanner = [0]
    scanners_pos = [(0, 0, 0)]
    beacons_pos = copy.deepcopy(data[0])
    while len(scanned_scanner) < len(data) - 1:
        for s in range(1, len(data)):
            if s in scanned_scanner:
                continue

            scanner_pos = None
            trial_data = copy.deepcopy(data[s])

            for i in range(24):
                facing = FACING[i % 4]
                new_facing_data = [(x * facing[0], y * facing[1], z * facing[2]) for x, y, z in trial_data]
                for x, y, z in new_facing_data:
                    if not scanner_pos:
                        trial_delta_vec = [(x_0 - x, y_0 - y, z_0 - z) for x_0, y_0, z_0 in beacons_pos]
                        for vec_x, vec_y, vec_z in trial_delta_vec:
                            new_beacons_pos = [
                                (x_1 + vec_x, y_1 + vec_y, z_1 + vec_z) for x_1, y_1, z_1 in new_facing_data]
                            interleaving_count = len(set(beacons_pos) & set(new_beacons_pos))
                            if interleaving_count >= 12:
                                scanner_pos = (vec_x, vec_y, vec_z)
                                beacons_pos.extend(list(set(new_beacons_pos) - set(beacons_pos)))
                                break

                if scanner_pos:
                    scanners_pos.append(scanner_pos)
                    scanned_scanner.append(s)
                    break

                if i == 11:
                    trial_data = [(-y, x, z) for x, y, z in trial_data]
                    continue

                if i % 4 == 3:
                    trial_data = [(y, z, x) for x, y, z in trial_data]

    return scanners_pos, beacons_pos


def parse_data(input_string):
    scanners_data = []
    for scanner_data in input_string.split('\n\n'):
        new_data = []
        for x, y, z in re.findall(r'([-\d]+),([-\d]+),([-\d]+)', scanner_data):
            new_data.append((int(x), int(y), int(z)))
        scanners_data.append(new_data)

    return scanners_data


def get_manhatton_distance(p_0, p_1):
    return sum([abs(a - b) for a, b in zip(p_0, p_1)])


def part_1(input_string):
    scanners_data = parse_data(input_string)
    scanners_pos, beacons_pos = get_pos(scanners_data)
    print(len(beacons_pos))


def part_2(input_string):
    scanners_data = parse_data(input_string)
    scanners_pos, beacons_pos = get_pos(scanners_data)
    max_two_scanner_dist = 0
    for scanner_0_pos, scanner_1_pos in itertools.combinations(scanners_pos, 2):
        scanner_dist = get_manhatton_distance(scanner_0_pos, scanner_1_pos)
        max_two_scanner_dist = max(max_two_scanner_dist, scanner_dist)

    print(max_two_scanner_dist)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2021/Input_19.txt', 'r')
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
