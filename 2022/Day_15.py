import argparse
import re


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


def part_2(input_string):
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
    # Though fast, it could output wrong answer under specific cases
    # That's why it got commented out
    # sensor_reports.sort(key=lambda s: s[0][0])
    # x, y = 0, 0
    # while x < range_max and y < range_max:
    #     if (x, y) in sensors_n_beacons:
    #         x += 1
    #         continue
    #     is_beacon = False
    #     for (sensor_x, sensor_y), reported_dist in sensor_reports:
    #         x_dist = abs(sensor_x - x)
    #         y_dist = abs(sensor_y - y)
    #         if x_dist + y_dist > reported_dist:
    #             is_beacon = True
    #             continue
    #         x = sensor_x + reported_dist - y_dist + 1
    #         is_beacon = False
    #         if x > range_max:
    #             break
    #     if is_beacon:
    #         print(x * range_max + y)
    #         return
    #     if x > range_max:
    #         x = 0
    #     y += 1
    
    # Version 2
    for (sensor_x, sensor_y), reported_dist in sensor_reports:
        intersections = [
            (sensor_x - reported_dist - 1, sensor_y),
            (sensor_x, sensor_y + reported_dist + 1),
            (sensor_x + reported_dist + 1, sensor_y),
            (sensor_x, sensor_y - reported_dist - 1)
        ]
        for i, intersection in enumerate(intersections):
            x, y = intersection
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
            
            while (x, y) != intersections[(i + 1) % 4]:
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_15.txt', 'r')
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
