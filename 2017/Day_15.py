import argparse
import re


def part_1(input_string):
    a = int(re.findall(r'Generator A starts with (\d+)', input_string)[0])
    b = int(re.findall(r'Generator B starts with (\d+)', input_string)[0])
    match_count = 0
    for _ in range(40000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        if a % 2**16 == b % 2**16:
            match_count += 1
    print(match_count)


def part_2(input_string):
    a = int(re.findall(r'Generator A starts with (\d+)', input_string)[0])
    b = int(re.findall(r'Generator B starts with (\d+)', input_string)[0])
    match_count = 0
    for _ in range(5000000):
        while a % 4:
            a = (a * 16807) % 2147483647
        while b % 8:
            b = (b * 48271) % 2147483647
        if a % 2**16 == b % 2**16:
            match_count += 1
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
    print(match_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_15.txt', 'r')
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
