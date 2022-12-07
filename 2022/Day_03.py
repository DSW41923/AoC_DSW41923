import argparse
import string


priority_map = " " + string.ascii_lowercase + string.ascii_uppercase


def part_1(input_string):
    rucksacks = input_string.split('\n')
    priority = 0
    for rucksack in rucksacks:
        first_half_items = []
        for i in range(len(rucksack)):
            if i < len(rucksack) // 2:
                if rucksack[i] not in first_half_items:
                    first_half_items.append(rucksack[i])
                continue
            if rucksack[i] in first_half_items:
                priority += priority_map.index(rucksack[i])
                break
    print(priority)


def part_2(input_string):
    rucksacks = input_string.split('\n')
    priority = 0
    for rucksack_0, rucksack_1, rucksack_2 in zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3]):
        for i in range(len(rucksack_0)):
            if rucksack_0[i] in rucksack_1 and rucksack_0[i] in rucksack_2:
                priority += priority_map.index(rucksack_0[i])
                break
    print(priority)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_03.txt', 'r')
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
