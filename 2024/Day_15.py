import argparse

from itertools import product


def parse_input(input_string):
    map_data, move_data = input_string.split("\n\n")
    warehouse_map = list(map(list, map_data.split('\n')))
    x_range = len(warehouse_map)
    y_range = len(warehouse_map[0])
    pos = (0, 0)
    for x, y in product(range(x_range), range(y_range)):
        if warehouse_map[x][y] == '@':
            pos = (x, y)
            warehouse_map[x][y] = '.'
            break
    movements = list(move_data.replace('\n',''))
    return warehouse_map, x_range, y_range, pos, movements


def part_1(input_string):
    warehouse_map, x_range, y_range, pos, movements = parse_input(input_string)
    # No range check 0 <= front_pos[0] < x_range and 0 <= front_pos[1] < y_range
    # Since warehouse is surounded by '#'
    for movement in movements:
        front_pos = pos
        fronts = []
        if movement == '^':
            front_pos = (pos[0]-1,pos[1])
            while warehouse_map[front_pos[0]][front_pos[1]] == 'O':
                fronts.append(front_pos)
                front_pos = (front_pos[0]-1,front_pos[1])
        elif movement == '>':
            front_pos = (pos[0],pos[1]+1)
            while warehouse_map[front_pos[0]][front_pos[1]] == 'O':
                fronts.append(front_pos)
                front_pos = (front_pos[0],front_pos[1]+1)
        elif movement == 'v':
            front_pos = (pos[0]+1,pos[1])
            while warehouse_map[front_pos[0]][front_pos[1]] == 'O':
                fronts.append(front_pos)
                front_pos = (front_pos[0]+1,front_pos[1])
        elif movement == '<':
            front_pos = (pos[0],pos[1]-1)
            while warehouse_map[front_pos[0]][front_pos[1]] == 'O':
                fronts.append(front_pos)
                front_pos = (front_pos[0],front_pos[1]-1)
        # print(movement, pos, front_pos, fronts)
        if warehouse_map[front_pos[0]][front_pos[1]] == '.':
            if len(fronts) == 0:
                pos = front_pos
                continue

            if movement == '^':
                fronts.sort(key=lambda f: f[0])
                warehouse_map[fronts[-1][0]][fronts[-1][1]] = '.'
                warehouse_map[front_pos[0]][front_pos[1]] = 'O'
                pos = fronts[-1]
            elif movement == '>':
                fronts.sort(key=lambda f: f[1])
                warehouse_map[front_pos[0]][front_pos[1]] = 'O'
                warehouse_map[fronts[0][0]][fronts[0][1]] = '.'
                pos = fronts[0]
            elif movement == 'v':
                fronts.sort(key=lambda f: f[0])
                warehouse_map[front_pos[0]][front_pos[1]] = 'O'
                warehouse_map[fronts[0][0]][fronts[0][1]] = '.'
                pos = fronts[0]
            elif movement == '<':
                fronts.sort(key=lambda f: f[1])
                warehouse_map[fronts[-1][0]][fronts[-1][1]] = '.'
                warehouse_map[front_pos[0]][front_pos[1]] = 'O'
                pos = fronts[-1]

        # print('\n'.join(list(map(lambda s: ''.join(s), warehouse_map))))
        # import pdb; pdb.set_trace()

    result = 0
    for x, y in product(range(x_range), range(y_range)):
        if warehouse_map[x][y] == 'O':
            result += (100*x+y)
    print(result)


