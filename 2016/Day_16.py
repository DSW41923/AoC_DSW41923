import argparse


def get_fit_data(desired_length, initial_state):
    data = initial_state
    while len(data) < desired_length:
        data_num = int(data[::-1], 2)
        max_appending_data_num = int('1' * len(data), 2)
        appending_data_num = max_appending_data_num ^ data_num
        raw_appending_data = bin(appending_data_num)[2:]
        appending_data = '0' * (len(data) - len(raw_appending_data)) + raw_appending_data
        data += ('0' + appending_data)

    return data[:desired_length]


def get_checksum(data):
    checksum = data
    while len(checksum) % 2 == 0:
        new_checksum = ''
        for pair in [checksum[i:i + 2] for i in range(0, len(checksum), 2)]:
            if int(pair, 2) % 3 == 0:
                new_checksum += '1'
                continue

            if int(pair, 2) % 3 != 0:
                new_checksum += '0'
                continue

        checksum = new_checksum

    return checksum


def part_1(initial_state):
    fit_data = get_fit_data(272, initial_state)
    checksum = get_checksum(fit_data)
    print(checksum)


def part_2(initial_state):
    fit_data = get_fit_data(35651584, initial_state)
    checksum = get_checksum(fit_data)
    print(checksum)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    initial_state = '11110010111001001'

    if args.part == '1':
        part_1(initial_state)
    elif args.part == '2':
        part_2(initial_state)
    else:
        part_1(initial_state)
        part_2(initial_state)


if __name__ == "__main__":
    main()
