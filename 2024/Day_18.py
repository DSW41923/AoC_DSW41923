import argparse
import heapq
import re


def parse_input(input_string):
    corrupting_bytes = []
    for x, y in re.findall(r"(\d+),(\d+)", input_string):
        corrupting_bytes.append((int(x), int(y)))
    return corrupting_bytes


def get_adjacent(x, x_range, y, y_range):
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


def part_1(input_string):
    corrupting_bytes = parse_input(input_string)
    start = (0, 0)
    end = (70, 70)
    x_range, y_range = 71, 71
    space = [['.' for _ in range(x_range)] for _ in range(y_range)]
    for x, y in corrupting_bytes[:1024]:
        space[y][x] = '#'
    routes = {start: 0}
    fronts = [(0, start)]
    while fronts:
        steps, pos = heapq.heappop(fronts)
        pos_y, pos_x = pos
        next_fronts = get_adjacent(pos_x, x_range, pos_y, y_range)

        for next_pos in next_fronts:
            next_pos_x, next_pos_y = next_pos
            if space[next_pos_y][next_pos_x] == '#':
                continue
            new_steps = steps + 1
            if (next_pos_y, next_pos_x) in routes:
                if new_steps < routes[(next_pos_y, next_pos_x)]:
                    heapq.heappush(fronts, (new_steps, (next_pos_y, next_pos_x)))
            else:
                routes.update({
                    (next_pos_y, next_pos_x): new_steps
                })
                heapq.heappush(fronts, (new_steps, (next_pos_y, next_pos_x)))
    print(routes[end])


def part_2(input_string):
    corrupting_bytes = parse_input(input_string)
    start = (0, 0)
    end = (70, 70)
    x_range, y_range = 71, 71
    space = [['.' for _ in range(x_range)] for _ in range(y_range)]
    for x, y in corrupting_bytes[:1024]:
        space[y][x] = '#'
    for x, y in corrupting_bytes[1024:]:
        space[y][x] = '#'
        routes = {start: 0}
        fronts = [(0, start)]
        while fronts:
            steps, pos = heapq.heappop(fronts)
            if pos == end:
                continue
            pos_y, pos_x = pos
            next_fronts = get_adjacent(pos_x, x_range, pos_y, y_range)

            for next_pos in next_fronts:
                next_pos_x, next_pos_y = next_pos
                if space[next_pos_y][next_pos_x] == '#':
                    continue
                new_steps = steps + 1
                if (next_pos_y, next_pos_x) in routes:
                    if new_steps < routes[(next_pos_y, next_pos_x)]:
                        heapq.heappush(fronts, (new_steps, (next_pos_y, next_pos_x)))
                else:
                    routes.update({
                        (next_pos_y, next_pos_x): new_steps
                    })
                    heapq.heappush(fronts, (new_steps, (next_pos_y, next_pos_x)))
        if end not in routes:
            print(','.join(map(str, [x,y])))
            break
        # else:
        #     print('\n'.join(list(map(lambda s: ''.join(s), space))))
        #     print(y,x,routes[end])
        #     import pdb; pdb.set_trace()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_18.txt', 'r')
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
