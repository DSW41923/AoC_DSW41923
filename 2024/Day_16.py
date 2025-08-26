import argparse
import heapq

from itertools import product


def parse_input(input_string):
    maze = list(map(list, input_string.split('\n')))
    x_range = len(maze)
    y_range = len(maze[0])
    start = None
    end = None
    for x, y in product(range(x_range), range(y_range)):
        if maze[x][y] == 'S':
            start = (x, y)
        if maze[x][y] == 'E':
            end = (x, y)
        if start and end:
            break
    return maze, x_range, y_range, start, end


def get_next_adjacent(x, x_range, y, y_range, facing):
    adjacent = []
    if x > 0 and facing != 'S':
        adjacent.append(((1000*(facing!='N'),(x-1,y),'N')))
    if x < x_range-1 and facing != 'N':
        adjacent.append((1000*(facing!='S'),(x+1,y),'S'))
    if y > 0 and facing != 'E':
        adjacent.append((1000*(facing!='W'),(x,y-1),'W'))
    if y < y_range-1 and facing != 'W':
        adjacent.append((1000*(facing!='E'),(x,y+1),'E'))
    return adjacent


def part_1(input_string):
    maze, x_range, y_range, start, end = parse_input(input_string)
    scores = {start: 0}
    fronts = [(0, start, 'E')]
    while fronts:
        score, pos, facing = heapq.heappop(fronts)
        pos_x, pos_y = pos
        next_fronts = get_next_adjacent(pos_x, x_range, pos_y, y_range, facing)

        for turn_score, next_pos, new_facing in next_fronts:
            next_pos_x, next_pos_y = next_pos
            if maze[next_pos_x][next_pos_y] == '#':
                continue
            new_score = score + turn_score + 1
            if next_pos in scores:
                old_score = scores[next_pos]
                scores[next_pos] = min(new_score, old_score)
                if scores[next_pos] != old_score:
                    heapq.heappush(fronts, (new_score, next_pos, new_facing))
            else:
                scores.update({
                    next_pos: new_score
                })
                heapq.heappush(fronts, (new_score, next_pos, new_facing))
    print(scores[end])


# from collections import deque

# dir_map = {
#     'u': {'v': (-1, 0), 't': ['l', 'r']}, 'd': {'v': (1, 0), 't': ['l', 'r']},
#     'l': {'v': (0, -1), 't': ['u', 'd']}, 'r': {'v': (0, 1), 't': ['u', 'd']}
# }
    
def part_2(input_string):
    # data = [x for x in input_string.split()]
    # m = len(data)
    # n = len(data[0])
    # maze = {}
    # for i, line in enumerate(data):
    #     for j, char in enumerate(line):
    #         if char == 'S':
    #             maze[(i, j)] = 0
    #             start = (i, j)
    #         elif char == 'E':
    #             maze[(i, j)] = 1000000000000
    #             end = (i, j)
    #         else:
    #             maze[(i, j)] = char
    # maze = maze
    # future_moves, good_spots, maze = deque(), set(), maze

    # def dfs(loc, score, dir, reverse):
    #     if loc in [(1, 115), (2, 115)] and reverse:
    #         print(loc, dir, maze[loc], score)
    #     if maze[loc] == '#' or (isinstance(maze[loc], int) and
    #                             maze[loc] < score and not reverse):
    #         return
    #     if maze[loc] == '.' or maze[loc] > score:
    #         if reverse:
    #             return
    #         maze[loc] = score
    #     if reverse:
    #         good_spots.add(loc)
    #     for n_dr in [dir, *dir_map[dir]['t']]:
    #         n_loc = tuple([loc[i] + dir_map[n_dr]['v'][i] for i in [0, 1]])
    #         dif = (1001 if n_dr != dir else 1) * (-1 if reverse else 1)
    #         future_moves.append([n_loc, score + dif, n_dr, reverse])

    # future_moves.append([start, 0, 'r', False])
    # while future_moves:
    #     dfs(*future_moves.popleft())
    # future_moves.append([end, maze[end], 'd', True])
    # future_moves.append([end, maze[end], 'l', True])
    # while future_moves:
    #     dfs(*future_moves.popleft())
    # print(len(good_spots))
    maze, x_range, y_range, start, end = parse_input(input_string)
    scores = {
        start: 0
    }
    fronts = [(0, start, 'E')]
    while fronts:
        score, pos, facing = heapq.heappop(fronts)
        pos_x, pos_y = pos
        if maze[pos_x][pos_y] == 'E':
            continue
        next_fronts = get_next_adjacent(pos_x, x_range, pos_y, y_range, facing)

        for turn_score, next_pos, new_facing in next_fronts:
            next_pos_x, next_pos_y = next_pos
            if maze[next_pos_x][next_pos_y] == '#':
                continue
            new_score = score + turn_score + 1
            if next_pos in scores:
                if new_score < scores[next_pos]:
                    scores[next_pos] = new_score
                    heapq.heappush(fronts, (new_score, next_pos, new_facing))
            else:
                scores.update({
                    next_pos: new_score
                })
                heapq.heappush(fronts, (new_score, next_pos, new_facing))
    visited = set()
    backward_fronts = [(scores[end], end, 'S'), (scores[end], end, 'W')]
    while backward_fronts:
        score, pos, facing = backward_fronts.pop(0)
        visited.add(pos)
        pos_x, pos_y = pos
        next_fronts = get_next_adjacent(pos_x, x_range, pos_y, y_range, facing)
        for turn_score, next_pos, new_facing in next_fronts:
            x, y = next_pos
            new_score = score - turn_score*(new_facing != facing) - 1
            if maze[x][y] != '#' and (x,y) in scores:
                if scores[(x,y)] <= new_score:
                    backward_fronts.append((new_score, (x,y), new_facing))
    print(len(visited))
    # for v_x, v_y in visited:
    #     maze[v_x][v_y] = 'O'
    # print('\n'.join(list(map(lambda s: ''.join(s), maze))))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_16.txt', 'r')
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
