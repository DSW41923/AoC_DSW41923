import argparse


def part_1(instructions, start=5):
    current = start
    codes = []
    for instruction in instructions:
        moves = list(instruction)
        for move in moves:
            if move == 'U':
                if current > 3:
                    current -= 3
            elif move == 'D':
                if current < 7:
                    current += 3
            elif move == 'R':
                if current % 3 > 0:
                    current += 1
            elif move == 'L':
                if current % 3 != 1:
                    current -= 1
        codes.append(str(current))
    print("Bathroom code is {}".format(''.join(codes)))


def part_2(instructions):
    current = 5
    codes = []
    for instruction in instructions:
        moves = list(instruction)
        for move in moves:
            if move == 'U':
                if current in [3, 13]:
                    current -= 2
                elif current not in [1, 2, 4 ,5, 9]:
                    current -= 4
            elif move == 'D':
                if current in [1, 11]:
                    current += 2
                elif current not in [5, 9, 10, 12, 13]:
                    current += 4
            elif move == 'R':
                if current not in [1, 4, 9, 12, 13]:
                    current += 1
            elif move == 'L':
                if current not in [1, 2, 5, 10, 13]:
                    current -= 1
        codes.append(hex(current)[-1].upper())
    print("Bathroom code is actually {}".format(''.join(codes)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_02.txt', 'r')
    instructions = file_input.readlines()
    file_input.close()

    if args.part == '1':
        part_1(instructions)
    elif args.part == '2':
        part_2(instructions)
    else:
        part_1(instructions)
        part_2(instructions)


if __name__ == "__main__":
    main()
