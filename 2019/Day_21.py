import argparse

from Day_13 import IntCodeComputer
from itertools import product


def part_1(input_string):
    instructions = ["AND", "OR", "NOT"]
    writable_registers = ["T", "J"]
    read_only_registers = ["A", "B", "C", "D"]
    register_pairs = [' '.join(rp) for rp in product(read_only_registers+writable_registers, writable_registers) if rp[0] != rp[1]]
    all_commands = [' '.join(c)+'\n' for c in product(instructions, register_pairs)]
    all_commands.append("NOT T T\n")
    all_commands.append("NOT J J\n")
    program = ""
    result = 0
    while result <= 255:
        '''
        NOT C J 
        AND D J 
        NOT A T 
        OR T J
        '''
        print("Current program: \n"+program, end='')
        print("Current commands options: ")
        for i, c in enumerate(all_commands):
            if c not in program:
                print(str(i)+") " + c, end='')
        command_chosen = int(input("Choose desired command to add: "))
        command = all_commands[command_chosen]
        instruction = ''.join([program, command, "WALK\n"])
        computer = IntCodeComputer(input_string)
        for i in instruction:
            computer.add_input(ord(i))
        computer.run()
        outputs = computer.get_outputs()
        result = outputs[-1]
        for o in outputs:
            if o <= 255:
                print(chr(o), end='')
        if result > 255:
            break
        else:
            save_command = input("Save command? (y/n): ")
            if save_command == 'y':
                program += command
    print(result)

def part_2(input_string):
    instructions = ["AND", "OR", "NOT"]
    writable_registers = ["T", "J"]
    read_only_registers = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    register_pairs = [' '.join(rp) for rp in product(read_only_registers+writable_registers, writable_registers) if rp[0] != rp[1]]
    all_commands = [' '.join(c)+'\n' for c in product(instructions, register_pairs)]
    all_commands.append("NOT T T\n")
    all_commands.append("NOT J J\n")
    program = ""
    result = 0
    while result <= 255:
        '''
        NOT A J 
        NOT C T 
        AND D T 
        AND H T 
        OR T J
        NOT B T 
        AND D T 
        OR T J
        '''
        command = ''
        action = int(input("Choose action: 1) Add new command 2) Remove command: "))
        if action == 1:
            print("Current commands options: ")
            for i, c in enumerate(all_commands):
                print(str(i)+") " + c, end='')
            command_chosen = int(input("Choose desired command to add: "))
            if command_chosen < len(all_commands):
                command = all_commands[command_chosen]
        elif action == 2:
            print("Current program: \n"+program, end='')
            program = program.split('\n')[:-1]
            for i, c in enumerate(program):
                print(str(i)+") " + c)
            command_chosen = int(input("Choose desired command to remove: "))
            if command_chosen < len(program):
                program.pop(command_chosen)
            program = '\n'.join(program)
            if len(program) > 0:
                program += '\n'
        instruction = ''.join([program, command, "RUN\n"])
        computer = IntCodeComputer(input_string)
        for i in instruction:
            computer.add_input(ord(i))
        computer.run()
        outputs = computer.get_outputs()
        result = outputs[-1]
        for o in outputs:
            if o <= 255:
                print(chr(o), end='')
        if result > 255:
            break
        else:
            save_command = input("Save command? (y/n): ")
            if save_command == 'y':
                program += command
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_21.txt', 'r')
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
