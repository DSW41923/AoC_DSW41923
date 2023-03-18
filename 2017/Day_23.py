import argparse
import string


def part_1(input_string):
    instructions = input_string.split('\n')
    registers = {name: 0 for name in string.ascii_lowercase[:8]}
    cur = 0
    mul_count = 0
    while 0 <= cur < len(instructions):
        instruction = instructions[cur].split(' ')
        command = instruction[0]
        if command == 'set':
            reg, value = instruction[1:]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            registers.update({reg: value})
        elif command == 'sub':
            reg, value = instruction[1:]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            registers.update({reg: registers.get(reg, 0) - value})
        elif command == 'mul':
            reg, value = instruction[1:]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            registers.update({reg: registers.get(reg, 0) * value})
            mul_count += 1
        elif command == 'jnz':
            value, offset = instruction[1:]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            try:
                offset = int(offset)
            except ValueError:
                offset = registers.get(offset, 0)
            if value != 0:
                cur += offset
                continue
        cur += 1
    print(mul_count)


def part_2(input_string):
    instructions = input_string.split('\n')
    registers = {name: 0 for name in string.ascii_lowercase[:8]}
    registers['a'] = 1
    cur = 0
    while 0 <= cur < len(instructions):
        if cur == 8:
            break
        # Test if b % d for d in range(2, b)
        # f will be 0 if any of d satisfies, means that b is not prime
        # e is just checking through all possible numbers for multiple
        # elif cur == 11:
        #     if (registers['b'] % registers['d']) == 0:
        #         registers['f'] = 0
        #     registers['e'] = registers['b']
        #     cur = 20
        #     print(registers)
        # elif cur == 23:
        #     registers['d'] = registers['b']
        #     print(cur, registers)
        #     cur = 24

        # h will be incremented 1 while cur = 24~28 if b is not prime

        # Test all b from initial value to at most c
        # elif cur == 28:
        #     print(cur, registers)
        #     if loop_time == 0:
        #         loop_time = abs(registers['b'] - registers['c']) // 17
        #         print(loop_time)
        #         break

        instruction = instructions[cur].split(' ')
        command = instruction[0]
        if command == 'set':
            reg, value = instruction[1:]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            registers.update({reg: value})
        elif command == 'sub':
            reg, value = instruction[1:]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            registers.update({reg: registers.get(reg, 0) - value})
        elif command == 'mul':
            reg, value = instruction[1:]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            registers.update({reg: registers.get(reg, 0) * value})
        elif command == 'jnz':
            value, offset = instruction[1:]
            try:
                value = int(value)
            except ValueError:
                value = registers.get(value, 0)
            try:
                offset = int(offset)
            except ValueError:
                offset = registers.get(offset, 0)
            if value != 0:
                cur += offset
                continue
        cur += 1

    for i in range(registers['b'], registers['c'] + 1, 17):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if not is_prime:
            registers['h'] += 1
    print(registers['h'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_23.txt', 'r')
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
