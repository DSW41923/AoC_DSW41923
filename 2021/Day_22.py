import argparse
import numpy as np
import re

from itertools import product


def part_1(input_string):
    range_radius = 50
    cube_states = np.array([
        [[0 for _ in range(range_radius * 2 + 1)] for _ in range(range_radius * 2 + 1)]
        for _ in range(range_radius * 2 + 1)])
    for step in input_string.splitlines():
        action, ranges = tuple(step.split(' '))
        new_x_min, new_x_max = map(int, re.search(r'x=([-\d]+)..([-\d]+)', ranges).groups())
        new_y_min, new_y_max = map(int, re.search(r'y=([-\d]+)..([-\d]+)', ranges).groups())
        new_z_min, new_z_max = map(int, re.search(r'z=([-\d]+)..([-\d]+)', ranges).groups())
        if new_x_min > new_x_max or new_y_min > new_y_max or new_z_min > new_z_max:
            raise

        if new_x_max < -range_radius or new_y_max < -range_radius or new_z_max < -range_radius or \
                new_x_min > range_radius or new_y_min > range_radius or new_z_min > range_radius:
            continue

        x_range = range(max(-range_radius, new_x_min), min(range_radius, new_x_max) + 1)
        y_range = range(max(-range_radius, new_y_min), min(range_radius, new_y_max) + 1)
        z_range = range(max(-range_radius, new_z_min), min(range_radius, new_z_max) + 1)
        for x, y, z in product(x_range, y_range, z_range):
            if action == 'on':
                cube_states[x][y][z] = 1

            if action == 'off':
                cube_states[x][y][z] = 0

    print(np.sum(cube_states))


def part_2(input_string):
    cubes = []
    for step in input_string.splitlines():
        action, ranges = tuple(step.split(' '))
        new_x = tuple(map(int, re.search(r'x=([-\d]+)..([-\d]+)', ranges).groups()))
        new_y = tuple(map(int, re.search(r'y=([-\d]+)..([-\d]+)', ranges).groups()))
        new_z = tuple(map(int, re.search(r'z=([-\d]+)..([-\d]+)', ranges).groups()))
        new_cubes = []
        for cube in cubes:
            if new_x[0] > cube['x'][1] or new_x[1] < cube['x'][0] \
                    or new_y[0] > cube['y'][1] or new_y[1] < cube['y'][0] \
                    or new_z[0] > cube['z'][1] or new_z[1] < cube['z'][0]:
                new_cubes.append(cube)
                continue
            intersect_x = (max(new_x[0], cube['x'][0]), min(new_x[1], cube['x'][1]))
            intersect_y = (max(new_y[0], cube['y'][0]), min(new_y[1], cube['y'][1]))
            intersect_z = (max(new_z[0], cube['z'][0]), min(new_z[1], cube['z'][1]))
            x_split = [(cube['x'][0], intersect_x[0] - 1),
                       (intersect_x[0], intersect_x[1]),
                       (intersect_x[1] + 1, cube['x'][1])]
            y_split = [(cube['y'][0], intersect_y[0] - 1),
                       (intersect_y[0], intersect_y[1]),
                       (intersect_y[1] + 1, cube['y'][1])]
            z_split = [(cube['z'][0], intersect_z[0] - 1),
                       (intersect_z[0], intersect_z[1]),
                       (intersect_z[1] + 1, cube['z'][1])]
            splitted_cubes = product(x_split, y_split, z_split)
            for x, y, z in splitted_cubes:
                if x[0] > x[1] or y[0] > y[1] or z[0] > z[1]:
                    continue

                if x == x_split[1] and y == y_split[1] and z == z_split[1]:
                    continue

                new_cubes.append({
                    'x': x,
                    'y': y,
                    'z': z,
                })

        if action == 'on':
            new_cubes.append({
                'x': new_x,
                'y': new_y,
                'z': new_z,
            })

        if action == 'off':
            pass

        cubes = new_cubes

    on_cube_count = 0
    for cube in cubes:
        on_cube_count += ((cube['x'][1] - cube['x'][0] + 1) *
                          (cube['y'][1] - cube['y'][0] + 1) *
                          (cube['z'][1] - cube['z'][0] + 1))

    print(on_cube_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_22.txt', 'r')
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
