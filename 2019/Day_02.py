import argparse


def run_program(codes):
    for i in range(0, len(codes), 4):
        opcode, input_0, input_1, output = codes[i:i+4]
        if opcode == 99:
            break
        elif opcode == 1:
            codes[output] = codes[input_0] + codes[input_1]
        elif opcode == 2:
            codes[output] = codes[input_0] * codes[input_1]
        else:
            print(i, opcode, input_0, input_1, output)
    return codes


def part_1(input_string):
    codes = list(map(int, input_string.split(',')))
    codes[1] = 12
    codes[2] = 2
    codes = run_program(codes)
    print(codes[0])


def part_2(input_string):
    noun = 0
    verb = 0
    codes = list(map(int, input_string.split(',')))
    codes[1] = noun
    codes[2] = verb
    codes = run_program(codes)
    while codes[0] != 19690720:
        verb += 1
        if verb > 99:
            verb = 0
            noun += 1
        codes = list(map(int, input_string.split(',')))
        codes[1] = noun
        codes[2] = verb
        codes = run_program(codes)
    print(noun*100+verb)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_02.txt', 'r')
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
