import argparse


def get_min_alignment_fuel_cost(positions, part):
    min_position, max_position = min(positions), max(positions)
    min_fuel_cost = 0
    for position in range(min_position, max_position + 1):
        alignment_fuel_cost = 0
        if part == 1:
            alignment_fuel_cost = sum(map(lambda p: abs(position - p), positions))

        if part == 2:
            alignment_fuel_cost = sum(map(lambda p: abs(position - p) * (abs(position - p) + 1) // 2, positions))

        if min_fuel_cost == 0:
            min_fuel_cost = alignment_fuel_cost
            continue

        min_fuel_cost = min(min_fuel_cost, alignment_fuel_cost)

    return min_fuel_cost


def part_1(input_string):
    crab_positions = list(map(int, input_string.split(',')))
    print(get_min_alignment_fuel_cost(crab_positions, part=1))


def part_2(input_string):
    crab_positions = list(map(int, input_string.split(',')))
    print(get_min_alignment_fuel_cost(crab_positions, part=2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2021/Input_07.txt', 'r')
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
