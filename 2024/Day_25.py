import argparse


def part_1(input_string):
    lock_pads = []
    key_pads = []
    for pad in input_string.split('\n\n'):
        pad = list(map(list, pad.split('\n')))
        pad_type = None
        if all([p == '#' for p in pad[0]]):
            pad_type = 'LOCK'
            pad = pad[1:]
        elif all([p == '#' for p in pad[-1]]):
            pad_type = 'KEY'
            pad = pad[:-1]

        pad_columns = [[pad[i][j] for i in range(6)] for j in range(5)]
        pad_numeric = tuple(map(lambda c: c.count('#'), pad_columns))
        if pad_type == 'LOCK':
            lock_pads.append(pad_numeric)
        elif pad_type == 'KEY':
            key_pads.append(pad_numeric)

    result = 0
    for lock in lock_pads:
        for key in key_pads:
            fitting = tuple(lock[i]+key[i] for i in range(5))
            if all([f <= 5 for f in fitting]):
                result += 1
    print(result)


def part_2(input_string):
    print("Merry Christmas!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_25.txt', 'r')
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
