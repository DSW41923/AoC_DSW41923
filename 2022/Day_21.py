import argparse
import copy
import re


def get_monkeys(input_string):
    monkeys = {}
    for monkey_name, monkey_value in re.findall(r'(\w{4}): (\d+)', input_string):
        monkeys.update({
            monkey_name:{
                'value': int(monkey_value)
                }
            })
    for monkey_name, l_monkey, operation, r_monkey in re.findall(r'(\w{4}): (\w{4}) ([+\-*/]) (\w{4})', input_string):
        monkeys.update({
            monkey_name:{
                'operation': operation,
                'left': l_monkey,
                'right': r_monkey
                }
            })
    return monkeys


def part_1(input_string):
    monkeys = get_monkeys(input_string)
    while 'value' not in monkeys['root']:
        for monkey in monkeys.values():
            if 'value' not in monkey:
                if 'value' in monkeys[monkey['left']] and 'value' in monkeys[monkey['right']]:
                    monkey_value = eval('{left} {operation} {right}'.format(
                        left=monkeys[monkey['left']]['value'],
                        operation=monkey['operation'],
                        right=monkeys[monkey['right']]['value']))
                    monkey.update({
                        'value': int(monkey_value)})
    print(monkeys['root']['value'])


def part_2(input_string):
    monkeys = get_monkeys(input_string)
    monkeys['root']['operation'] = '=='
    # Get values not related to monkey humn
    is_updating = True
    while is_updating:
        is_updating = False
        for name, monkey in monkeys.items():
            if name == 'humn':
                continue
            if 'left' in monkey and 'right' in monkey:
                if 'humn' in [monkey['left'], monkey['right']]:
                    continue
            if 'value' not in monkey:
                if 'value' in monkeys[monkey['left']] and 'value' in monkeys[monkey['right']]:
                    monkey_value = eval('{left} {operation} {right}'.format(
                        left=monkeys[monkey['left']]['value'],
                        operation=monkey['operation'],
                        right=monkeys[monkey['right']]['value']))
                    monkeys.update({
                        name: {
                            'value': int(monkey_value)}
                        })
                    is_updating = True
    # Reversedly computing values for monkey humn
    monkeys['humn'] = {}
    name = 'root'
    number = 0
    while name != 'humn':
        monkey = monkeys[name]
        operation = monkey['operation']
        value = 0
        if 'value' in monkeys[monkey['left']] and 'value' in monkeys[monkey['right']]:
            return

        if 'value' in monkeys[monkey['left']]:
            name = monkey['right']
            value = monkeys[monkey['left']]['value']
            if operation == '-':
                number = value - number
            elif operation == '/':
                number = value // number
        if 'value' in monkeys[monkey['right']]:
            name = monkey['left']
            value = monkeys[monkey['right']]['value']
            if operation == '-':
                number += value
            elif operation == '/':
                number *= value

        if operation == '==':
            number = value
        elif operation == '+':
            number -= value
        elif operation == '*':
            number //= value
    print(number)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2022/Input_21.txt', 'r')
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

