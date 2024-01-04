import argparse


def part_1(input_string):
    data_location = int(input_string)
    for i in range(1, data_location):
        if i * (i - 1) * 4 + 1 <= data_location <= i * (i + 1) * 4 + 1:
            start = i * (i - 1) * 4 + 2
            side_len = i * 2
            side_start = start + side_len * ((data_location - start) // side_len)
            print(abs(data_location - (side_start + i)) + i + 1)
            break


def part_2(input_string):
    input_value = int(input_string)
    data = [[0 for _ in range(200)] for _ in range(200)]
    data[0][0] = 1
    cur = (0, 0)
    for i in range(1, 100):
        for j in range(4):
            if j == 0:
                cur = (cur[0] + 1, cur[1])
            elif j == 1:
                cur = (cur[0] - 1, cur[1])
            elif j == 2:
                cur = (cur[0], cur[1] - 1)
            elif j == 3:
                cur = (cur[0] + 1, cur[1])
            data[cur[0]][cur[1]] += data[cur[0] - 1][cur[1] - 1] + data[cur[0] - 1][cur[1]] + data[cur[0] - 1][cur[1] + 1] + \
                data[cur[0]][cur[1] - 1] + data[cur[0]][cur[1] + 1] + \
                data[cur[0] + 1][cur[1] - 1] + data[cur[0] + 1][cur[1]] + data[cur[0] + 1][cur[1] + 1]
            if data[cur[0]][cur[1]] >= input_value:
                print(data[cur[0]][cur[1]])
                return
            side_len = i * 2 - 1
            for _ in range(side_len):
                if j == 0:
                    cur = (cur[0], cur[1] + 1)
                elif j == 1:
                    cur = (cur[0] - 1, cur[1])
                elif j == 2:
                    cur = (cur[0], cur[1] - 1)
                elif j == 3:
                    cur = (cur[0] + 1, cur[1])
                data[cur[0]][cur[1]] += data[cur[0] - 1][cur[1] - 1] + data[cur[0] - 1][cur[1]] + data[cur[0] - 1][cur[1] + 1] + \
                    data[cur[0]][cur[1] - 1] + data[cur[0]][cur[1] + 1] + \
                    data[cur[0] + 1][cur[1] - 1] + data[cur[0] + 1][cur[1]] + data[cur[0] + 1][cur[1] + 1]
                if data[cur[0]][cur[1]] >= input_value:
                    print(data[cur[0]][cur[1]])
                    return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2017/Input_03.txt', 'r')
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
