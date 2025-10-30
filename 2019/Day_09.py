import argparse


def run_program_v6(codes, input_num):
    cur = 0
    relative_offset = 0
    outputs = []
    while True:
        cur_value = codes.get(cur, 0)
        # print(cur, cur_value, codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), relative_offset)
        opcode = cur_value % 100
        if opcode == 99:
            cur += 1
            break
        elif opcode == 1:
            mode_num = cur_value // 100
            if (mode_num % 10) == 0:
                input_0_id = codes.get(cur+1, 0)
                input_0 = codes.get(input_0_id, 0)
            elif (mode_num % 10) == 1:
                input_0 = codes.get(cur+1, 0)
            elif (mode_num % 10) == 2:
                input_0_id = relative_offset+codes.get(cur+1, 0)
                input_0 = codes.get(input_0_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                input_1_id = codes.get(cur+2, 0)
                input_1 = codes.get(input_1_id, 0)
            elif (mode_num % 10) == 1:
                input_1 = codes.get(cur+2, 0)
            elif (mode_num % 10) == 2:
                input_1_id = relative_offset+codes.get(cur+2, 0)
                input_1 = codes.get(input_1_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                output_id = codes.get(cur+3, 0)
            elif (mode_num % 10) == 2:
                output_id = relative_offset+codes.get(cur+3, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)

            codes[output_id] = input_0 + input_1
            cur += 4
        elif opcode == 2:
            mode_num = cur_value // 100
            if (mode_num % 10) == 0:
                input_0_id = codes.get(cur+1, 0)
                input_0 = codes.get(input_0_id, 0)
            elif (mode_num % 10) == 1:
                input_0 = codes.get(cur+1, 0)
            elif (mode_num % 10) == 2:
                input_0_id = relative_offset+codes.get(cur+1, 0)
                input_0 = codes.get(input_0_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                input_1_id = codes.get(cur+2, 0)
                input_1 = codes.get(input_1_id, 0)
            elif (mode_num % 10) == 1:
                input_1 = codes.get(cur+2, 0)
            elif (mode_num % 10) == 2:
                input_1_id = relative_offset+codes.get(cur+2, 0)
                input_1 = codes.get(input_1_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                output_id = codes.get(cur+3, 0)
            elif (mode_num % 10) == 2:
                output_id = relative_offset+codes.get(cur+3, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)
            codes[output_id] = input_0 * input_1
            cur += 4
        elif opcode == 3:
            mode_num = cur_value // 100
            if (mode_num % 10) == 0:
                target_id = codes.get(cur+1, 0)
                codes.update({target_id: input_num})
            elif (mode_num % 10) == 2:
                target_id = relative_offset+codes.get(cur+1, 0)
                codes.update({target_id: input_num})
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)
            cur += 2
        elif opcode == 4:
            mode_num = cur_value // 100
            if (mode_num % 10) == 0:
                output_id = codes.get(cur+1, 0)
                output = codes.get(output_id, 0)
                outputs.append(output)
            elif (mode_num % 10) == 1:
                outputs.append(codes.get(cur+1, 0))
            elif (mode_num % 10) == 2:
                output_id = relative_offset+codes.get(cur+1, 0)
                output = codes.get(output_id, 0)
                outputs.append(output)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)
            cur += 2
        elif opcode == 5:
            mode_num = cur_value // 100
            if (mode_num % 10) == 0:
                input_0_id = codes.get(cur+1, 0)
                input_0 = codes.get(input_0_id, 0)
            elif (mode_num % 10) == 1:
                input_0 = codes.get(cur+1, 0)
            elif (mode_num % 10) == 2:
                input_0_id = relative_offset+codes.get(cur+1, 0)
                input_0 = codes.get(input_0_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)
            
            mode_num //= 10
            if (mode_num % 10) == 0:
                output_id = codes.get(cur+2, 0)
                output = codes.get(output_id, 0)
            elif (mode_num % 10) == 1:
                output = codes.get(cur+2, 0)
            elif (mode_num % 10) == 2:
                output_id = relative_offset+codes.get(cur+2, 0)
                output = codes.get(output_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)

            if input_0 != 0:
                cur = output
            else:
                cur += 3
        elif opcode == 6:
            mode_num = cur_value // 100
            if (mode_num % 10) == 0:
                input_0_id = codes.get(cur+1, 0)
                input_0 = codes.get(input_0_id, 0)
            elif (mode_num % 10) == 1:
                input_0 = codes.get(cur+1, 0)
            elif (mode_num % 10) == 2:
                input_0_id = relative_offset+codes.get(cur+1, 0)
                input_0 = codes.get(input_0_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)
            
            mode_num //= 10
            if (mode_num % 10) == 0:
                output_id = codes.get(cur+2, 0)
                output = codes.get(output_id, 0)
            elif (mode_num % 10) == 1:
                output = codes.get(cur+2, 0)
            elif (mode_num % 10) == 2:
                output_id = relative_offset+codes.get(cur+2, 0)
                output = codes.get(output_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)

            if input_0 == 0:
                cur = output
            else:
                cur += 3
        elif opcode == 7:
            mode_num = cur_value // 100
            if (mode_num % 10) == 0:
                input_0_id = codes.get(cur+1, 0)
                input_0 = codes.get(input_0_id, 0)
            elif (mode_num % 10) == 1:
                input_0 = codes.get(cur+1, 0)
            elif (mode_num % 10) == 2:
                input_0_id = relative_offset+codes.get(cur+1, 0)
                input_0 = codes.get(input_0_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                input_1_id = codes.get(cur+2, 0)
                input_1 = codes.get(input_1_id, 0)
            elif (mode_num % 10) == 1:
                input_1 = codes.get(cur+2, 0)
            elif (mode_num % 10) == 2:
                input_1_id = relative_offset+codes.get(cur+2, 0)
                input_1 = codes.get(input_1_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                output_id = codes.get(cur+3, 0)
            elif (mode_num % 10) == 2:
                output_id = relative_offset+codes.get(cur+3, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)
            codes[output_id] = (input_0 < input_1)
            cur += 4
        elif opcode == 8:
            mode_num = cur_value // 100
            if (mode_num % 10) == 0:
                input_0_id = codes.get(cur+1, 0)
                input_0 = codes.get(input_0_id, 0)
            elif (mode_num % 10) == 1:
                input_0 = codes.get(cur+1, 0)
            elif (mode_num % 10) == 2:
                input_0_id = relative_offset+codes.get(cur+1, 0)
                input_0 = codes.get(input_0_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                input_1_id = codes.get(cur+2, 0)
                input_1 = codes.get(input_1_id, 0)
            elif (mode_num % 10) == 1:
                input_1 = codes.get(cur+2, 0)
            elif (mode_num % 10) == 2:
                input_1_id = relative_offset+codes.get(cur+2, 0)
                input_1 = codes.get(input_1_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)

            mode_num //= 10
            if (mode_num % 10) == 0:
                output_id = codes.get(cur+3, 0)
            elif (mode_num % 10) == 2:
                output_id = relative_offset+codes.get(cur+3, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)
            codes[output_id] = (input_0 == input_1)
            cur += 4
        elif opcode == 9:
            mode_num = cur_value // 100
            if (mode_num % 10) == 0:
                value_id = codes.get(cur+1, 0)
                value = codes.get(value_id, 0)
            elif (mode_num % 10) == 1:
                value = codes.get(cur+1, 0)
            elif (mode_num % 10) == 2:
                value_id = relative_offset+codes.get(cur+1, 0)
                value = codes.get(value_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)

            relative_offset += value
            cur += 2
        else:
            print(cur, opcode)
    return codes, outputs


def part_1(input_string):
    codes = list(map(int, input_string.split(',')))
    codes_dict = {}
    for i, c in enumerate(codes):
        codes_dict.update({
            i: c
        })
    codes_dict, outputs = run_program_v6(codes_dict, input_num=1)
    print(outputs[-1])


def part_2(input_string):
    codes = list(map(int, input_string.split(',')))
    codes_dict = {}
    for i, c in enumerate(codes):
        codes_dict.update({
            i: c
        })
    codes_dict, outputs = run_program_v6(codes_dict, input_num=2)
    print(outputs[-1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_09.txt', 'r')
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
