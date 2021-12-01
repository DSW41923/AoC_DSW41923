import argparse


SUPPORTED_OPERATIONS = ['cpy', 'inc', 'dec', 'jnz']


def do_instruction(instruction, registers):
    decoded_instruction = instruction.split(' ')
    operation, opperands = decoded_instruction[0], decoded_instruction[1:]

    if operation not in SUPPORTED_OPERATIONS:
        raise NotImplementedError

    if operation == 'cpy':
        try:
            registers[opperands[1]] = registers[opperands[0]]
        except KeyError:
            registers[opperands[1]] = int(opperands[0])

        registers['i'] += 1
        return

    if operation == 'inc':
        registers[opperands[0]] += 1
        registers['i'] += 1
        return

    if operation == 'dec':
        registers[opperands[0]] -= 1
        registers['i'] += 1
        return

    if operation == 'jnz':
        try:
            if registers[opperands[0]] != 0:
                registers['i'] += int(opperands[1])
                return
        except KeyError:
            if int(opperands[0]) != 0:
                registers['i'] += int(opperands[1])
                return

        registers['i'] += 1
        return


def part_1(input_string):
    instructions = input_string.split('\n')
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'i': 0}
    while registers['i'] < len(instructions):
        do_instruction(instructions[registers['i']], registers)
    print(registers['a'])


def part_2(input_string):
    instructions = input_string.split('\n')
    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0, 'i': 0}
    while registers['i'] < len(instructions):
        do_instruction(instructions[registers['i']], registers)
    print(registers['a'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_12.txt', 'r')
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
