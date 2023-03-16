import argparse


def part_1(input_string):
    step = int(input_string)
    buffer = [0]
    cur = 0
    for i in range(1, 2018):
        new_cur = (cur + step) % len(buffer)
        buffer.insert(new_cur + 1, i)
        cur = new_cur + 1
    print(buffer[(buffer.index(2017) + 1) % len(buffer)])
    print(buffer[(buffer.index(0) + 1) % len(buffer)])


def part_2(input_string):
    step = int(input_string)
    value = ''
    pos = 0
    cur = 0
    for i in range(1, 50000001):
        new_cur = (cur + step) % i
        if new_cur == pos:
            value = i
        elif new_cur < pos:
            pos += 1
        cur = new_cur + 1
    print(value)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_17.txt', 'r')
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
