import argparse
import re

from Day_16 import addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr


def get_low_primes():
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
            103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
            211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
            331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
            449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
            587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
            709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
            853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
            991, 997]


def parse_data(input_string):
    instruction_register = int(re.findall(r"#ip (\d+)", input_string)[0])
    instructions = []
    for instruction, a, b, c in re.findall(r"(\w+) (\d+) (\d+) (\d+)", input_string):
        a, b, c = tuple(map(int, (a, b, c)))
        instructions.append("{}(registers, {})".format(instruction, [instruction, a, b, c]))
    return instruction_register, instructions


def run_program(registers, instruction_register, instructions, part=1):
    ip = 0
    while ip < len(instructions):
        registers[instruction_register] = ip
        registers = eval(instructions[ip])
        ip = registers[instruction_register]
        ip += 1
        if ip == 3 and part == 2:
            break
    return registers


def part_1(input_string):
    instruction_register, instructions = parse_data(input_string)
    registers = [0 for _ in range(6)]
    registers = run_program(registers, instruction_register, instructions)
    print(registers[0])


def part_2(input_string):
    instruction_register, instructions = parse_data(input_string)
    registers = [0 for _ in range(6)]
    registers[0] = 1
    registers = run_program(registers, instruction_register, instructions, part=2)
    primes = get_low_primes()
    for i in range(1001, int(registers[5]**(0.5))+1):
        if (i % 6) in [1, 5]:
            is_prime = True
            for p in primes:
                if (i % p) == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
    prime_factors = []
    for p in primes:
        if (registers[5] % p) == 0:
            n = 1
            r = registers[5] // p
            while r % p == 0:
                n += 1
                r //= p
            prime_factors.append((p, n))
    left = registers[5]
    for p, n in prime_factors:
        for i in range(n):
            left //= p
    prime_factors.append((left, 1))
    result = 1
    for p, n in prime_factors:
        f = 0
        for i in range(n+1):
            f += p**i
        result *= f
    print(result)
    '''
    [1, 0, 0, 0, 0, 0]
    0 addi(registers, ['addi', 4, 16, 4])  # r[4]+=16
    [1, 0, 0, 0, 16, 0]
    17 addi(registers, ['addi', 5, 2, 5])  # r[5]+=2
    [1, 0, 0, 0, 17, 2]
    18 mulr(registers, ['mulr', 5, 5, 5])  # r[5]*=r[5]
    [1, 0, 0, 0, 18, 4]
    19 mulr(registers, ['mulr', 4, 5, 5])  # r[5]*=r[4]
    [1, 0, 0, 0, 19, 76]
    20 muli(registers, ['muli', 5, 11, 5]) # r[5]*=11
    [1, 0, 0, 0, 20, 836]
    21 addi(registers, ['addi', 1, 4, 1])  # r[1]+=4
    [1, 4, 0, 0, 21, 836]
    22 mulr(registers, ['mulr', 1, 4, 1])  # r[1]*=r[4]
    [1, 88, 0, 0, 22, 836]
    23 addi(registers, ['addi', 1, 15, 1]) # r[1]+=15
    [1, 103, 0, 0, 23, 836]
    24 addr(registers, ['addr', 5, 1, 5])  # r[5]+=r[1]
    [1, 103, 0, 0, 24, 939]
    25 addr(registers, ['addr', 4, 0, 4])  # r[4]+=r[0]
    [1, 103, 0, 0, 26, 939]
    27 setr(registers, ['setr', 4, 2, 1])  # r[1]+=r[4]
    [1, 27, 0, 0, 27, 939]
    28 mulr(registers, ['mulr', 1, 4, 1])  # r[1]*=r[4]
    [1, 756, 0, 0, 28, 939]
    29 addr(registers, ['addr', 4, 1, 1])  # r[1]+=r[4]
    [1, 785, 0, 0, 29, 939]
    30 mulr(registers, ['mulr', 4, 1, 1])  # r[1]*=r[4]
    [1, 23550, 0, 0, 30, 939]
    31 muli(registers, ['muli', 1, 14, 1]) # r[1]*=14
    [1, 329700, 0, 0, 31, 939]
    32 mulr(registers, ['mulr', 1, 4, 1])  # r[1]*=r[4]
    [1, 10550400, 0, 0, 32, 939]
    33 addr(registers, ['addr', 5, 1, 5])  # r[5]+=r[1]
    [1, 10550400, 0, 0, 33, 10551339]
    34 seti(registers, ['seti', 0, 8, 0])  # r[0]=0
    [0, 10550400, 0, 0, 34, 10551339]
    35 seti(registers, ['seti', 0, 4, 4])  # r[4]=0
    [0, 10550400, 0, 0, 0, 10551339]
    1 seti(registers, ['seti', 1, 3, 3])   # r[3]=1
    [0, 10550400, 0, 1, 1, 10551339]
    2 seti(registers, ['seti', 1, 4, 2])   # r[2]=1
    [0, 10550400, 1, 1, 2, 10551339]
    3 mulr(registers, ['mulr', 3, 2, 1])   # r[1]=r[3]*r[2]
    [0, 1, 1, 1, 3, 10551339]
    4 eqrr(registers, ['eqrr', 1, 5, 1])   # r[1]=(r[1]==r[5])
    [0, False, 1, 1, 4, 10551339]
    5 addr(registers, ['addr', 1, 4, 4])   # r[4]+=r[1]
    [0, False, 1, 1, 5, 10551339]
    6 addi(registers, ['addi', 4, 1, 4])   # r[4]+=1
    [0, False, 1, 1, 7, 10551339]
    8 addi(registers, ['addi', 2, 1, 2])   # r[2]+=1
    [0, False, 2, 1, 8, 10551339]
    9 gtrr(registers, ['gtrr', 2, 5, 1])   # r[1]=(r[2]>r[5])
    [0, False, 2, 1, 9, 10551339]
    10 addr(registers, ['addr', 4, 1, 4])  # r[4]+=r[1]
    [0, False, 2, 1, 10, 10551339]
    11 seti(registers, ['seti', 2, 2, 4])  # r[4]=r[2]
    [0, False, 2, 1, 2, 10551339]

    loop from 3

    Looking at part 1 result
    if 4 is true -> r[1]=(r[3]*r[2]==r[5])
    3 mulr(registers, ['mulr', 3, 2, 1])   # r[1]=r[3]*r[2]
    [317, 939, 1, 939, 3, 939]
    4 eqrr(registers, ['eqrr', 1, 5, 1])   # r[1]=(r[1]==r[5])
    [317, True, 1, 939, 4, 939]
    5 addr(registers, ['addr', 1, 4, 4])   # r[4]+=r[1]
    [317, True, 1, 939, 6, 939]
    7 addr(registers, ['addr', 3, 0, 0])   # r[0]+=r[3]
    [1256, True, 1, 939, 7, 939]
    8 addi(registers, ['addi', 2, 1, 2])   # r[2]+=1
    [1256, True, 2, 939, 8, 939]
    9 gtrr(registers, ['gtrr', 2, 5, 1])   # r[1]=(r[2]>r[5])
    [1256, False, 2, 939, 9, 939]
    10 addr(registers, ['addr', 4, 1, 4])  # r[4]+=r[1]
    [1256, False, 2, 939, 10, 939]
    11 seti(registers, ['seti', 2, 2, 4])  # r[4]=r[2]
    [1256, False, 2, 939, 2, 939]
    loop from 3

    if 9 is true -> r[2]>r[5]
    3 mulr(registers, ['mulr', 3, 2, 1])   # r[1]=r[3]*r[2]
    [1256, 881721, 939, 939, 3, 939]
    4 eqrr(registers, ['eqrr', 1, 5, 1])   # r[1]=(r[1]==r[5])
    [1256, False, 939, 939, 4, 939]
    5 addr(registers, ['addr', 1, 4, 4])   # r[4]+=r[1]
    [1256, False, 939, 939, 5, 939]
    6 addi(registers, ['addi', 4, 1, 4])   # r[4]+=1
    [1256, False, 939, 939, 7, 939]
    8 addi(registers, ['addi', 2, 1, 2])   # r[2]+=1
    [1256, False, 940, 939, 8, 939]
    9 gtrr(registers, ['gtrr', 2, 5, 1])   # r[1]=(r[2]>r[5])
    [1256, True, 940, 939, 9, 939]
    10 addr(registers, ['addr', 4, 1, 4])  # r[4]+=r[1]
    [1256, True, 940, 939, 11, 939]
    12 addi(registers, ['addi', 3, 1, 3])  # r[3]+=1
    [1256, True, 940, 940, 12, 939]
    13 gtrr(registers, ['gtrr', 3, 5, 1])  # r[1]=(r[3]>r[5])
    [1256, True, 940, 940, 13, 939]
    14 addr(registers, ['addr', 1, 4, 4])  # r[4]+=r[1]
    [1256, True, 940, 940, 15, 939]
    16 mulr(registers, ['mulr', 4, 4, 4])  # r[4]*=r[4]
    [1256, True, 940, 940, 256, 939]

    r[0] is the sum of all factors of r[5] when set
    '''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_19.txt', 'r')
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