def part_2(input_string):
    warehouse_map, x_range, y_range, pos, movements = parse_input(input_string)
    new_warehouse_map = [[] for _ in range(x_range)]
    for x in range(x_range):
        for y in range(y_range):
            if warehouse_map[x][y] == 'O':
                new_warehouse_map[x] += ['[', ']']
            else:
                new_warehouse_map[x] += [warehouse_map[x][y], warehouse_map[x][y]]
    pos = (pos[0], pos[1]*2)
    y_range *= 2
    # print('\n'.join(list(map(lambda s: ''.join(s), warehouse_map))))
    # print('\n'.join(list(map(lambda s: ''.join(s), new_warehouse_map))))
    for movement in movements:
        # print(movement, pos)
        fronts = []
        if movement == '^':
            front_pos = [(pos[0]-1,pos[1])]
            while any([new_warehouse_map[fp_x][fp_y] in ['[', ']'] for fp_x, fp_y in front_pos]):
                new_front_pos = []
                for fp_x, fp_y in front_pos:
                    if new_warehouse_map[fp_x][fp_y] == '[':
                        fronts += [(fp_x, fp_y), (fp_x, fp_y+1)]
                        new_front_pos += [(fp_x-1,fp_y),(fp_x-1,fp_y+1)]
                    elif new_warehouse_map[fp_x][fp_y] == ']':
                        fronts += [(fp_x, fp_y-1), (fp_x, fp_y)]
                        new_front_pos += [(fp_x-1,fp_y-1),(fp_x-1,fp_y)]
                    else:
                        new_front_pos.append((fp_x, fp_y))
                fronts = list(set(fronts))
                front_pos = list(set(new_front_pos))
            if all([new_warehouse_map[fp_x][fp_y] == '.' for fp_x, fp_y in front_pos]):
                if len(fronts) == 0:
                    pos = front_pos[0]
                else:
                    fronts.sort(key=lambda f: f[0])
                    for fp_x, fp_y in fronts:
                        new_warehouse_map[fp_x-1][fp_y] = new_warehouse_map[fp_x][fp_y]
                        new_warehouse_map[fp_x][fp_y] = '.'
                    pos = (pos[0]-1,pos[1])
        elif movement == '>':
            front_pos = (pos[0],pos[1]+1)
            while new_warehouse_map[front_pos[0]][front_pos[1]] in ['[', ']']:
                fronts.append(front_pos)
                front_pos = (front_pos[0],front_pos[1]+1)
            if new_warehouse_map[front_pos[0]][front_pos[1]] == '.':
                if len(fronts) == 0:
                    pos = front_pos
                else:
                    fronts.sort(key=lambda f: f[1],reverse=True)
                    for fp_x, fp_y in fronts:
                        new_warehouse_map[fp_x][fp_y+1] = new_warehouse_map[fp_x][fp_y]
                        new_warehouse_map[fp_x][fp_y] = '.'
                    pos = (pos[0],pos[1]+1)
        elif movement == 'v':
            front_pos = [(pos[0]+1,pos[1])]
            while any([new_warehouse_map[fp_x][fp_y] in ['[', ']'] for fp_x, fp_y in front_pos]):
                new_front_pos = []
                for fp_x, fp_y in front_pos:
                    if new_warehouse_map[fp_x][fp_y] == '[':
                        fronts += [(fp_x, fp_y), (fp_x, fp_y+1)]
                        new_front_pos += [(fp_x+1,fp_y),(fp_x+1,fp_y+1)]
                    elif new_warehouse_map[fp_x][fp_y] == ']':
                        fronts += [(fp_x, fp_y-1), (fp_x, fp_y)]
                        new_front_pos += [(fp_x+1,fp_y-1),(fp_x+1,fp_y)]
                    else:
                        new_front_pos.append((fp_x, fp_y))
                fronts = list(set(fronts))
                front_pos = list(set(new_front_pos))
            if all([new_warehouse_map[fp_x][fp_y] == '.' for fp_x, fp_y in front_pos]):
                if len(fronts) == 0:
                    pos = front_pos[0]
                else:
                    fronts.sort(key=lambda f: f[0],reverse=True)
                    for fp_x, fp_y in fronts:
                        new_warehouse_map[fp_x+1][fp_y] = new_warehouse_map[fp_x][fp_y]
                        new_warehouse_map[fp_x][fp_y] = '.'
                    pos = (pos[0]+1,pos[1])
        elif movement == '<':
            front_pos = (pos[0],pos[1]-1)
            while new_warehouse_map[front_pos[0]][front_pos[1]] in ['[', ']']:
                fronts.append(front_pos)
                front_pos = (front_pos[0],front_pos[1]-1)
            if new_warehouse_map[front_pos[0]][front_pos[1]] == '.':
                if len(fronts) == 0:
                    pos = front_pos
                else:
                    fronts.sort(key=lambda f: f[1])
                    for fp_x, fp_y in fronts:
                        new_warehouse_map[fp_x][fp_y-1] = new_warehouse_map[fp_x][fp_y]
                        new_warehouse_map[fp_x][fp_y] = '.'
                    pos = (pos[0],pos[1]-1)

        # print(front_pos, fronts)
        # print('\n'.join(list(map(lambda s: ''.join(s), new_warehouse_map))))
    result = 0
    for x, y in product(range(x_range), range(y_range)):
        if new_warehouse_map[x][y] == '[':
            result += (100*x+y)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_15.txt', 'r')
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
