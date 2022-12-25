import argparse


def parse_bliz_data(map_input):
    bliz_data = {'>': [], 'v': [], '<': [], '^': []}
    for r, row in enumerate(map_input):
            for c, char in enumerate(row):
                if char in bliz_data:
                    bliz_data[char].append((r, c))
    return bliz_data


def move(src, des, bliz_data, max_r, max_c):
    pos = [src]
    i = 0
    while des not in pos:
        # print(i, len(pos), pos[-1])
        new_pos = []
        for bliz, bliz_pos in bliz_data.items():
            if bliz == '>':
                bliz_data[bliz] = [(r, c + 1) if c != max_c else (r, 1) for r, c in bliz_pos]
            if bliz == 'v':
                bliz_data[bliz] = [(r + 1, c) if r != max_r else (1, c) for r, c in bliz_pos]
            if bliz == '<':
                bliz_data[bliz] = [(r, c - 1) if c != 1 else (r, max_c) for r, c in bliz_pos]
            if bliz == '^':
                bliz_data[bliz] = [(r - 1, c) if r != 1 else (max_r, c) for r, c in bliz_pos]
        new_bliz_pos = bliz_data['>'] + bliz_data['v'] + bliz_data['<'] + bliz_data['^']
        for p_r, p_c in pos:
            next_pos = [
                (p_r - 1, p_c),
                (p_r + 1, p_c),
                (p_r, p_c - 1),
                (p_r, p_c + 1),
                (p_r, p_c)
                ]
            for pos_r, pos_c in next_pos:
                if 1 <= pos_r <= max_r and 1 <= pos_c <= max_c or (pos_r, pos_c) in [src, des]:
                    if (pos_r, pos_c) not in new_bliz_pos + new_pos:
                        new_pos.append((pos_r, pos_c))
        i += 1
        pos = new_pos
    return i


def part_1(input_string):
    map_input = list(map(list, input_string.split('\n')[:-1]))
    bliz_data = parse_bliz_data(map_input)
    max_r = len(map_input) - 2
    max_c = len(map_input[0]) - 2
    src = (0, map_input[0].index('.'))
    des = (len(map_input) - 1, map_input[-1].index('.'))
    print(move(src, des, bliz_data, max_r, max_c))


def part_2(input_string):
    map_input = list(map(list, input_string.split('\n')[:-1]))
    bliz_data = parse_bliz_data(map_input)
    max_r = len(map_input) - 2
    max_c = len(map_input[0]) - 2
    src = (0, map_input[0].index('.'))
    des = (len(map_input) - 1, map_input[-1].index('.'))
    i = move(src, des, bliz_data, max_r, max_c) + move(des, src, bliz_data, max_r, max_c) + move(src, des, bliz_data, max_r, max_c)
    print(i)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_24.txt', 'r')
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

