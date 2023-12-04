import argparse
import re


def part_1(input_string):
    result = 0
    for winning_numbers, holding_numbers in re.findall(r"Card +\d+: ([\d ]+) \| ([\d ]+)", input_string):
        winning_numbers = set(re.findall(r"(\d+)", winning_numbers))
        holding_numbers = set(re.findall(r"(\d+)", holding_numbers))
        winning_numbers_held = len(winning_numbers & holding_numbers)
        if winning_numbers_held > 0:
            result += (2**(winning_numbers_held - 1))
    print(result)


def part_2(input_string):
    card_counts = [1 for _ in range(len(input_string.split('\n')))]
    for card_id, winning_numbers, holding_numbers in re.findall(r"Card +(\d+): ([\d ]+) \| ([\d ]+)", input_string):
        card_id = int(card_id)
        winning_numbers = set(re.findall(r"(\d+)", winning_numbers))
        holding_numbers = set(re.findall(r"(\d+)", holding_numbers))
        winning_numbers_held = len(winning_numbers & holding_numbers)
        for i in range(winning_numbers_held):
            card_counts[card_id+i] += card_counts[card_id-1]
    print(sum(card_counts))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_04.txt', 'r')
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
