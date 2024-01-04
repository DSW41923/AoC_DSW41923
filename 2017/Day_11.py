import argparse


def part_1(input_string):
    steps = input_string.split(',')
    pos = (0, 0)
    for step in steps:
        if step == 'n':
            pos = (pos[0] - 1, pos[1] + 2)
        if step == 's':
            pos = (pos[0] + 1, pos[1] - 2)
        if step == 'ne':
            pos = (pos[0] + 1, pos[1] + 1)
        if step == 'se':
            pos = (pos[0] + 2, pos[1] - 1)
        if step == 'nw':
            pos = (pos[0] - 2, pos[1] + 1)
        if step == 'sw':
            pos = (pos[0] - 1, pos[1] - 1)
    min_steps = min(abs((pos[0] - pos[1]) // -3) + abs((-2 * pos[0] - pos[1]) // -3),
                    abs((-pos[0] - 2 * pos[1]) // -3) + abs((-pos[0] + pos[1]) // -3),
                    abs((-2 * pos[0] - pos[1]) // -3) + abs((pos[0] + 2 * pos[1]) // -3))
    print(min_steps)

def part_2(input_string):
    steps = input_string.split(',')
    pos = (0, 0)
    furthest_steps = 0
    for step in steps:
        if step == 'n':
            pos = (pos[0] - 1, pos[1] + 2)
        if step == 's':
            pos = (pos[0] + 1, pos[1] - 2)
        if step == 'ne':
            pos = (pos[0] + 1, pos[1] + 1)
        if step == 'se':
            pos = (pos[0] + 2, pos[1] - 1)
        if step == 'nw':
            pos = (pos[0] - 2, pos[1] + 1)
        if step == 'sw':
            pos = (pos[0] - 1, pos[1] - 1)
        min_steps = min(abs((pos[0] - pos[1]) // -3) + abs((-2 * pos[0] - pos[1]) // -3),
                       abs((-pos[0] - 2 * pos[1]) // -3) + abs((-pos[0] + pos[1]) // -3),
                       abs((-2 * pos[0] - pos[1]) // -3) + abs((pos[0] + 2 * pos[1]) // -3))
        furthest_steps = max(furthest_steps, min_steps)
    print(furthest_steps)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2017/Input_11.txt', 'r')
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
