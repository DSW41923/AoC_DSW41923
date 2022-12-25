import argparse


def is_adjacent(cube, other_cube):
    return (abs(other_cube[0] - cube[0]) == 1 and other_cube[1] == cube[1] and other_cube[2] == cube[2]) or \
            (abs(other_cube[1] - cube[1]) == 1 and other_cube[2] == cube[2] and other_cube[0] == cube[0]) or \
            (abs(other_cube[2] - cube[2]) == 1 and other_cube[0] == cube[0] and other_cube[1] == cube[1])


def get_neighbor_cubes(x, y, z):
    return [(x - 1, y, z), (x + 1, y, z),
            (x, y - 1, z), (x, y + 1, z),
            (x, y, z - 1), (x, y, z + 1)]


def part_1(input_string):
    cubes_data = input_string.split('\n')[:-1]
    cubes = []
    surface_area = 0
    for cd in cubes_data:
        cube = tuple(map(int, cd.split(',')))
        surface_area += 6
        for other_cube in cubes:
            if is_adjacent(cube, other_cube):
                surface_area -= 2
        cubes.append(cube)
    print(surface_area)


def part_2(input_string):
    cubes_data = input_string.split('\n')[:-1]
    cubes = []
    exterior_surface_area = 0
    for cd in cubes_data:
        cube = tuple(map(int, cd.split(',')))
        exterior_surface_area += 6
        for other_cube in cubes:
            if is_adjacent(cube, other_cube):
                exterior_surface_area -= 2
        cubes.append(cube)
    x_min, x_max = min([c[0] for c in cubes]), max([c[0] for c in cubes])
    y_min, y_max = min([c[1] for c in cubes]), max([c[1] for c in cubes])
    z_min, z_max = min([c[2] for c in cubes]), max([c[2] for c in cubes])
    x_range = range(x_min - 1, x_max + 2)
    y_range = range(y_min - 1, y_max + 2)
    z_range = range(z_min - 1, z_max + 2)
    outside_cubes = [(x_min - 1, y_min - 1, z_min - 1)]
    front_cubes = [(x_min - 1, y_min - 1, z_min - 1)]
    while front_cubes:
        new_front_cubes = []
        for cube in front_cubes:
            cube_x, cube_y, cube_z = cube
            neighbor_cubes = get_neighbor_cubes(cube_x, cube_y, cube_z)
            for x, y, z in neighbor_cubes:
                if x in x_range and y in y_range and z in z_range:
                    if (x, y, z) not in cubes + outside_cubes + new_front_cubes:
                        outside_cubes.append((x, y, z))
                        new_front_cubes.append((x, y, z))
        front_cubes = new_front_cubes
    for x in x_range:
        for y in y_range:
            for z in z_range:
                if (x, y, z) not in cubes + outside_cubes:
                    neighbor_cubes = get_neighbor_cubes(x, y, z)
                    for neighbor_cube in neighbor_cubes:
                        if neighbor_cube in cubes:
                            exterior_surface_area -= 1  
    print(exterior_surface_area)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_18.txt', 'r')
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

