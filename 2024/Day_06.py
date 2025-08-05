import argparse

from copy import deepcopy

def get_map_data(input_string):
    patrol_map = list(map(list, input_string.split('\n')))
    max_x = len(patrol_map)
    max_y = len(patrol_map[0])
    pos = (0, 0)
    for x in range(max_x):
        for y in range(max_y):
            if patrol_map[x][y] == '^':
                pos = (x, y)
                break
        if pos != (0, 0):
            break
    return patrol_map, max_x, max_y, pos



def get_next_pos(pos, facing):
    if facing == 0:
        return (pos[0]-1, pos[1])
    elif facing == 1:
        return (pos[0], pos[1]+1)
    elif facing == 2:
        return (pos[0]+1, pos[1])
    elif facing == 3:
        return (pos[0], pos[1]-1)

def get_visited(patrol_map, max_x, max_y, start_pos):
    pos = start_pos
    facing = 0
    visited = []
    while True:
        if pos not in visited:
            visited.append(pos)
        next_pos = get_next_pos(pos, facing)
        if not(0 <= next_pos[0] < max_x and 0 <= next_pos[1] < max_y):
            break
        if patrol_map[next_pos[0]][next_pos[1]] == '#':
            facing += 1
            facing %= 4
        else:
            pos = next_pos
    return visited


def part_1(input_string):
    patrol_map, max_x, max_y, pos = get_map_data(input_string)
    print(len(get_visited(patrol_map, max_x, max_y, pos)))


def part_2(input_string):
    patrol_map, max_x, max_y, pos = get_map_data(input_string)
    visited = get_visited(patrol_map, max_x, max_y, pos)
    obstruction_pos_count = 0
    for x, y in visited:
        if (x, y) == pos:
            continue
        new_patrol_map = deepcopy(patrol_map)
        new_patrol_map[x][y] = '#'
        cur_pos = (pos[0], pos[1])
        facing = 0
        visited_status = []
        is_loop = True
        while (cur_pos, facing) not in visited_status:
            visited_status.append((cur_pos, facing))
            next_pos = get_next_pos(cur_pos, facing)
            if not(0 <= next_pos[0] < max_x and 0 <= next_pos[1] < max_y):
                is_loop = False
                break
            if new_patrol_map[next_pos[0]][next_pos[1]] == '#':
                facing += 1
                facing %= 4
            else:
                cur_pos = next_pos
        if is_loop:
            obstruction_pos_count += 1
    print(obstruction_pos_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_06.txt', 'r')
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
