import sys
import getopt

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_08.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_08.py [-h | --help]')
            print('Advent of Code 2020 Day 08')
            sys.exit()

    file_input = open('inputs/2020/Input_08.txt', 'r')
    instruction_strings = file_input.readlines()
    file_input.close()
    instructions = []
    for instruction_string in instruction_strings:
        operation, num = instruction_string.split(' ')
        instructions.append((operation, int(num)))
    accumulator = 0
    cur = 0
    cur_history = []
    while True:
        if cur in cur_history:
            break
        cur_history.append(cur)
        operation, num = instructions[cur]
        if operation == 'jmp':
            cur += num
        else:
            cur += 1
            if operation == 'acc':
                accumulator += num
    print(accumulator)

    for line, instruction in enumerate(instructions):
        original_operation, number = instruction
        if original_operation == 'jmp':
            instructions[line] = ('nop', number)
        elif original_operation == 'nop':
            instructions[line] = ('jmp', number)

        accumulator = 0
        cur = 0
        cur_history = []
        while True:
            if cur in cur_history or cur >= len(instructions):
                break
            cur_history.append(cur)
            operation, num = instructions[cur]
            if operation == 'jmp':
                cur += num
            else:
                cur += 1
                if operation == 'acc':
                    accumulator += num
        if cur == len(instructions):
            print(accumulator)
        instructions[line] = (original_operation, number)

if __name__ == "__main__":
    main(sys.argv[1:])