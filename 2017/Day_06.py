import argparse
import re


def part_1(input_string):
    bank_state = list(map(int, re.findall(r'\d+', input_string)))
    redistribution_count = 0
    bank_state_history = []
    while tuple(bank_state) not in bank_state_history:
        bank_state_history.append(tuple(bank_state))
        max_blocks = max(bank_state)
        max_bank = bank_state.index(max_blocks)
        bank_state[max_bank] = 0
        for i in range(max_blocks):
            bank_state[(max_bank + i + 1) % len(bank_state)] += 1
        redistribution_count += 1
    print(redistribution_count)


def part_2(input_string):
    bank_state = list(map(int, re.findall(r'\d+', input_string)))
    bank_state_history = []
    while tuple(bank_state) not in bank_state_history:
        bank_state_history.append(tuple(bank_state))
        max_blocks = max(bank_state)
        max_bank = bank_state.index(max_blocks)
        bank_state[max_bank] = 0
        for i in range(max_blocks):
            bank_state[(max_bank + i + 1) % len(bank_state)] += 1
    print(len(bank_state_history) - bank_state_history.index(tuple(bank_state)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2017/Input_06.txt', 'r')
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
