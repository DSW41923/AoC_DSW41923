import argparse


def part_1(input_string):
    digits = list(input_string)
    result = 0
    for i in range(-1, len(digits) - 1):
        if digits[i] == digits[i + 1]:
            result += int(digits[i])
    print(result)


def part_2(input_string):
    digits = list(input_string)
    result = 0
    for i in range(-len(digits) // 2, len(digits) // 2 - 1):
        if digits[i] == digits[i + len(digits) // 2]:
            result += int(digits[i])
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_01.txt', 'r')
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
