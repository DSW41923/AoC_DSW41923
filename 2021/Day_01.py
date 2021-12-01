import argparse


def part_1(input_string):
    measurements = list(map(int, input_string.split('\n')))
    larger_count = 0
    for i in range(len(measurements)):
        if i > 0 and measurements[i] > measurements[i-1]:
            larger_count += 1
    print(larger_count)


def part_2(input_string):
    measurements = list(map(int, input_string.split('\n')))
    three_measurements = [sum(measurements[i:i+3]) for i in range(len(measurements) - 2)]
    larger_count = 0
    for i in range(len(three_measurements)):
        if i > 0 and three_measurements[i] > three_measurements[i - 1]:
            larger_count += 1
    print(larger_count)


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
