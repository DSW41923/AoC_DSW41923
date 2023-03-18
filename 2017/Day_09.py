import argparse


def part_1(input_string):
    total_score = 1
    score = 1
    groups_string = input_string[1:-1]
    is_grabage = False
    omit_next = False
    for char in groups_string:
        if omit_next:
            omit_next = False
            continue

        if is_grabage:
            if char == "!":
                omit_next = True
            if char == ">":
                is_grabage = False
            continue

        if char == "<":
            is_grabage = True
            continue

        if char == "{":
            score += 1
        elif char == "}" and score > 1:
            total_score += score
            score -= 1
    print(total_score)


def part_2(input_string):
    garbage_count = 0
    is_grabage = False
    omit_next = False
    for char in input_string:
        if omit_next:
            omit_next = False
            continue

        if is_grabage:
            if char == "!":
                omit_next = True
                continue
            if char == ">":
                is_grabage = False
                continue
            garbage_count += 1
            continue

        if char == "<":
            is_grabage = True
            continue

    print(garbage_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_09.txt', 'r')
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
