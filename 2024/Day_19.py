import argparse

from functools import lru_cache


def parse_input(input_string):
    patterns, design_list = input_string.split('\n\n')
    patterns = patterns.split(', ')
    design_list = design_list.split('\n')
    return patterns, design_list


def part_1(input_string):
    patterns, design_list = parse_input(input_string)
    result = 0
    for design in design_list:
        def is_design_possible(d):
            if len(d) == 0:
                return True
            if d in patterns:
                return True
            result = False
            for i in range(1,len(d)+1):
                if d[:i] in patterns:
                    result |= is_design_possible(d[i:])
                if result:
                    break
            return result
        if is_design_possible(design):
            result += 1
    print(result)


def part_2(input_string):
    patterns, design_list = parse_input(input_string)
    result = 0
    for design in design_list:
        @lru_cache(maxsize=None)
        def design_possible_count(d):
            if len(d) == 0:
                return 1
            count = 0
            for i in range(1,len(d)+1):
                if d[:i] in patterns:
                    count += design_possible_count(d[i:])
            return count
        result += design_possible_count(design)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_19.txt', 'r')
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
