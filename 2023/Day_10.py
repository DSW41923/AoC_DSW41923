import argparse


def part_1(input_string):
    maps = [list(line) for line in input_string.split('\n')]
    s_location = (0, 0)
    x_bound = len(maps) - 1
    y_bound = len(maps[0]) - 1
    for x in range(x_bound + 1):
        for y in range(y_bound + 1):
            if maps[x][y] == 'S':
                s_location = (x, y)
                s_north = None
                if 0 < x:
                    s_north = maps[x-1][y]
                s_east = None
                if y < y_bound:
                    s_east = maps[x][y+1]
                s_south = None
                if x < x_bound:
                    s_south = maps[x+1][y]
                s_west = None
                if 0 < y:
                    s_west = maps[x][y-1]
                if s_north in ['|', '7', 'F'] and s_south in ['|', 'L', 'J']:
                    maps[x][y] = '|'
                elif s_east in ['-', '7', 'J'] and s_west in ['-', 'F', 'L']:
                    maps[x][y] = '-'
                elif s_north in ['|', '7', 'F'] and s_east in ['-', '7', 'J']:
                    maps[x][y] = 'L'
                elif s_north in ['|', '7', 'F'] and s_west in ['-', 'F', 'L']:
                    maps[x][y] = 'J'
                elif s_west in ['-', 'F', 'L'] and s_south in ['|', 'L', 'J']:
                    maps[x][y] = '7'
                elif s_east in ['-', '7', 'J'] and s_south in ['|', 'L', 'J']:
                    maps[x][y] = 'F'
    visited = []
    fronts = [s_location, s_location]
    steps = 0
    while len(fronts) > 1:
        new_front_candidates = []
        for front_x, front_y in fronts:
            visited.append((front_x, front_y))
            if maps[front_x][front_y] == '|': # | is a vertical pipe connecting north and south.
                if 0 < front_x:
                    new_front_candidates.append((front_x-1, front_y))
                if front_x < x_bound:
                    new_front_candidates.append((front_x+1, front_y))
            elif maps[front_x][front_y] == '-': # - is a horizontal pipe connecting east and west.
                if 0 < front_y:
                    new_front_candidates.append((front_x, front_y-1))
                if front_y < y_bound:
                    new_front_candidates.append((front_x, front_y+1))
            elif maps[front_x][front_y] == 'L': # L is a 90-degree bend connecting north and east.
                if 0 < front_x:
                    new_front_candidates.append((front_x-1, front_y))
                if front_y < y_bound:
                    new_front_candidates.append((front_x, front_y+1))
            elif maps[front_x][front_y] == 'J': # J is a 90-degree bend connecting north and west.
                if 0 < front_x:
                    new_front_candidates.append((front_x-1, front_y))
                if 0 < front_y:
                    new_front_candidates.append((front_x, front_y-1))
            elif maps[front_x][front_y] == '7': # 7 is a 90-degree bend connecting south and west.
                if front_x < x_bound:
                    new_front_candidates.append((front_x+1, front_y))
                if 0 < front_y:
                    new_front_candidates.append((front_x, front_y-1))
            elif maps[front_x][front_y] == 'F': # F is a 90-degree bend connecting south and east.
                if front_x < x_bound:
                    new_front_candidates.append((front_x+1, front_y))
                if front_y < y_bound:
                    new_front_candidates.append((front_x, front_y+1))
        new_front_candidates = list(set(new_front_candidates))
        fronts = [f for f in new_front_candidates if f not in visited]
        steps += 1
    print(steps)


