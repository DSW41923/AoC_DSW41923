import argparse


def part_1(input_string):
    datastream_buffer = input_string[:-1] if input_string[-1] == '\n' else input_string
    for i in range(3, len(datastream_buffer)):
        marker = datastream_buffer[i - 3:i + 1]
        if len(set(marker)) == 4:
            print(i + 1)
            break


def part_2(input_string):
    datastream_buffer = input_string[:-1] if input_string[-1] == '\n' else input_string
    for i in range(13, len(datastream_buffer)):
        marker = datastream_buffer[i - 13:i + 1]
        if len(set(marker)) == 14:
            print(i + 1)
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2022/Input_06.txt', 'r')
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
