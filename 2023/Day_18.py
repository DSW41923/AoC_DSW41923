import argparse
import math
import re


def part_1(input_string):
    # Commented method 1: actually record status of ground blocks, sum the blocks on edge and inside
    # ground = [['.' for _ in range(1000)] for _ in range(1000)]
    # cur = (0, 0)
    curs = [(0, 0)]
    # x_range, y_range = 500, 500
    dirs = {'R':(0,1), 'L':(0,-1), 'D':(1,0), 'U':(-1,0)}
    volume = 0
    for direction, length, color in re.findall(r"([RULD]) (\d+) \(([\#0-9a-f]+)\)", input_string):
        length = int(length)
        new_cur = (curs[-1][0]+length*dirs[direction][0], curs[-1][1]+length*dirs[direction][1])
        # match direction:
        #     case 'R': 
        #         for y in range(cur[1]+1, new_cur[1]+1): ground[cur[0]][y] = color
        #     case 'L':
        #         for y in range(cur[1]-1, new_cur[1]-1, -1): ground[cur[0]][y] = color
        #     case 'U':
        #         for x in range(cur[0]-1, new_cur[0]-1, -1): ground[x][cur[1]] = color
        #     case 'D':
        #         for x in range(cur[0]+1, new_cur[0]+1): ground[x][cur[1]] = color
        volume += length
        # cur = new_cur
        curs.append(new_cur)
    volume_inner = 0
    for x in range(1, len(curs)-1):
        volume_inner += curs[x][0] * curs[x+1][1]
        volume_inner -= curs[x][1] * curs[x+1][0]
    print(abs(volume_inner)//2+1+volume//2)

    # Slow method: Adopt inner node check from Day 10
    # for x in range(-x_range, x_range):
    #     for y in range(-y_range, y_range):
    #         if not ground[x][y].startswith('#'):
    #             intersect_count = 0
    #             cur_x, cur_y = x, y
    #             while -x_range <= cur_x and -y_range <= cur_y:
    #                 if ground[cur_x][cur_y].startswith('#'):
    #                     if ('#', '#') in [(ground[cur_x-1][cur_y][0],ground[cur_x][cur_y+1][0]), 
    #                                       (ground[cur_x][cur_y-1][0],ground[cur_x+1][cur_y][0])]:
    #                         # Hitting corners, set intersect_count increment by 2
    #                         intersect_count += 2
    #                     else:
    #                         intersect_count += 1
    #                 cur_x -= 1
    #                 cur_y -= 1

    #             if intersect_count % 2:
    #                 # If you shoot a ray in any direction from the pixel 
    #                 # and it crosses the boundary an odd number of times, it's inside the shape. 
    #                 # otherwise, it's outside. 
    #                 # Works for all enclosed shapes, even self-intersecting and non-convex ones.
    #                 volume += 1
    # print(volume)


def part_2(input_string):
    # Fast method 2: Combine the shoelace formula (the surveyor's formula) and Pick's theorem
    # Area = inner_points_count + edge_points_count / 2 - 1
    # inner_points_count = Area - edge_points_count / 2 + 1
    # What we want is actually inner_points_count + edge_points_count = Area + edge_points_count / 2 + 1
    # Area can be computed by the shoelace formula
    curs = [(0, 0)]
    int_to_dir =['R', 'D', 'L', 'U']
    dirs = {'R':(0,1), 'L':(0,-1), 'D':(1,0), 'U':(-1,0)}
    edge_points = 0
    for instruction in re.findall(r"\(\#([0-9a-f]+)\)", input_string):
        length = int(instruction[:5], 16)
        direction = int_to_dir[int(instruction[5])]
        new_cur = (curs[-1][0]+length*dirs[direction][0], curs[-1][1]+length*dirs[direction][1])
        edge_points += length
        curs.append(new_cur)
    volume = 0
    for x in range(1, len(curs)-1):
        volume += curs[x][0] * curs[x+1][1]
        volume -= curs[x][1] * curs[x+1][0]
    print(abs(volume)//2+edge_points//2+1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_18.txt', 'r')
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
