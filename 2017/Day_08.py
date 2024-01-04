import argparse
import re


def part_1(input_string):
    registers = {}
    for reg_0, act_0, act_1, value_0, reg_1, comp, value_1 in re.findall(r'([\w]+) (dec)?(inc)? ([-\d]+) if ([\w]+) ([><=!]=?) ([-\d]+)', input_string):
        value_0, value_1 = int(value_0), int(value_1)
        if reg_0 not in registers:
            registers.update({reg_0: 0})
        if reg_1 not in registers:
            registers.update({reg_1: 0})
        if (comp == '>' and registers[reg_1] > value_1) or (comp == '<' and registers[reg_1] < value_1) or (comp == '>=' and registers[reg_1] >= value_1) or \
            (comp == '==' and registers[reg_1] == value_1) or (comp == '<=' and registers[reg_1] <= value_1) or (comp == '!=' and registers[reg_1] != value_1):
            if act_0:
                registers[reg_0] -= value_0
            if act_1:
                registers[reg_0] += value_0
    print(max(registers.values()))


def part_2(input_string):
    registers = {}
    result = 0
    for reg_0, act_0, act_1, value_0, reg_1, comp, value_1 in re.findall(r'([\w]+) (dec)?(inc)? ([-\d]+) if ([\w]+) ([><=!]=?) ([-\d]+)', input_string):
        value_0, value_1 = int(value_0), int(value_1)
        if reg_0 not in registers:
            registers.update({reg_0: 0})
        if reg_1 not in registers:
            registers.update({reg_1: 0})
        if (comp == '>' and registers[reg_1] > value_1) or (comp == '<' and registers[reg_1] < value_1) or (comp == '>=' and registers[reg_1] >= value_1) or \
            (comp == '==' and registers[reg_1] == value_1) or (comp == '<=' and registers[reg_1] <= value_1) or (comp == '!=' and registers[reg_1] != value_1):
            if act_0:
                registers[reg_0] -= value_0
            if act_1:
                registers[reg_0] += value_0
        result = max(max(registers.values()), result)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2017/Input_08.txt', 'r')
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
