import argparse


def get_map_data(input_string):
    height_map = list(map(list, input_string.split('\n')))
    max_x = len(height_map)
    max_y = len(height_map[0])
    trailheads = []
    for x in range(max_x):
        for y in range(max_y):
            if height_map[x][y] == '0':
                trailheads += [(x,y)]
    return height_map, max_x, max_y, trailheads


def part_1(input_string):
    height_map, max_x, max_y, trailheads = get_map_data(input_string)
    result = 0
    for trailhead in trailheads:
        trail_fronts = [trailhead]
        for i in range(1,10):
            next_fronts = []
            for trailhead_x, trailhead_y in trail_fronts:
                if trailhead_x > 0 and int(height_map[trailhead_x-1][trailhead_y]) == i:
                    next_fronts.append((trailhead_x-1, trailhead_y))
                if trailhead_x < max_x-1 and int(height_map[trailhead_x+1][trailhead_y]) == i:
                    next_fronts.append((trailhead_x+1, trailhead_y))
                if trailhead_y > 0 and int(height_map[trailhead_x][trailhead_y-1]) == i:
                    next_fronts.append((trailhead_x, trailhead_y-1))
                if trailhead_y < max_y-1 and int(height_map[trailhead_x][trailhead_y+1]) == i:
                    next_fronts.append((trailhead_x, trailhead_y+1))
            trail_fronts = list(set(next_fronts))
        result += len(set(trail_fronts))
    print(result)


def part_2(input_string):
    height_map, max_x, max_y, trailheads = get_map_data(input_string)
    result = 0
    for trailhead in trailheads:
        trail_fronts = [trailhead]
        for i in range(1,10):
            next_fronts = []
            for trailhead_x, trailhead_y in trail_fronts:
                if trailhead_x > 0 and int(height_map[trailhead_x-1][trailhead_y]) == i:
                    next_fronts.append((trailhead_x-1, trailhead_y))
                if trailhead_x < max_x-1 and int(height_map[trailhead_x+1][trailhead_y]) == i:
                    next_fronts.append((trailhead_x+1, trailhead_y))
                if trailhead_y > 0 and int(height_map[trailhead_x][trailhead_y-1]) == i:
                    next_fronts.append((trailhead_x, trailhead_y-1))
                if trailhead_y < max_y-1 and int(height_map[trailhead_x][trailhead_y+1]) == i:
                    next_fronts.append((trailhead_x, trailhead_y+1))
            trail_fronts = next_fronts
        result += len(trail_fronts)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_10.txt', 'r')
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
