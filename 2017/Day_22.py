import argparse


def part_1(input_string):
    nodes = list(map(list, input_string.split('\n')))
    cur = (len(nodes) // 2, len(nodes[0]) // 2, 0)
    bursts = 10000
    for node in nodes:
        node.extend(['.' for _ in range(100 - len(node))])
    while len(nodes) < 100:
        nodes.append(['.' for _ in range(100)])

    infected_count = 0
    for _ in range(bursts):
        cur_x, cur_y, cur_facing = cur
        if nodes[cur_x][cur_y] == '#':
            cur_facing = (cur_facing + 1) % 4
        elif nodes[cur_x][cur_y] == '.':
            cur_facing = (cur_facing - 1) % 4

        if nodes[cur_x][cur_y] == '#':
            nodes[cur_x][cur_y] = '.'
        elif nodes[cur_x][cur_y] == '.':
            nodes[cur_x][cur_y] = '#'
            infected_count += 1

        if cur_facing == 0:
            cur = (cur_x - 1, cur_y, cur_facing)
        elif cur_facing == 1:
            cur = (cur_x, cur_y + 1, cur_facing)
        elif cur_facing == 2:
            cur = (cur_x + 1, cur_y, cur_facing)
        elif cur_facing == 3:
            cur = (cur_x, cur_y - 1, cur_facing)
        else:
            raise

    print(infected_count)


def part_2(input_string):
    nodes = list(map(list, input_string.split('\n')))
    cur = (len(nodes) // 2, len(nodes[0]) // 2, 0)
    bursts = 10000000
    for node in nodes:
        node.extend(['.' for _ in range(1000 - len(node))])
    while len(nodes) < 1000:
        nodes.append(['.' for _ in range(1000)])

    infected_count = 0
    for _ in range(bursts):
        cur_x, cur_y, cur_facing = cur
        if nodes[cur_x][cur_y] == '#':
            cur_facing = (cur_facing + 1) % 4
        elif nodes[cur_x][cur_y] == '.':
            cur_facing = (cur_facing - 1) % 4
        elif nodes[cur_x][cur_y] == '+':
            cur_facing = (cur_facing - 2) % 4
        elif nodes[cur_x][cur_y] == '-':
            cur_facing = cur_facing
            # Keep direction

        if nodes[cur_x][cur_y] == '#':
            nodes[cur_x][cur_y] = '+'
        elif nodes[cur_x][cur_y] == '+':
            nodes[cur_x][cur_y] = '.'
        elif nodes[cur_x][cur_y] == '.':
            nodes[cur_x][cur_y] = '-'
        elif nodes[cur_x][cur_y] == '-':
            nodes[cur_x][cur_y] = '#'
            infected_count += 1

        if cur_facing == 0:
            cur = (cur_x - 1, cur_y, cur_facing)
        elif cur_facing == 1:
            cur = (cur_x, cur_y + 1, cur_facing)
        elif cur_facing == 2:
            cur = (cur_x + 1, cur_y, cur_facing)
        elif cur_facing == 3:
            cur = (cur_x, cur_y - 1, cur_facing)
        else:
            raise

    print(infected_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2017/Input_22.txt', 'r')
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
