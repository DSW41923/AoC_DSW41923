import argparse


def part_1(input_string):
    rounds = input_string.split("\n")[:-1]
    score = 0
    for foe, me in map(lambda x: x.split(" "), rounds):
        if me == 'X':
            score += 1
            if foe == 'A':
                score += 3
                continue
            if foe == 'B':
                score += 0
                continue
            if foe == 'C':
                score += 6
                continue
            raise
        if me == 'Y':
            score += 2
            if foe == 'A':
                score += 6
                continue
            if foe == 'B':
                score += 3
                continue
            if foe == 'C':
                score += 0
                continue
        if me == 'Z':
            score += 3
            if foe == 'A':
                score += 0
                continue
            if foe == 'B':
                score += 6
                continue
            if foe == 'C':
                score += 3
                continue
        raise
    print(score)


def part_2(input_string):
    
    rounds = input_string.split("\n")[:-1]
    score = 0
    for foe, me in map(lambda x: x.split(" "), rounds):
        if me == 'X':
            score += 0
            if foe == 'A':
                score += 3
                continue
            if foe == 'B':
                score += 1
                continue
            if foe == 'C':
                score += 2
                continue
            raise
        if me == 'Y':
            score += 3
            if foe == 'A':
                score += 1
                continue
            if foe == 'B':
                score += 2
                continue
            if foe == 'C':
                score += 3
                continue
        if me == 'Z':
            score += 6
            if foe == 'A':
                score += 2
                continue
            if foe == 'B':
                score += 3
                continue
            if foe == 'C':
                score += 1
                continue
        raise
    print(score)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_02.txt', 'r')
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
