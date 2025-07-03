import argparse
import re


def part_1(input_string):
    result = 0
    for a, b in re.findall(r'mul\((\d+),(\d+)\)',input_string):
        result += int(a) * int(b)
    print(result)


def part_2(input_string):
    result = 0
    dos = [d.start(0) for d in re.finditer(r'do\(\)',input_string)]
    donts = [d.start(0) for d in re.finditer(r'don\'t\(\)',input_string)]
    for m in re.finditer(r'mul\(\d+,\d+\)',input_string):
        index = m.start(0)
        nearest_do = 0
        for d in dos:
            if d > index:
                break
            nearest_do = d
        nearest_donts = 0
        for d in donts:
            if d > index:
                break
            nearest_donts = d
        if nearest_do > nearest_donts or nearest_do == nearest_donts == 0:
            a, b = re.findall(r'mul\((\d+),(\d+)\)',m.group(0))[0]
            result += int(a) * int(b)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_03.txt', 'r')
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
