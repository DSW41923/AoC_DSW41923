import argparse

from itertools import permutations

def run_program_v4(codes, phase_setting, input_num):
    cur = 0
    outputs = []
    input_count = 0
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
                if input_count == 0:
                    codes[codes[cur+1]] = phase_setting
                    input_count += 1
                elif input_count == 1:
                    codes[codes[cur+1]] = input_num
                else:
                    print(cur, codes[cur:cur+4], mode_num)
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


def run_program_v5(cur, codes, input_count, phase_setting, input_num):
    while True:
        opcode = codes[cur] % 100
        if opcode == 99:
            cur += 1
            return cur, codes, input_count, None
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
                if input_count == 0:
                    codes[codes[cur+1]] = phase_setting
                    input_count += 1
                else:
                    codes[codes[cur+1]] = input_num
            else:
                print(cur, codes[cur:cur+4], mode_num)
            cur += 2
        elif opcode == 4:
            mode_num = codes[cur] // 100
            if (mode_num % 10) == 0:
                output = codes[codes[cur+1]]
            elif (mode_num % 10) == 1:
                output = codes[cur+1]
            else:
                print(cur, codes[cur:cur+4], mode_num)
            cur += 2
            return cur, codes, input_count, output
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


def part_1(input_string):
    max_signal = 0
    for phase_settings in permutations(range(5), 5):
        amp_input = 0
        for ps in phase_settings:
            codes = list(map(int, input_string.split(',')))
            codes, outputs = run_program_v4(codes, ps, amp_input)
            amp_input = outputs[-1]
        max_signal = max(max_signal, amp_input)
    print(max_signal)


def part_2(input_string):
    max_signal = 0
    for phase_settings in permutations(range(5, 10), 5):
        amp_input = 0
        amplifiers = [(0, tuple(map(int, input_string.split(','))), 0, None) for _ in range(5)]
        final_output = 0
        while True:
            halt_count = 0
            for i, ps in enumerate(phase_settings):
                cur, codes, input_count, last_output = amplifiers[i]
                if input_count > 0 and last_output is None:
                    halt_count += 1
                    continue
                codes = list(codes)
                cur, codes, input_count, output = run_program_v5(cur, codes, input_count, ps, amp_input)
                # print(phase_settings, ps, i, cur, codes, input_count, output)
                amplifiers[i] = (cur, tuple(codes), input_count, output)
                if output:
                    amp_input = output
                    if i == 4:
                        final_output = output
                else:
                    halt_count += 1
            if halt_count == 5:
                break
        max_signal = max(max_signal, final_output)
    print(max_signal)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_07.txt', 'r')
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
