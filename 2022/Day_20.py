import argparse


def part_1(input_string):
    numbers = list(map(int, input_string.split('\n')[:-1]))
    mixing_numbers = [(0, number) for number in numbers]
    for number in numbers:
        index = mixing_numbers.index((0, number))
        del mixing_numbers[index]
        new_index = (index + number) % len(mixing_numbers)
        mixing_numbers.insert(new_index, (1, number))

    zero_index = mixing_numbers.index((1, 0))
    print(
        mixing_numbers[(zero_index + 1000) % len(numbers)][1] + \
        mixing_numbers[(zero_index + 2000) % len(numbers)][1] + \
        mixing_numbers[(zero_index + 3000) % len(numbers)][1])


def part_2(input_string):
    decryption_key = 811589153
    numbers = list(map(lambda x: int(x) * decryption_key, input_string.split('\n')[:-1]))
    mixing_numbers = list(enumerate(numbers))
    mixing_times = 10
    for _ in range(mixing_times):
        for i, number in enumerate(numbers):
            index = mixing_numbers.index((i, number))
            del mixing_numbers[index]
            new_index = (index + number) % len(mixing_numbers)
            if new_index == 0:
                mixing_numbers.append((i, number))
            else:
                mixing_numbers.insert(new_index, (i, number))

    zero_index = mixing_numbers.index((numbers.index(0), 0))
    print(
        mixing_numbers[(zero_index + 1000) % len(numbers)][1] + \
        mixing_numbers[(zero_index + 2000) % len(numbers)][1] + \
        mixing_numbers[(zero_index + 3000) % len(numbers)][1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_20.txt', 'r')
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

