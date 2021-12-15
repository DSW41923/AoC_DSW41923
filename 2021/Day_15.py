import argparse

from math import inf


def get_risk_sum_map(risk_level_map):
    max_x, max_y = len(risk_level_map) - 1, len(risk_level_map[0]) - 1
    risk_sum_map = [[inf for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    front = [(0, 0)]
    risk_sum_map[0][0] = 0
    while front:
        u_x, u_y = front[0]
        del front[0]

        possible_pos = []
        if u_x > 0:
            possible_pos.append((u_x - 1, u_y))
        if u_x < max_x:
            possible_pos.append((u_x + 1, u_y))
        if u_y > 0:
            possible_pos.append((u_x, u_y - 1))
        if u_y < max_y:
            possible_pos.append((u_x, u_y + 1))

        for pos_x, pos_y in possible_pos:
            old_risk_sum = risk_sum_map[pos_x][pos_y]
            risk_sum_map[pos_x][pos_y] = min(risk_sum_map[u_x][u_y] + risk_level_map[pos_x][pos_y],
                                             risk_sum_map[pos_x][pos_y])
            if risk_sum_map[pos_x][pos_y] != old_risk_sum:
                front.append((pos_x, pos_y))

    return risk_sum_map


def part_1(input_string):
    risk_level_map = [list(map(int, line)) for line in list(map(list, input_string.split('\n')))]
    risk_sum_map = get_risk_sum_map(risk_level_map)
    print(risk_sum_map[-1][-1])


def part_2(input_string):
    risk_level_map = [list(map(int, line)) for line in list(map(list, input_string.split('\n')))]
    x_range, y_range = len(risk_level_map), len(risk_level_map[0])
    real_risk_level_map = [[0 for _ in range(y_range * 5)] for _ in range(x_range * 5)]
    for x in range(len(real_risk_level_map)):
        for y in range(len(real_risk_level_map[0])):
            real_risk_level_map[x][y] = (risk_level_map[x % x_range][y % y_range] +
                                         x // len(risk_level_map) + y // len(risk_level_map[0]))
            if real_risk_level_map[x][y] > 9:
                real_risk_level_map[x][y] -= 9
    risk_sum_map = get_risk_sum_map(real_risk_level_map)
    print(risk_sum_map[-1][-1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_15.txt', 'r')
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
