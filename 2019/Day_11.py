import argparse


def run_program_v7(cur, relative_offset, codes, input_num):
    output_value = None
    while True:
        cur_value = codes.get(cur, 0)
        # print(cur, cur_value, codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), relative_offset)
        opcode = cur_value % 100
        if opcode == 99:
            output_value = None
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
                output_value = codes.get(output_id, 0)
            elif (mode_num % 10) == 1:
                output_value = codes.get(cur+1, 0)
            elif (mode_num % 10) == 2:
                output_id = relative_offset+codes.get(cur+1, 0)
                output_value = codes.get(output_id, 0)
            else:
                print(cur, codes.get(cur, 0), codes.get(cur+1, 0), codes.get(cur+2, 0), codes.get(cur+3, 0), mode_num)
            output_value = int(output_value)
            cur += 2
            break
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
            import pdb; pdb.set_trace()
    return cur, relative_offset, codes, output_value


def parse_data(input_string):
    codes = list(map(int, input_string.split(',')))
    codes_dict = {}
    for i, c in enumerate(codes):
        codes_dict.update({
            i: c
        })
    return codes_dict


def paint_panel(codes_dict, start_color=0):
    painted_panels = {}
    facing_options = [1j, 1, -1j, -1]
    cur = 0
    relative_offset = 0
    pos = 0
    facing = 1j
    output = 1
    if start_color:
        painted_panels[pos] = start_color
    while output != None:
        input_num = 0
        if pos in painted_panels:
            input_num = painted_panels[pos]

        cur, relative_offset, codes_dict, output = run_program_v7(cur, relative_offset, codes_dict, input_num)
        if output == 1:
            if pos in painted_panels:
                painted_panels[pos] = 1
            else:
                painted_panels.update({pos: 1})
        elif output == 0:
            if pos in painted_panels:
                painted_panels[pos] = 0
            else:
                painted_panels.update({pos: 0})
        elif output is None:
            break
        else:
            print(output)
            import pdb; pdb.set_trace()

        cur, relative_offset, codes_dict, output = run_program_v7(cur, relative_offset, codes_dict, input_num)
        if output == 0:
            facing = facing_options[(facing_options.index(facing)-1)%4]
        elif output == 1:
            facing = facing_options[(facing_options.index(facing)+1)%4]
        else:
            print(output)
            import pdb; pdb.set_trace()
        pos += facing
    return painted_panels


def part_1(input_string):
    codes_dict = parse_data(input_string)
    painted_panels = paint_panel(codes_dict)
    print(len(painted_panels.keys()))


def part_2(input_string):
    codes_dict = parse_data(input_string)
    painted_panels = paint_panel(codes_dict, start_color=1)
    white_panels = [(int(k.real), -int(k.imag)) for k in painted_panels.keys() if painted_panels[k] == 1]
    min_x = min(white_panels, key=lambda p:p[0])[0]
    min_y = min(white_panels, key=lambda p:p[1])[1]
    white_panels = [(p[0]-min_x, p[1]-min_y) for p in white_panels]
    min_x = min(white_panels, key=lambda p:p[0])[0]
    max_x = max(white_panels, key=lambda p:p[0])[0]
    min_y = min(white_panels, key=lambda p:p[1])[1]
    max_y = max(white_panels, key=lambda p:p[1])[1]
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in white_panels:
                print('#', end='')
                continue
            print('.', end='')
        print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_11.txt', 'r')
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
