import argparse


def part_1(input_string):
    instructions = input_string.split('\n')
    registers = {}
    cur = 0
    played_freq = -1
    while 0 <= cur < len(instructions):
        instruction = instructions[cur].split(' ')
        command = instruction[0]
        if command == 'snd':
            freq = instruction[1]
            try:
                freq = int(freq)
            except ValueError:
                freq = registers.get(freq, 0)
            played_freq = freq
        elif command == 'rcv':
            value = instruction[1]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            if value != 0:
                print(played_freq)
                break
        elif command == 'set':
            reg, value = instruction[1:]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            registers.update({reg: value})
        elif command == 'add':
            reg, value = instruction[1:]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            registers.update({reg: registers.get(reg, 0) + value})
        elif command == 'mul':
            reg, value = instruction[1:]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            registers.update({reg: registers.get(reg, 0) * value})
        elif command == 'mod':
            reg, value = instruction[1:]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            registers.update({reg: registers.get(reg, 0) % value})
        elif command == 'jgz':
            value, offset = instruction[1:]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            try:
                offset = int(offset)
            except ValueError:
                offset = registers.get(offset, 0)
            if value > 0:
                cur += offset
                continue
        cur += 1


def part_2(input_string):
    instructions = input_string.split('\n')
    program_registers = [{'p': 0, 'cur': 0, 'waiting': False}, {'p': 1, 'cur': 0, 'waiting': False}]
    send_count = 0
    while not ((program_registers[0]['waiting'] and 'rcv' not in program_registers[0]) and (program_registers[1]['waiting'] and 'rcv' not in program_registers[1])):
        if not (program_registers[0]['waiting'] and 'rcv' not in program_registers[0]):
            while 0 <= program_registers[0]['cur'] < len(instructions):
                instruction = instructions[program_registers[0]['cur']].split(' ')
                command = instruction[0]
                if command == 'snd':
                    value = instruction[1]
                    try:
                        value = int(value)
                    except ValueError:
                        value = program_registers[0].get(value, 0)
                    program_registers[1].update({'rcv': program_registers[1].get('rcv', []) + [value]})
                elif command == 'rcv':
                    reg = instruction[1]
                    if 'rcv' not in program_registers[0]:
                        program_registers[0]['waiting'] = True
                        break
                    value = program_registers[0]['rcv'].pop(0)
                    program_registers[0].update({reg: value})
                    if len(program_registers[0]['rcv']) == 0:
                        del program_registers[0]['rcv']
                    program_registers[0]['waiting'] = False
                elif command == 'set':
                    reg, value = instruction[1:]
                    try:
                        value = int(value)
                    except ValueError:
                        value = program_registers[0].get(value, 0)
                    program_registers[0].update({reg: value})
                elif command == 'add':
                    reg, value = instruction[1:]
                    try:
                        value = int(value)
                    except ValueError:
                        value = program_registers[0].get(value, 0)
                    program_registers[0].update({reg: program_registers[0].get(reg, 0) + value})
                elif command == 'mul':
                    reg, value = instruction[1:]
                    try:
                        value = int(value)
                    except ValueError:
                        value = program_registers[0].get(value, 0)
                    program_registers[0].update({reg: program_registers[0].get(reg, 0) * value})
                elif command == 'mod':
                    reg, value = instruction[1:]
                    try:
                        value = int(value)
                    except ValueError:
                        value = program_registers[0].get(value, 0)
                    program_registers[0].update({reg: program_registers[0].get(reg, 0) % value})
                elif command == 'jgz':
                    value, offset = instruction[1:]
                    try:
                        value = int(value)
                    except ValueError:
                        value = program_registers[0].get(value, 0)
                    try:
                        offset = int(offset)
                    except ValueError:
                        offset = program_registers[0].get(offset, 0)
                    if value > 0:
                        program_registers[0]['cur'] += offset
                        continue
                program_registers[0]['cur'] += 1
        if not (program_registers[1]['waiting'] and 'rcv' not in program_registers[1]):
            while 0 <= program_registers[1]['cur'] < len(instructions):
                instruction = instructions[program_registers[1]['cur']].split(' ')
                command = instruction[0]
                if command == 'snd':
                    value = instruction[1]
                    try:
                        value = int(value)
                    except ValueError:
                        value = program_registers[1].get(value, 0)
                    program_registers[0].update({'rcv': program_registers[0].get('rcv', []) + [value]})
                    send_count += 1
                elif command == 'rcv':
                    reg = instruction[1]
                    if 'rcv' not in program_registers[1]:
                        program_registers[1]['waiting'] = True
                        break
                    value = program_registers[1]['rcv'].pop(0)
                    program_registers[1].update({reg: value})
                    if len(program_registers[1]['rcv']) == 0:
                        del program_registers[1]['rcv']
                    program_registers[1]['waiting'] = False
                elif command == 'set':
                    reg, value = instruction[1:]
                    try:
                        value = int(value)
                    except ValueError:
                        value = program_registers[1].get(value, 0)
                    program_registers[1].update({reg: value})
                elif command == 'add':
                    reg, value = instruction[1:]
                    try:
                        value = int(value)
                    except ValueError:
                        value = program_registers[1].get(value, 0)
                    program_registers[1].update({reg: program_registers[1].get(reg, 0) + value})
                elif command == 'mul':
                    reg, value = instruction[1:]
                    try:
                        value = int(value)
                    except ValueError:
                        value = program_registers[1].get(value, 0)
                    program_registers[1].update({reg: program_registers[1].get(reg, 0) * value})
                elif command == 'mod':
                    reg, value = instruction[1:]
                    try:
                        value = int(value)
                    except ValueError:
                        value = program_registers[1].get(value, 0)
                    program_registers[1].update({reg: program_registers[1].get(reg, 0) % value})
                elif command == 'jgz':
                    value, offset = instruction[1:]
                    try:
                        value = int(value)
                    except ValueError:
                        value = program_registers[1].get(value, 0)
                    try:
                        offset = int(offset)
                    except ValueError:
                        offset = program_registers[1].get(offset, 0)
                    if value > 0:
                        program_registers[1]['cur'] += offset
                        continue
                program_registers[1]['cur'] += 1
    print(send_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2017/Input_18.txt', 'r')
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
