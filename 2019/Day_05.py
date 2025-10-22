import argparse


def run_program_v2(codes, input_num):
    cur = 0
    outputs = []
    while True:
        opcode = codes[cur] % 100
        if opcode == 99:
            cur += 1
            break
        elif opcode == 1:
            mode_num = codes[cur] // 100
            if (mode_num % 10) == 0:
                input_0 = codes[codes[cur+1]]
            elif (mode_num % 10) == 1:
                input_0 = codes[cur+1]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                input_1 = codes[codes[cur+2]]
            elif (mode_num % 10) == 1:
                input_1 = codes[cur+2]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                output_id = codes[cur+3]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            codes[output_id] = input_0 + input_1
            cur += 4
        elif opcode == 2:
            mode_num = codes[cur] // 100
            if (mode_num % 10) == 0:
                input_0 = codes[codes[cur+1]]
            elif (mode_num % 10) == 1:
                input_0 = codes[cur+1]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                input_1 = codes[codes[cur+2]]
            elif (mode_num % 10) == 1:
                input_1 = codes[cur+2]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                output_id = codes[cur+3]
            else:
                print(cur, codes[cur:cur+4], mode_num)
            codes[output_id] = input_0 * input_1
            cur += 4
        elif opcode == 3:
            mode_num = codes[cur] // 100
            if (mode_num % 10) == 0:
                codes[codes[cur+1]] = input_num
            else:
                print(cur, codes[cur:cur+4], mode_num)
            cur += 2
        elif opcode == 4:
            mode_num = codes[cur] // 100
            if (mode_num % 10) == 0:
                outputs.append(codes[codes[cur+1]])
            elif (mode_num % 10) == 1:
                outputs.append(codes[cur+1])
            else:
                print(cur, codes[cur:cur+4], mode_num)
            cur += 2
        else:
            print(cur, opcode)
    return codes, outputs


def run_program_v3(codes, input_num):
    cur = 0
    outputs = []
    while True:
        opcode = codes[cur] % 100
        if opcode == 99:
            cur += 1
            break
        elif opcode == 1:
            mode_num = codes[cur] // 100
            if (mode_num % 10) == 0:
                input_0 = codes[codes[cur+1]]
            elif (mode_num % 10) == 1:
                input_0 = codes[cur+1]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                input_1 = codes[codes[cur+2]]
            elif (mode_num % 10) == 1:
                input_1 = codes[cur+2]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                output_id = codes[cur+3]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            codes[output_id] = input_0 + input_1
            cur += 4
        elif opcode == 2:
            mode_num = codes[cur] // 100
            if (mode_num % 10) == 0:
                input_0 = codes[codes[cur+1]]
            elif (mode_num % 10) == 1:
                input_0 = codes[cur+1]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                input_1 = codes[codes[cur+2]]
            elif (mode_num % 10) == 1:
                input_1 = codes[cur+2]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                output_id = codes[cur+3]
            else:
                print(cur, codes[cur:cur+4], mode_num)
            codes[output_id] = input_0 * input_1
            cur += 4
        elif opcode == 3:
            mode_num = codes[cur] // 100
            if (mode_num % 10) == 0:
                codes[codes[cur+1]] = input_num
            else:
                print(cur, codes[cur:cur+4], mode_num)
            cur += 2
        elif opcode == 4:
            mode_num = codes[cur] // 100
            if (mode_num % 10) == 0:
                outputs.append(codes[codes[cur+1]])
            elif (mode_num % 10) == 1:
                outputs.append(codes[cur+1])
            else:
                print(cur, codes[cur:cur+4], mode_num)
            cur += 2
        elif opcode == 5:
            mode_num = codes[cur] // 100
            if (mode_num % 10) == 0:
                input_0 = codes[codes[cur+1]]
            elif (mode_num % 10) == 1:
                input_0 = codes[cur+1]
            else:
                print(cur, codes[cur:cur+4], mode_num)
            
            mode_num //= 10
            if (mode_num % 10) == 0:
                output = codes[codes[cur+2]]
            elif (mode_num % 10) == 1:
                output = codes[cur+2]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            if input_0 != 0:
                cur = output
            else:
                cur += 3
        elif opcode == 6:
            mode_num = codes[cur] // 100
            if (mode_num % 10) == 0:
                input_0 = codes[codes[cur+1]]
            elif (mode_num % 10) == 1:
                input_0 = codes[cur+1]
            else:
                print(cur, codes[cur:cur+4], mode_num)
            
            mode_num //= 10
            if (mode_num % 10) == 0:
                output = codes[codes[cur+2]]
            elif (mode_num % 10) == 1:
                output = codes[cur+2]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            if input_0 == 0:
                cur = output
            else:
                cur += 3
        elif opcode == 7:
            mode_num = codes[cur] // 100
            if (mode_num % 10) == 0:
                input_0 = codes[codes[cur+1]]
            elif (mode_num % 10) == 1:
                input_0 = codes[cur+1]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                input_1 = codes[codes[cur+2]]
            elif (mode_num % 10) == 1:
                input_1 = codes[cur+2]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                output_id = codes[cur+3]
            else:
                print(cur, codes[cur:cur+4], mode_num)
            codes[output_id] = (input_0 < input_1)
            cur += 4
        elif opcode == 8:
            mode_num = codes[cur] // 100
            if (mode_num % 10) == 0:
                input_0 = codes[codes[cur+1]]
            elif (mode_num % 10) == 1:
                input_0 = codes[cur+1]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                input_1 = codes[codes[cur+2]]
            elif (mode_num % 10) == 1:
                input_1 = codes[cur+2]
            else:
                print(cur, codes[cur:cur+4], mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                output_id = codes[cur+3]
            else:
                print(cur, codes[cur:cur+4], mode_num)
            codes[output_id] = (input_0 == input_1)
            cur += 4
        else:
            print(cur, opcode)
    return codes, outputs


def part_1(input_string):
    codes = list(map(int, input_string.split(',')))
    codes, outputs = run_program_v2(codes, input_num=1)
    print(outputs[-1])


def part_2(input_string):
    codes = list(map(int, input_string.split(',')))
    codes, outputs = run_program_v3(codes, input_num=5)
    print(outputs[-1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_05.txt', 'r')
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
