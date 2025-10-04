import argparse
import re


def parse_input(input_string):
    states, rules_string = input_string.split('\n\n')
    states = list(states.split(' ')[-1])
    rules = {}
    for rule_left, rule_right in re.findall(r"([\#\.]{5}) => ([\#\.])", rules_string):
        rules.update({
            rule_left: rule_right
        })
    return states, rules


def part_1(input_string):
    states, rules = parse_input(input_string)

    states = ['.' for _ in range(40)] + states + ['.' for _ in range(40)]
    for _ in range(20):
        new_states = ['.' for _ in range(2)]
        for i in range(2,len(states)-2):
            new_states.append(rules[''.join(states[i-2:i+3])])
        new_states += ['.' for _ in range(2)]
        states = new_states

    result = 0
    for i in range(len(states)):
        if states[i] == '#':
            result += (i-40)
    print(result)


def part_2(input_string):
    states, rules = parse_input(input_string)

    states = ['.' for _ in range(5)] + states + ['.' for _ in range(5)]
    index = -5
    remaining_generations = 50000000000
    while remaining_generations > 0:
        new_states = ['.' for _ in range(5)]
        for i in range(2,len(states)-2):
            new_states.append(rules[''.join(states[i-2:i+3])])
        new_states += ['.' for _ in range(5)]
        remaining_generations -= 1
        new_start = new_states.index('#')-5
        new_end = len(new_states)
        for i in range(1,len(new_states)):
            if new_states[-i] == '#':
                new_end = len(new_states)-i+5
                break
        index = (index - 3) + new_start
        if new_states[new_start:new_end+1] == states:
            # print(index, new_start, ''.join(states))
            break
        states = new_states[new_start:new_end+1]

    result = 0
    for i in range(len(states)):
        if states[i] == '#':
            result += (i+index+remaining_generations)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_12.txt', 'r')
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
