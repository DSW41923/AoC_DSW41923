import argparse


def part_1(input_string):
    instructions = list(map(int, input_string.split('\n')))
    cur = 0
    steps = 0
    while 0 <= cur < len(instructions):
        new_cur = cur + instructions[cur]
        instructions[cur] += 1
        cur = new_cur
        steps += 1
    print(steps)


def part_2(input_string):
    instructions = list(map(int, input_string.split('\n')))
    cur = 0
    steps = 0
    while 0 <= cur < len(instructions):
        new_cur = cur + instructions[cur]
        if instructions[cur] >= 3:
            instructions[cur] -= 1
        else:
            instructions[cur] += 1
        cur = new_cur
        steps += 1
    print(steps)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2017/Input_05.txt', 'r')
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
