import argparse
import re

from copy import deepcopy


'''
Addition:
    addr (add register) stores into register C the result of adding register A and register B.
    addi (add immediate) stores into register C the result of adding register A and value B.

Multiplication:
    mulr (multiply register) stores into register C the result of multiplying register A and register B.
    muli (multiply immediate) stores into register C the result of multiplying register A and value B.

Bitwise AND:
    banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
    bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.

Bitwise OR:
    borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
    bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.

Assignment:
    setr (set register) copies the contents of register A into register C. (Input B is ignored.)
    seti (set immediate) stores value A into register C. (Input B is ignored.)

Greater-than testing:
    gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
    gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
    gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.

Equality testing:
    eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
    eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
    eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
'''

def addr(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = computing_registers[instruction[1]] + computing_registers[instruction[2]]
    return computing_registers


def addi(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = computing_registers[instruction[1]] + instruction[2]
    return computing_registers


def mulr(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = computing_registers[instruction[1]] * computing_registers[instruction[2]]
    return computing_registers


def muli(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = computing_registers[instruction[1]] * instruction[2]
    return computing_registers


def banr(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = computing_registers[instruction[1]] & computing_registers[instruction[2]]
    return computing_registers


def bani(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = computing_registers[instruction[1]] & instruction[2]
    return computing_registers


def borr(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = computing_registers[instruction[1]] | computing_registers[instruction[2]]
    return computing_registers


def bori(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = computing_registers[instruction[1]] | instruction[2]
    return computing_registers


def setr(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = computing_registers[instruction[1]]
    return computing_registers


def seti(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = instruction[1]
    return computing_registers


def gtir(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = instruction[1] > computing_registers[instruction[2]]
    return computing_registers


def gtri(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = computing_registers[instruction[1]] > instruction[2]
    return computing_registers


def gtrr(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = computing_registers[instruction[1]] > computing_registers[instruction[2]]
    return computing_registers


def eqir(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = instruction[1] == computing_registers[instruction[2]]
    return computing_registers


def eqri(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = computing_registers[instruction[1]] == instruction[2]
    return computing_registers


def eqrr(registers, instruction):
    computing_registers = deepcopy(registers)
    computing_registers[instruction[3]] = computing_registers[instruction[1]] == computing_registers[instruction[2]]
    return computing_registers


def part_1(input_string):
    result = 0
    for before, instruction, after in re.findall(r"Before: ([\[\d, \]]+)\n([\d ]+)\nAfter:  ([\[\d, \]]+)", input_string):
        before = eval(before)
        instruction = list(map(int, instruction.split(' ')))
        after = eval(after)
        operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
        behavior_count = 0
        for operation in operations:
            if operation(before, instruction) == after:
                behavior_count += 1
            if behavior_count == 3:
                result += 1
                break
    print(result)


def part_2(input_string):
    sample, program = input_string.split("\n\n\n\n")
    opcodes = []
    for before, instruction, after in re.findall(r"Before: ([\[\d, \]]+)\n([\d ]+)\nAfter:  ([\[\d, \]]+)", sample):
        before = eval(before)
        instruction = list(map(int, instruction.split(' ')))
        after = eval(after)
        opcode = instruction[0]
        if len(opcodes) < (opcode+1):
            opcodes.extend([[] for _ in range(opcode - len(opcodes) + 1)])

        operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
        if opcodes[opcode]:
            operations = opcodes[opcode]
        new_opcodes = []
        for operation in operations:
            if operation(before, instruction) == after:
                new_opcodes.append(operation)
        opcodes[opcode] = new_opcodes

    while any([len(o) > 1 for o in opcodes]):
        for i, opcode in enumerate(opcodes):
            if len(opcode) == 1:
                removing_opcode = opcode[0]
                for j in range(len(opcodes)):
                    if j != i and removing_opcode in opcodes[j]:
                        opcodes[j].remove(removing_opcode)
    
    for i, opcode in enumerate(opcodes):
        opcodes[i] = opcode[0]

    registers = [0 for _ in range(4)]
    for instruction in re.findall(r"([\d ]+)", program):
        instruction = list(map(int, instruction.split(' ')))
        registers = opcodes[instruction[0]](registers, instruction)
    print(registers[0])



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_16.txt', 'r')
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
