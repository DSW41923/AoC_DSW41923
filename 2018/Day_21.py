import argparse

from Day_16 import addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr
from Day_19 import parse_data


def part_1(input_string):
    '''
    (18, 0, 12262664, 17, 0, 65536, 0)
    addi(registers, ['addi', 5, 1, 3])   #r[3] = r[5]+1
    (19, 0, 12262664, 18, 1, 65536, 0)
    muli(registers, ['muli', 3, 256, 3]) #r[3] *= 256
    (20, 0, 12262664, 19, 256, 65536, 0)
    gtrr(registers, ['gtrr', 3, 4, 3])   #r[3] = (r[3] > r[4])
    (21, 0, 12262664, 20, False, 65536, 0)
    addr(registers, ['addr', 3, 2, 2])   #r[2] += r[3]
    (22, 0, 12262664, 21, False, 65536, 0)
    addi(registers, ['addi', 2, 1, 2])   #r[2] += 1
    (24, 0, 12262664, 23, False, 65536, 0)
    addi(registers, ['addi', 5, 1, 5])   #r[5] += 1
    (25, 0, 12262664, 24, False, 65536, 1)
    seti(registers, ['seti', 17, 1, 2])  #r[2] = 17

    if r[3] > r[4] when ip=20
    (21, 0, 12262664, 20, True, 65536, 256)
    addr(registers, ['addr', 3, 2, 2])        #r[2] += r[3]
    (23, 0, 12262664, 22, True, 65536, 256)
    seti(registers, ['seti', 25, 4, 2])       #r[2] = 25
    (26, 0, 12262664, 25, True, 65536, 256)
    addi(registers, ['setr', 5, 3, 4])        #r[4] = r[5]
    (27, 0, 12262664, 26, True, 256, 256)
    seti(registers, ['seti', 7, 7, 2])        #r[2] = 7
    (8, 0, 12262664, 7, True, 256, 256)
    bani(registers, ['bani', 4, 255, 5])      #r[5] = r[4] & 255
    (9, 0, 12262664, 8, True, 256, 0)
    addr(registers, ['addr', 1, 5, 1])        #r[1] += r[5]
    (10, 0, 12262664, 9, True, 256, 0)
    bani(registers, ['bani', 1, 16777215, 1]) #r[1] &= 16777215
    (11, 0, 12262664, 10, True, 256, 0)
    muli(registers, ['muli', 1, 65899, 1])    #r[1] *= 65899
    (12, 0, 808097294936, 11, True, 256, 0)
    bani(registers, ['bani', 1, 16777215, 1]) #r[5] &= 16777215
    (13, 0, 5909080, 12, True, 256, 0)
    gtir(registers, ['gtir', 256, 4, 5])      #r[5] = (256 > r[4])
    (14, 0, 5909080, 13, True, 256, False)
    addr(registers, ['addr', 5, 2, 2])        #r[2] += r[5]
    (15, 0, 5909080, 14, True, 256, False)
    addi(registers, ['addi', 2, 1, 2])        #r[2] += 1
    (17, 0, 5909080, 16, True, 256, False)
    seti(registers, ['seti', 0, 3, 5])        #r[5] = 0
    (18, 0, 5909080, 17, True, 256, 0)

    if 256 > r[4] when ip=13
    (14, 0, *, 13, True, *, True)
    addr(registers, ['addr', 5, 2, 2])        #r[2] += r[5]
    (16, 0, *, 15, True, *, True)
    seti(registers, ['seti', 27, 1, 2])       #r[2] = 27
    (28, 0, *, 27, True, *, True)
    eqrr(registers, ['eqrr', 1, 0, 5])        #r[5] = (r[1] == r[0])
    (29, 0, *, 28, True, *, ?)
    addr(registers, ['addr', 5, 2, 2])        #r[2] += r[5]

    if r[1] == r[0] when ip=28
    (29, 0, *, 28, True, *, True)
    addr(registers, ['addr', 5, 2, 2])        #r[2] += r[5]
    (31, 0, *, 30, True, *, True)
    end
    else
    (29, 0, *, 28, True, *, False)
    addr(registers, ['addr', 5, 2, 2])        #r[2] += r[5]
    (30, 0, *, 29, True, *, True)
    seti(registers, ['seti', 5, 3, 2])        #r[2] = 5
    (6, 0, *, 5, True, *, ?)
    bori(registers, ['bori', 1, 65536, 4])    #r[4] = r[1] | 65536
    (7, 0, *, 6, True, *, False)
    seti(registers, ['seti', 16298264, 8, 1]) #r[1] = 16298264
    (8, 0, 16298264, 7, True, *, False)

    '''
    instruction_register, instructions = parse_data(input_string)
    registers = [0 for _ in range(6)]
    result = 0
    while True:
        registers[0] = result
        ip = 0
        history = []
        halt = True
        while ip < len(instructions):
            # print(tuple([ip] + registers))
            if tuple([ip] + registers) in history:
                halt = False
                break
            history.append(tuple([ip] + registers))
            registers[instruction_register] = ip
            # print(instructions[ip])
            registers = eval(instructions[ip])
            ip = registers[instruction_register]
            ip += 1
            if ip == 28:
                print(registers[1])
                return
        
        if halt:
            print(result)
            break

        result += 1


def part_2(input_string):
    instruction_register, instructions = parse_data(input_string)
    registers = [0 for _ in range(6)]
    halting_results = []
    while True:
        ip = 0
        while ip < len(instructions):
            # print(tuple([ip] + registers))
            if ip == 20:
                registers[5] = (registers[4] // 256)
                registers[3] = registers[5] + 1
                registers[3] *= 256
            registers[instruction_register] = ip
            # print(instructions[ip])
            registers = eval(instructions[ip])
            ip = registers[instruction_register]
            ip += 1
            if ip == 28:
                if registers[1] in halting_results:
                    print(halting_results[-1])
                    return
                halting_results.append(registers[1])
                # print(halting_results[-10:])
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_21.txt', 'r')
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
