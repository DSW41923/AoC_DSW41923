import argparse

from string import ascii_lowercase, ascii_uppercase


def get_triggered_units():
    return [a+b for a, b in (list(zip(ascii_lowercase, ascii_uppercase)) + list(zip(ascii_uppercase, ascii_lowercase)))]


def react(polymer, triggered_units):
    while True:
        new_polymer = polymer
        for unit in triggered_units:
            new_polymer = new_polymer.replace(unit, '')
        if new_polymer == polymer:
            break
        polymer = new_polymer
    return polymer


def part_1(input_string):
    polymer = input_string
    triggered_units = get_triggered_units()
    polymer = react(polymer, triggered_units)
    print(len(polymer))


def part_2(input_string):
    polymer = input_string
    triggered_units = get_triggered_units()
    min_polymer_len = len(polymer)
    for lower, upper in zip(ascii_lowercase, ascii_uppercase):
        trial_polymer = polymer.replace(lower, '').replace(upper, '')
        trial_polymer = react(trial_polymer, triggered_units)
        min_polymer_len = min(len(trial_polymer), min_polymer_len)
    print(min_polymer_len)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_05.txt', 'r')
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
