import argparse
import re


def part_1(input_string):
    signal_strengths_sum = 0
    register = 1
    cycle = 1
    for instruction, value in re.findall(r'(\w{4}) ?(-?\d*)', input_string):
        if instruction == 'noop':
            if cycle % 40 == 20:
                signal_strengths_sum += cycle * register
            cycle += 1

        if instruction == 'addx':
            if cycle % 40 == 20:
                signal_strengths_sum += cycle * register
            cycle += 1
            if cycle % 40 == 20:
                signal_strengths_sum += cycle * register
            register += int(value)
            cycle += 1
    print(signal_strengths_sum)


def part_2(input_string):
    pixels = []
    register = 1
    cycle = 1
    for instruction, value in re.findall(r'(\w{4}) ?(-?\d*)', input_string):
        if instruction == 'noop':
            if abs(cycle - 1 - register) > 1:
                pixels.append('.')
            else:
                pixels.append('#')
            if cycle % 40 == 0:
                print(''.join(pixels))
                pixels = []
                cycle = 0
            cycle += 1

        if instruction == 'addx':
            if abs(cycle - 1 - register) > 1:
                pixels.append('.')
            else:
                pixels.append('#')
            if cycle % 40 == 0:
                print(''.join(pixels))
                pixels = []
                cycle = 0
            cycle += 1
            if abs(cycle - 1 - register) > 1:
                pixels.append('.')
            else:
                pixels.append('#')
            if cycle % 40 == 0:
                print(''.join(pixels))
                pixels = []
                cycle = 0
            register += int(value)
            cycle += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_10.txt', 'r')
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

