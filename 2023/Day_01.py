import argparse
import re


def part_1(input_string):
    lines = input_string.split('\n')
    result = 0
    for line in lines:
        number_chars = [c for c in list(line) if c.isdigit()]
        result += int(number_chars[0]) * 10 + int(number_chars[-1])
    print(result)


def part_2(input_string):
    lines = input_string.split('\n')
    result = 0
    for line in lines:
        number_chars = []
        letter_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        for i, letter_number in enumerate(letter_numbers):
            letter_number_index = [g.span()[0] for g in list(re.finditer(letter_number, line))]
            for index in letter_number_index:
                number_chars.append((index, i+1))
        digit_index = [g.span()[0] for g in list(re.finditer(r"\d", line))]
        for index in digit_index:
            number_chars.append((index, int(line[index])))
        number_chars = sorted(number_chars, key=lambda x:x[0])
        result += number_chars[0][1] * 10 + number_chars[-1][1]
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2023/Input_01.txt', 'r')
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