def part_2(input_string):
    maps = [list(line) for line in input_string.split('\n')]
    s_location = (0, 0)
    x_bound = len(maps) - 1
    y_bound = len(maps[0]) - 1
    for x in range(x_bound + 1):
        for y in range(y_bound + 1):
            if maps[x][y] == 'S':
                s_location = (x, y)
                s_north = None
                if 0 < x:
                    s_north = maps[x-1][y]
                s_east = None
                if y < y_bound:
                    s_east = maps[x][y+1]
                s_south = None
                if x < x_bound:
                    s_south = maps[x+1][y]
                s_west = None
                if 0 < y:
                    s_west = maps[x][y-1]
                if s_north in ['|', '7', 'F'] and s_south in ['|', 'L', 'J']:
                    maps[x][y] = '|'
                elif s_east in ['-', '7', 'J'] and s_west in ['-', 'F', 'L']:
                    maps[x][y] = '-'
                elif s_north in ['|', '7', 'F'] and s_east in ['-', '7', 'J']:
                    maps[x][y] = 'L'
                elif s_north in ['|', '7', 'F'] and s_west in ['-', 'F', 'L']:
                    maps[x][y] = 'J'
                elif s_west in ['-', 'F', 'L'] and s_south in ['|', 'L', 'J']:
                    maps[x][y] = '7'
                elif s_east in ['-', '7', 'J'] and s_south in ['|', 'L', 'J']:
                    maps[x][y] = 'F'
    loop_tiles = []
    fronts = [s_location, s_location]
    while fronts:
        new_front_candidates = []
        for front in fronts:
            if front not in loop_tiles:
                loop_tiles.append(front)
            front_x, front_y = front

            if maps[front_x][front_y] == '|': # | is a vertical pipe connecting north and south.
                if 0 < front_x:
                    new_front_candidates.append((front_x-1, front_y))
                if front_x < x_bound:
                    new_front_candidates.append((front_x+1, front_y))
            elif maps[front_x][front_y] == '-': # - is a horizontal pipe connecting east and west.
                if 0 < front_y:
                    new_front_candidates.append((front_x, front_y-1))
                if front_y < y_bound:
                    new_front_candidates.append((front_x, front_y+1))
            elif maps[front_x][front_y] == 'L': # L is a 90-degree bend connecting north and east.
                if 0 < front_x:
                    new_front_candidates.append((front_x-1, front_y))
                if front_y < y_bound:
                    new_front_candidates.append((front_x, front_y+1))
            elif maps[front_x][front_y] == 'J': # J is a 90-degree bend connecting north and west.
                if 0 < front_x:
                    new_front_candidates.append((front_x-1, front_y))
                if 0 < front_y:
                    new_front_candidates.append((front_x, front_y-1))
            elif maps[front_x][front_y] == '7': # 7 is a 90-degree bend connecting south and west.
                if front_x < x_bound:
                    new_front_candidates.append((front_x+1, front_y))
                if 0 < front_y:
                    new_front_candidates.append((front_x, front_y-1))
            elif maps[front_x][front_y] == 'F': # F is a 90-degree bend connecting south and east.
                if front_x < x_bound:
                    new_front_candidates.append((front_x+1, front_y))
                if front_y < y_bound:
                    new_front_candidates.append((front_x, front_y+1))
        new_front_candidates = list(set(new_front_candidates))
        fronts = [f for f in new_front_candidates if f not in loop_tiles]

    inner_counts = 0
    for x in range(x_bound + 1):
        for y in range(y_bound + 1):
            if (x, y) not in loop_tiles:
                intersect_count = 0
                cur_x, cur_y = x, y
                while 0 <= cur_x and 0 <= cur_y:
                    if (cur_x, cur_y) in loop_tiles:
                        if maps[cur_x][cur_y] in ['L', '7']:
                            # Hitting corners, set intersect_count increment by 2
                            intersect_count += 2
                        else:
                            intersect_count += 1
                    cur_x -= 1
                    cur_y -= 1

                if intersect_count % 2:
                    # If you shoot a ray in any direction from the pixel 
                    # and it crosses the boundary an odd number of times, it's inside the shape. 
                    # otherwise, it's outside. 
                    # Works for all enclosed shapes, even self-intersecting and non-convex ones.
                    inner_counts += 1
    print(inner_counts)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_10.txt', 'r')
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
