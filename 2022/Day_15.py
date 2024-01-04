import argparse
import re
import time

from collections import Counter
from itertools import product


def part_1(input_string):
    xs = [int(x) for x in re.findall(r'x=(\d+)', input_string)]
    arrangement = {x: '.' for x in range(min(xs), max(xs) + 1)}
    target_y = 2000000
    for sensor_x_str, sensor_y_str, beacon_x_str, beacon_y_str in re.findall(r'Sensor[\w ]+x=(\d+), y=([-\d]+): closest beacon[\w ]+x=(\d+), y=([-\d]+)', input_string):
        sensor_x, sensor_y, beacon_x, beacon_y = tuple(map(int, (sensor_x_str, sensor_y_str, beacon_x_str, beacon_y_str)))

        if sensor_y == target_y:
            arrangement.update({sensor_x: 'S'})
        if beacon_y == target_y:
            arrangement.update({beacon_x: 'B'})

        dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        y_dist = abs(target_y - sensor_y)
        x_range = dist - y_dist
        for x in range(sensor_x - x_range, sensor_x + x_range + 1):
            if arrangement.get(x, '.') == '.':
                arrangement.update({x: '#'})
                continue
    print(list(arrangement.values()).count('#'))


def part_2(input_string, method=4):
    sensor_reports = []
    sensors_n_beacons = []
    range_min, range_max = 0, 4000000

    for found in re.findall(r'Sensor[\w ]+x=(\d+), y=([-\d]+): closest beacon[\w ]+x=(\d+), y=([-\d]+)', input_string):
        sensor_x, sensor_y, beacon_x, beacon_y = tuple(map(int, found))
        sensor_reports.append(((sensor_x, sensor_y), abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)))
        sensors_n_beacons.extend([(sensor_x, sensor_y), (beacon_x, beacon_y)])

    sensors_n_beacons = list(set(sensors_n_beacons))

    # Version 1
    # Got correct answer after compared with Version 2
    # Actually works
    # Performance: 8.6 seconds
    if method == 1:
        sensor_reports.sort(key=lambda s: s[0][0])
        x, y = 0, 0
        while x < range_max and y < range_max:
            if (x, y) in sensors_n_beacons:
                x += 1
                continue
            is_beacon = False
            for (sensor_x, sensor_y), reported_dist in sensor_reports:
                x_dist = abs(sensor_x - x)
                y_dist = abs(sensor_y - y)
                if x_dist + y_dist > reported_dist:
                    is_beacon = True
                    continue
                x = sensor_x + reported_dist - y_dist + 1
                is_beacon = False
                if x > range_max:
                    break
            if is_beacon:
                print(x * range_max + y)
                return
            if x > range_max:
                x = 0
            y += 1

    # Version 2
    # Performance: 32 seconds
    if method == 2:
        for (sensor_x, sensor_y), reported_dist in sensor_reports:
            outer_endpoints = [
                (sensor_x - reported_dist - 1, sensor_y),
                (sensor_x, sensor_y + reported_dist + 1),
                (sensor_x + reported_dist + 1, sensor_y),
                (sensor_x, sensor_y - reported_dist - 1)
            ]
            for i, endpoint in enumerate(outer_endpoints):
                x, y = endpoint
                if i == 0:
                    while x < range_min or y < range_min:
                        x += 1
                        y += 1
                if i == 1:
                    while x < range_min or y > range_max:
                        x += 1
                        y -= 1
                if i == 2:
                    while x > range_max or y > range_max:
                        x -= 1
                        y -= 1
                if i == 3:
                    while x > range_max or y < range_min:
                        x -= 1
                        y += 1

                if not(range_min <= x <= range_max and range_min <= y <= range_max):
                    continue

                while (x, y) != outer_endpoints[(i + 1) % 4]:
                    if all([abs(sensor_x - x) + abs(sensor_y - y) > dist for (sensor_x, sensor_y), dist in sensor_reports]):
                        print(x * range_max + y)
                        return

                    if i == 0:
                        x += 1
                        y += 1
                    if i == 1:
                        x += 1
                        y -= 1
                    if i == 2:
                        x -= 1
                        y -= 1
                    if i == 3:
                        x -= 1
                        y += 1

                    if not(range_min <= x <= range_max and range_min <= y <= range_max):
                        break

    # Version 3
    # Performance: 26 seconds
    if method == 3:
        candidates = []
        for (sensor_x, sensor_y), reported_dist in sensor_reports:
            outer_endpoints = [
                (sensor_x - reported_dist - 1, sensor_y),
                (sensor_x, sensor_y + reported_dist + 1),
                (sensor_x + reported_dist + 1, sensor_y),
                (sensor_x, sensor_y - reported_dist - 1)
            ]
            for x, y in zip(
                range(outer_endpoints[0][0], outer_endpoints[1][0] + 1),
                range(outer_endpoints[0][1], outer_endpoints[1][1] + 1)):
                if range_min <= x <= range_max and range_min <= y <= range_max:
                    candidates.append((x, y))
            for x, y in zip(
                range(outer_endpoints[1][0], outer_endpoints[2][0] + 1),
                range(outer_endpoints[1][1], outer_endpoints[2][1] - 1, -1)):
                if range_min <= x <= range_max and range_min <= y <= range_max:
                    candidates.append((x, y))
            for x, y in zip(
                range(outer_endpoints[2][0], outer_endpoints[3][0] - 1, -1),
                range(outer_endpoints[2][1], outer_endpoints[3][1] - 1, -1)):
                if range_min <= x <= range_max and range_min <= y <= range_max:
                    candidates.append((x, y))
            for x, y in zip(
                range(outer_endpoints[3][0], outer_endpoints[0][0] - 1, -1),
                range(outer_endpoints[3][1], outer_endpoints[0][1] + 1, 1)):
                if range_min <= x <= range_max and range_min <= y <= range_max:
                    candidates.append((x, y))

        for x, y in candidates:
            is_beacon = False
            for (sensor_x, sensor_y), reported_dist in sensor_reports:
                if abs(sensor_x - x) + abs(sensor_y - y) > reported_dist:
                    is_beacon = True
                    continue
                is_beacon = False
                break
            if is_beacon:
                print(range_max * x + y)
                return

    # Version 4
    # Performance: 0.0007 seconds
    if method == 4:
        all_plus_lines = []
        all_minus_lines = []
        for (sensor_x, sensor_y), reported_dist in sensor_reports:
            outer_endpoints = [
                (sensor_x - reported_dist - 1, sensor_y),
                (sensor_x, sensor_y + reported_dist + 1),
                (sensor_x + reported_dist + 1, sensor_y),
                (sensor_x, sensor_y - reported_dist - 1)
            ]
            for x, y in outer_endpoints:
                if x + y not in all_plus_lines:
                    all_plus_lines.append(x + y)
                if x - y not in all_minus_lines:
                    all_minus_lines.append(x - y)

        for k_0, k_1 in product(all_plus_lines, all_minus_lines):
            if (k_0 + k_1) % 2 or (k_0 - k_1) % 2:
                continue
            x, y = (k_0 + k_1) // 2, (k_0 - k_1) // 2
            if not(range_min <= x <= range_max and range_min <= y <= range_max):
                continue

            is_beacon = False
            for (sensor_x, sensor_y), reported_dist in sensor_reports:
                if abs(sensor_x - x) + abs(sensor_y - y) > reported_dist:
                    is_beacon = True
                    continue
                is_beacon = False
                break
            if is_beacon:
                print(range_max * x + y)
                return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2022/Input_15.txt', 'r')
    input_string = file_input.read()
    file_input.close()

    if args.part == '1':
        part_1(input_string)
    elif args.part == '2':
        part_2(input_string)
    else:
        part_1(input_string)
        part_2(input_string, 4)

        # start = time.perf_counter()
        # part_2(input_string, 1)
        # end = time.perf_counter()
        # print("Method 1 執行時間：%f 秒" % (end - start))

        # start = time.perf_counter()
        # part_2(input_string, 2)
        # end = time.perf_counter()
        # print("Method 2 執行時間：%f 秒" % (end - start))

        # start = time.perf_counter()
        # part_2(input_string, 3)
        # end = time.perf_counter()
        # print("Method 3 執行時間：%f 秒" % (end - start))

        # start = time.perf_counter()
        # part_2(input_string, 4)
        # end = time.perf_counter()
        # print("Method 4 執行時間：%f 秒" % (end - start))

if __name__ == "__main__":
    main()
