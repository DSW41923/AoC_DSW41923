import argparse
import re

from collections import Counter


def part_1(input_string):
    desired_value_count = 0
    for output_values_string in re.findall(r" \| ([abcdefg ]+)", input_string):
        output_values = output_values_string.split(' ')
        for value in output_values:
            if len(value) in [2, 3, 4, 7]:
                desired_value_count += 1
    print(desired_value_count)


def part_2(input_string):
    total_output_values = 0
    for input_values_string, output_values_string in re.findall(r"([abcdefg ]+) \| ([abcdefg ]+)", input_string):
        input_values = list(map(lambda v: ''.join(sorted(v)), input_values_string.split(' ')))
        output_values = list(map(lambda v: ''.join(sorted(v)), output_values_string.split(' ')))
        segment_counts = Counter(input_values_string.replace(' ', ''))
        segment_1 = ([k for k, c in segment_counts.items() if c == 6])[0]
        segment_4 = ([k for k, c in segment_counts.items() if c == 4])[0]
        segment_5 = ([k for k, c in segment_counts.items() if c == 9])[0]
        segment_2 = ([k for k in list(([v for v in input_values if len(v) == 2])[0]) if k != segment_5])[0]

        numbers = {}
        for value in list(input_values):
            if len(value) == 2:
                numbers.update({value: 1})
                continue

            if len(value) == 3:
                numbers.update({value: 7})
                continue

            if len(value) == 4:
                numbers.update({value: 4})
                continue

            if len(value) == 5:
                if segment_1 in value:
                    numbers.update({value: 5})
                    continue

                if segment_4 not in value:
                    numbers.update({value: 3})
                    continue

                if segment_5 not in value:
                    numbers.update({value: 2})
                    continue

            if len(value) == 6:
                if segment_4 not in value:
                    numbers.update({value: 9})
                    continue

                if segment_2 in value:
                    numbers.update({value: 0})
                    continue

                numbers.update({value: 6})
                continue

            if len(value) == 7:
                numbers.update({value: 8})
                continue

        output_value = 0
        for value in output_values:
            output_value = output_value * 10 + numbers[value]

        total_output_values += output_value

    print(total_output_values)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_08.txt', 'r')
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
