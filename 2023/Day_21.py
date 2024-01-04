import argparse
import heapq


def part_1(input_string):
    garden = [list(line) for line in input_string.split('\n')]
    start = None
    for x, row in enumerate(garden):
        for y, obj in enumerate(row):
            if obj == 'S':
                start = (x, y)
                break
        if start:
            break
    garden_x_range = len(garden)
    garden_y_range = len(garden[0])
    total_steps = 64
    factor = 2
    steps_map = {start: 0}
    front = [(0, start)]
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    while all([steps <= total_steps for steps, _ in front]):
        steps, pos = heapq.heappop(front)
        pos_x, pos_y = pos
        possible_next_pos = []
        for dir in dirs:
            new_pos_x, new_pos_y = pos_x+dir[0], pos_y+dir[1]
            if 0 <= pos_x < garden_x_range and 0 <= y < garden_y_range and garden[new_pos_x][new_pos_y] != '#':
                possible_next_pos.append((new_pos_x, new_pos_y))

        for next_pos in possible_next_pos:
            new_steps = steps + 1
            if next_pos in steps_map:
                old_steps = steps_map[next_pos]
                steps_map[next_pos] = min(new_steps, old_steps)
                if steps_map[next_pos] != old_steps:
                    heapq.heappush(front, (new_steps, next_pos))
            else:
                steps_map.update({
                    next_pos: new_steps
                })
                heapq.heappush(front, (new_steps, next_pos))
    print(len([s for s in steps_map.values() if s % factor == 0]))


def part_2(input_string):
    garden = [list(line) for line in input_string.split('\n')]
    start = None
    for x, row in enumerate(garden):
        for y, obj in enumerate(row):
            if obj == 'S':
                start = (x, y)
                break
        if start:
            break

    garden_x_range = len(garden)
    garden_y_range = len(garden[0])
    total_steps = 26501365
    steps = 0
    visited = [[[start]], []]
    fronts = [start]
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    counts = []
    while steps < total_steps:
        next_fronts = []
        steps += 1
        visited[steps % 2].append([])
        for pos_x, pos_y in fronts:
            for dir in dirs:
                new_pos_x, new_pos_y = pos_x+dir[0], pos_y+dir[1]
                if garden[new_pos_x%garden_x_range][new_pos_y%garden_y_range] != '#':
                    if ((new_pos_x, new_pos_y) not in visited[steps % 2][steps//2-1] + visited[steps % 2][steps//2]):
                        visited[steps % 2][steps//2].append((new_pos_x, new_pos_y))
                        next_fronts.append((new_pos_x, new_pos_y))
        fronts = list(set(next_fronts))
        if steps % 131 == 65:
            counts.append(sum(list(map(len, visited[steps % 2]))))

        if len(counts) == 6:
            break
    lagrange = [None for _ in range(3)]
    xs = list(map(lambda x: garden_x_range*x+65, range(len(counts))))
    lagrange[0] = lambda k: (counts[0]*(k-xs[1])*(k-xs[2]))/((xs[0]-xs[1])*(xs[0]-xs[2]))
    lagrange[1] = lambda k: (counts[1]*(k-xs[2])*(k-xs[0]))/((xs[1]-xs[2])*(xs[1]-xs[0]))
    lagrange[2] = lambda k: (counts[2]*(k-xs[0])*(k-xs[1]))/((xs[2]-xs[0])*(xs[2]-xs[1]))
    for x, y in zip(xs, counts):
        assert((lagrange[0](x)+lagrange[1](x)+lagrange[2](x)) == y)
    print(int(lagrange[0](total_steps)+lagrange[1](total_steps)+lagrange[2](total_steps)))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2023/Input_21.txt', 'r')
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
