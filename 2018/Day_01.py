import argparse
import re


def part_1(input_string):
    result = 0
    for sign, change in re.findall(r"([+\-])(\d+)", input_string):
        if sign == '-':
            result -= int(change)
        else:
            result += int(change)
    print(result)


def part_2(input_string):
    results = [0]
    while True:
        for sign, change in re.findall(r"([+\-])(\d+)", input_string):
            new_result = results[-1]
            if sign == '-':
                new_result -= int(change)
            else:
                new_result += int(change)

            if new_result in results:
                print(new_result)
                return
            else:
                results.append(new_result)
        if len(results) > 2000:
            results = results[:1000]+results[-500:]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_01.txt', 'r')
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
