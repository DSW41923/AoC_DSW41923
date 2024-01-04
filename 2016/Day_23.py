import argparse

from Day_12 import do_instruction


def get_new_operation(instruction):
    decoded_target_instruction = instruction.split(' ')
    target_operation, target_opperands = decoded_target_instruction[0], decoded_target_instruction[1:]
    if len(target_opperands) == 1:
        if target_operation == 'inc':
            return ' '.join(['dec'] + target_opperands)

        if target_operation != 'inc':
            return ' '.join(['inc'] + target_opperands)

    if len(target_opperands) == 2:
        if target_operation == 'jnz':
            return ' '.join(['cpy'] + target_opperands)

        if target_operation != 'jnz':
            return ' '.join(['jnz'] + target_opperands)


def toggle_instructions(instruction, instructions, registers):
    decoded_instruction = instruction.split(' ')
    opperands = decoded_instruction[1:]
    try:
        target_instruction_index = registers['i'] + registers[opperands[0]]
        target_instruction = instructions[target_instruction_index]
    except KeyError:
        target_instruction_index = registers['i'] + int(opperands[0])
        target_instruction = instructions[target_instruction_index]
    except IndexError:
        registers['i'] += 1
        return

    instructions[target_instruction_index] = get_new_operation(target_instruction)
    registers['i'] += 1


def part_1(input_string):
    instructions = input_string.split('\n')
    registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0, 'i': 0}
    while registers['i'] < len(instructions):
        instruction = instructions[registers['i']]
        if instruction.startswith('tgl'):
            toggle_instructions(instruction, instructions, registers)
            continue
        do_instruction(instruction, registers)
    print(registers['a'])


def part_2():
    # Bruteforce the actual computation by human
    a, b, c, d = 12, 0, 0, 0
    b = a - 1
    while True:
        a *= b
        b -= 1
        c = b * 2
        if c == 2:
            break
    a += 72 * 93

    print(a)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2016/Input_23.txt', 'r')
    input_string = file_input.read()
    file_input.close()

    if args.part == '1':
        part_1(input_string)
    elif args.part == '2':
        part_2()
    else:
        part_1(input_string)
        part_2()


if __name__ == "__main__":
    main()
