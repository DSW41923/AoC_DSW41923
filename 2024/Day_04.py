import argparse


def part_1(input_string):
    chars = list(map(list, input_string.split('\n')))
    x_range = len(chars)
    y_range = len(chars[0])
    result = 0
    for x in range(x_range):
        for y in range(y_range):
            if chars[x][y] != 'X':
                continue
            candidates = []
            if x >= 3:
                candidates.append(''.join([chars[x][y], chars[x-1][y], chars[x-2][y], chars[x-3][y]]))
                if y >= 3:
                    candidates.append(''.join([chars[x][y], chars[x-1][y-1], chars[x-2][y-2], chars[x-3][y-3]]))
                if y < y_range - 3:
                    candidates.append(''.join([chars[x][y], chars[x-1][y+1], chars[x-2][y+2], chars[x-3][y+3]]))
            if x < x_range - 3:
                candidates.append(''.join([chars[x][y], chars[x+1][y], chars[x+2][y], chars[x+3][y]]))
                if y >= 3:
                    candidates.append(''.join([chars[x][y], chars[x+1][y-1], chars[x+2][y-2], chars[x+3][y-3]]))
                if y < y_range - 3:
                    candidates.append(''.join([chars[x][y], chars[x+1][y+1], chars[x+2][y+2], chars[x+3][y+3]]))
            if y >= 3:
                candidates.append(''.join([chars[x][y], chars[x][y-1], chars[x][y-2], chars[x][y-3]]))
            if y < y_range - 3:
                candidates.append(''.join([chars[x][y], chars[x][y+1], chars[x][y+2], chars[x][y+3]]))
            result += candidates.count('XMAS')
    print(result)


def part_2(input_string):
    chars = list(map(list, input_string.split('\n')))
    x_range = len(chars)
    y_range = len(chars[0])
    result = 0
    for x in range(x_range):
        for y in range(y_range):
            if chars[x][y] != 'A':
                continue
            candidates = []
            if 1 <= x < x_range - 1 and 1 <= y < y_range - 1:
                candidates.append(''.join([chars[x-1][y-1], chars[x][y], chars[x+1][y+1]]))
                candidates.append(''.join([chars[x+1][y-1], chars[x][y], chars[x-1][y+1]]))
            if candidates.count('MAS') + candidates.count('SAM') == 2:
                result += 1
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_04.txt', 'r')
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
