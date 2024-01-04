import argparse
import re


def part_1(input_string):
    rows = input_string.split('\n')
    result = 0
    for row in rows:
        numbers = list(map(int, re.findall(r'\d+', row)))
        result += (max(numbers) - min(numbers))
    print(result)


def part_2(input_string):
    rows = input_string.split('\n')
    result = 0
    for row in rows:
        numbers = sorted(list(map(int, re.findall(r'\d+', row))))
        found_division = False
        for i in range(len(numbers)):
            for num in numbers[i + 1:]:
                if num % numbers[i] == 0:
                    result += (num // numbers[i])
                    break
            if found_division:
                break
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2017/Input_02.txt', 'r')
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
