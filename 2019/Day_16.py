import argparse


def part_1(input_string):
    num_list = list(map(int, list(input_string)))
    num_list_len = len(num_list)
    pattern = [0, 1, 0, -1]
    for i in range(100):
        new_list = [0 for _ in range(num_list_len)]
        for j in range(num_list_len):
            for k in range(num_list_len):
                new_list[j] += (num_list[k] * pattern[((k+1)//(j+1))%4])
            new_list[j] = abs(new_list[j]) % 10
        num_list = new_list
    print(''.join(map(str, num_list[:8])))


def part_2(input_string):
    num_list = list(map(int, list(input_string)))
    num_list_len = len(num_list)
    offset = int(''.join(map(str, num_list[:7])))
    # print(offset)
    num_list = num_list*10000
    full_num_list_len = num_list_len*10000
    # print(full_num_list_len//2)
    # print(offset > full_num_list_len//2)
    full_num_list_len -= offset
    num_list = num_list[-full_num_list_len:]
    # pattern = [0, 1, 0, -1]
    for i in range(100):
        for j in range(2, full_num_list_len+1):
            num_list[-j] += num_list[-j+1]
            num_list[-j] = abs(num_list[-j]) % 10
        # print(i, ''.join(map(str, num_list[:8])))
    print(''.join(map(str, num_list[:8])))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_16.txt', 'r')
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
