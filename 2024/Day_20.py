import argparse
import heapq

# from copy import deepcopy
from itertools import product


def parse_input(input_string):
    race_map = list(map(list, input_string.split('\n')))
    x_range = len(race_map)
    y_range = len(race_map[0])
    start = None
    end = None
    for x, y in product(range(x_range), range(y_range)):
        if race_map[x][y] == 'S':
            start = (x, y)
        if race_map[x][y] == 'E':
            end = (x, y)
        if start and end:
            break
    return race_map, x_range, y_range, start, end


def get_next_fronts(x, x_range, y, y_range):
    adjacent = []
    if x > 0:
        adjacent.append((x-1,y))
    if x < x_range-1:
        adjacent.append((x+1,y))
    if y > 0:
        adjacent.append((x,y-1))
    if y < y_range-1:
        adjacent.append((x,y+1))
    return adjacent


def race(race_map, x_range, y_range, start, end):
    fronts = [(0, start, [])]
    while fronts:
        step, pos, visited = heapq.heappop(fronts)
        visited.append(pos)
        if pos == end:
            return step, visited
        pos_x, pos_y = pos
        next_fronts = get_next_fronts(pos_x, x_range, pos_y, y_range)
        # if pos not in [start, end]:
        #     if (len([ 1 for x, y in next_fronts if race_map[x][y] != '#']) != 2):
        #         print(pos)
        #         print([race_map[x][y] != '#' for x, y in next_fronts])
        #         return

        for next_pos in next_fronts:
            if next_pos in visited:
                continue
            next_pos_x, next_pos_y = next_pos
            if race_map[next_pos_x][next_pos_y] == '#':
                continue
            # if race_map[next_pos_x][next_pos_y] == '1' and race_map[pos_x][pos_y] == '2':
            #     continue
            new_step = step + 1
            heapq.heappush(fronts, (new_step, next_pos, visited))
    

def part_1(input_string):
    race_map, x_range, y_range, start, end = parse_input(input_string)
    _, visited = race(race_map, x_range, y_range, start, end)
    # for x, y in product(range(x_range), range(y_range)):
    #     if race_map[x][y] != '#' and (x,y) not in visited:
    #         print(x, y)
    # print(("!!"))
    result = 0
    for id, pos in enumerate(visited[:len(visited)-102]):
        x_0, y_0 = pos
        for x, y in visited[id+102:]:
            if abs(x-x_0)+abs(y-y_0) == 2:
                result += 1
    # for id, pos in enumerate(visited):
    #     x, y = pos
    #     if x > 1:
    #         if race_map[x-1][y] == '#' and race_map[x-2][y] != '#':
    #             if visited.index((x-2, y)) - id >= 102:
    #                 result += 1

    #     if x < x_range-2:
    #         if race_map[x+1][y] == '#' and race_map[x+2][y] != '#':
    #             if visited.index((x+2, y)) - id >= 102:
    #                 result += 1
    #     if y > 1:
    #         if race_map[x][y-1] == '#' and race_map[x][y-2] != '#':
    #             if visited.index((x, y-2)) - id >= 102:
    #                 result += 1
    #     if y < y_range-2:
    #         if race_map[x][y+1] == '#' and race_map[x][y+2] != '#':
    #             if visited.index((x, y+2)) - id >= 102:
    #                 result += 1
    print(result)


def part_2(input_string):
    race_map, x_range, y_range, start, end = parse_input(input_string)
    _, visited = race(race_map, x_range, y_range, start, end)
    result = 0
    for i in range(2, 21):
        for id, pos in enumerate(visited[:len(visited)-(100+i)]):
            x_0, y_0 = pos
            for x, y in visited[id+(100+i):]:
                if abs(x-x_0)+abs(y-y_0) == i:
                    result += 1
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_20.txt', 'r')
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
