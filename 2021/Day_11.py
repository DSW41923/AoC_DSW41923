import argparse
import copy
import itertools


def get_adjacent(x, y):
    return itertools.product(list(range(max(0, x-1), min(10, x+2))), list(range(max(0, y-1), min(10, y+2))))


def get_flashing_result(octupus_energy):
    flashing_octupus = []
    new_octupus_energy = []
    while new_octupus_energy != octupus_energy:
        if len(new_octupus_energy) == 0:
            new_octupus_energy = copy.deepcopy(octupus_energy)
        else:
            octupus_energy = copy.deepcopy(new_octupus_energy)

        for i in range(len(new_octupus_energy)):
            for j in range(len(new_octupus_energy[i])):
                if new_octupus_energy[i][j] > 9 and (i, j) not in flashing_octupus:
                    flashing_octupus.append((i, j))
                    adjacent_octupus = get_adjacent(i, j)
                    for x, y in adjacent_octupus:
                        new_octupus_energy[x][y] += 1

    return new_octupus_energy, flashing_octupus


def part_1(input_string):
    octupus_energy = [list(map(int, line)) for line in list(map(list, input_string.split('\n')))]
    steps = 100
    flashed_octupus_count = 0
    for _ in range(steps):
        octupus_energy = [list(e + 1 for e in er) for er in octupus_energy]
        octupus_energy, flashing_octupus = get_flashing_result(octupus_energy)
        for i, j in flashing_octupus:
            octupus_energy[i][j] = 0
        flashed_octupus_count += len(flashing_octupus)

    print(flashed_octupus_count)


def part_2(input_string):
    octupus_energy = [list(map(int, line)) for line in list(map(list, input_string.split('\n')))]
    steps = 0
    while not all(all(e == 0 for e in er) for er in octupus_energy):
        steps += 1
        octupus_energy = [list(e + 1 for e in er) for er in octupus_energy]
        octupus_energy, flashing_octupus = get_flashing_result(octupus_energy)
        for i, j in flashing_octupus:
            octupus_energy[i][j] = 0

    print(steps)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2021/Input_11.txt', 'r')
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
