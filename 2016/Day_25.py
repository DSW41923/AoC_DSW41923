import argparse

from Day_12 import do_instruction
from Day_23 import toggle_instructions


def run_instructions(instructions, registers):
    while registers['i'] < len(instructions):
        instruction = instructions[registers['i']]
        if instruction.startswith('tgl'):
            toggle_instructions(instruction, instructions, registers)
            continue

        if instruction.startswith('out'):
            decoded_instruction = instruction.split(' ')
            opperands = decoded_instruction[1:]
            try:
                output = registers[opperands[0]]
            except KeyError:
                output = int(opperands[0])
            except ValueError:
                raise

            yield output

            registers['i'] += 1
            continue
        do_instruction(instruction, registers)


def part_1(input_string):
    instructions = input_string.split('\n')
    x = 0
    outputs = []
    while True:
        registers = {'a': x, 'b': 0, 'c': 0, 'd': 0, 'i': 0}
        output = run_instructions(instructions, registers)
        outputs.append(next(output))
        while outputs[-1] in [0, 1]:
            if len(outputs) > 100:
                print(x)
                return

            outputs.append(next(output))
            if len(outputs) > 1:
                if outputs[-2] == outputs[-1]:
                    break

        outputs = []
        x += 1


def part_2():
    print("Merry Christmas!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('../inputs/2016/Input_25.txt', 'r')
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
