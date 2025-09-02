import argparse
import re

from copy import deepcopy


def parse_input(input_string):
    registers = {'A':0, 'B':0, 'C': 0}
    program = None
    for a_data, b_data, c_data, program_data in re.findall(r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: ([\d,]+)", input_string):
        registers['A'] = int(a_data)
        registers['B'] = int(b_data)
        registers['C'] = int(c_data)
        program = tuple(map(int, program_data.split(',')))
    return registers, program


def combo_operand(num, registers):
    if num < 4:
        return num
    elif num == 4:
        return registers['A']
    elif num == 5:
        return registers['B']
    elif num == 6:
        return registers['C']
    elif num == 7:
        return


def machine(registers, program):
    instruction_pointer = 0
    out = []
    while True:
        if instruction_pointer >= len(program):
            break
        instruction = program[instruction_pointer]
        operand = program[instruction_pointer+1]
        # print(instruction, operand, registers)
        if instruction == 0: # adv
            # denominator = 2**combo_operand(operand)
            # numerator = registers['A']
            # numerator // denominator == numerator >> combo_operand(operand)
            registers['A'] = registers['A'] >> combo_operand(operand, registers)
        elif instruction == 1: # bxl
            registers['B'] ^= operand
        elif instruction == 2: # bst
            registers['B'] = combo_operand(operand, registers) % 8
        elif instruction == 3: # jnz
            if registers['A'] != 0:
                instruction_pointer = operand
                continue
        elif instruction == 4: # bxc
            registers['B'] ^= registers['C']
        elif instruction == 5: # out
            out.append(combo_operand(operand, registers) % 8)
        elif instruction == 6: # bdv
            operand = program[instruction_pointer+1]
            registers['B'] = registers['A'] >> combo_operand(operand, registers)
        elif instruction == 7: # cdv
            operand = program[instruction_pointer+1]
            registers['C'] = registers['A'] >> combo_operand(operand, registers)
        else:
            break
        instruction_pointer += 2
    return out


def part_1(input_string):
    registers, program = parse_input(input_string)
    out = machine(registers, program)
    print(','.join(map(str, out)))


def part_2(input_string):
    registers, program = parse_input(input_string)
    trials = [(0, tuple())]
    while not any([tuple(t[1]) == program for t in trials]):
        new_trials = []
        for t, _ in trials:
            for i in range(8):
                trial_registers = deepcopy(registers)
                trial_registers['A'] = 8*t+i
                out = machine(trial_registers, program)
                if program[-len(out):] == tuple(out):
                    new_trials.append((8*t+i,tuple(out)))
        trials = new_trials
    print(min([t[0] for t in trials]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_17.txt', 'r')
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
