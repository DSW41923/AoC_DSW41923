import argparse


def part_1(input_string):
    snafu_numbers = input_string.split('\n')[:-1]
    final_input = 0
    for snafu_number in snafu_numbers:
        positive_sanfu = ''
        negitive_sanfu = ''
        for number in snafu_number:
            if number in ['0', '1', '2']:
                positive_sanfu += number
                negitive_sanfu += '0'
                continue
            if number == '-':
                positive_sanfu += '0'
                negitive_sanfu += '1'
                continue
            if number == '=':
                positive_sanfu += '0'
                negitive_sanfu += '2'
                continue
            raise ValueError
        final_input += (int(positive_sanfu, 5) - int(negitive_sanfu, 5))
    final_input_snafu_char = []
    while final_input > 0:
        remainder = final_input % 5
        if remainder == 3:
            final_input_snafu_char.insert(0, '=')
            final_input //= 5
            final_input += 1
            continue
        if remainder == 4:
            final_input_snafu_char.insert(0, '-')
            final_input //= 5
            final_input += 1
            continue

        final_input_snafu_char.insert(0, str(final_input % 5))
        final_input //= 5
    final_input_snafu = ''.join(final_input_snafu_char)
    print(final_input_snafu)


def part_2(input_string):
    print("Merry Christmas!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_25.txt', 'r')
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

