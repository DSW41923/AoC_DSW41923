import sys
import getopt
import copy


def get_adjacent_tiles(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y - 1), (x - 1, y + 1)]


# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_24.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_24.py [-h | --help]')
            print('Advent of Code 2020 Day 24')
            sys.exit()

    file_input = open('Input_24.txt', 'r')
    input_strings = file_input.readlines()
    file_input.close()
    black_tiles = []
    reference_tile = (0, 0)
    for steps in input_strings:
        step_list = list(steps)
        flipping_tile_x, flipping_tile_y = reference_tile[0], reference_tile[1]
        previous_north, previous_south = False, False
        for step in step_list:
            if step == 'e':
                if previous_north:
                    previous_north = False
                else:
                    flipping_tile_x += 1
                    previous_south = False
            if step == 'w':
                if previous_south:
                    previous_south = False
                else:
                    flipping_tile_x -= 1
                    previous_north = False
            if step == 'n':
                flipping_tile_y += 1
                previous_north = True
            if step == 's':
                flipping_tile_y -= 1
                previous_south = True
        if (flipping_tile_x, flipping_tile_y) not in black_tiles:
            black_tiles.append((flipping_tile_x, flipping_tile_y))
        else:
            black_tiles.remove((flipping_tile_x, flipping_tile_y))
    print(len(black_tiles))

    black_tiles_dict = {}
    for x, y in black_tiles:
        if black_tiles_dict.get(x, []):
            black_tiles_dict[x].append(y)
        else:
            black_tiles_dict.update({x: [y]})

    for _ in range(100):
        new_black_tiles_dict = copy.deepcopy(black_tiles_dict)
        xborder = (min(black_tiles_dict.keys()) - 1, max(black_tiles_dict.keys()) + 1)
        yborder = (min([min(t) for t in black_tiles_dict.values() if t]) - 1,
                   max([max(t) for t in black_tiles_dict.values() if t]) + 1)
        for tile_x in range(xborder[0], xborder[1] + 1):
            for tile_y in range(yborder[0], yborder[1] + 1):
                adjacent_tiles = get_adjacent_tiles(tile_x, tile_y)
                adjacent_black_tiles_count = len([t for t in adjacent_tiles if t[1] in black_tiles_dict.get(t[0], [])])
                if tile_y in black_tiles_dict.get(tile_x, []):
                    if adjacent_black_tiles_count not in [1, 2]:
                        new_black_tiles_dict[tile_x].remove(tile_y)
                else:
                    if adjacent_black_tiles_count == 2:
                        if new_black_tiles_dict.get(tile_x, []):
                            new_black_tiles_dict[tile_x].append(tile_y)
                        else:
                            new_black_tiles_dict.update({tile_x: [tile_y]})
        black_tiles_dict = new_black_tiles_dict
    print(sum(list(map(len, black_tiles_dict.values()))))

if __name__ == "__main__":
    main(sys.argv[1:])