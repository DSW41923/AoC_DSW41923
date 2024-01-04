#! python3
import sys
import getopt
import re
import itertools

class Tile(object):
    def __init__(self, index, data):
        super(Tile, self).__init__()
        self.index = index
        self.data = data
        self.unarranged_adjacent_tiles = []
        self.adjacent_tiles = {
            'down': None,
            'right': None
        }

    def get_sides(self):
        return [self.data[0], ''.join([d[-1] for d in self.data]), self.data[-1], ''.join([d[0] for d in self.data])]

    def flip(self):
        self.data.reverse()

    def rotate(self):
        self.data = [''.join([d[-i] for d in self.data]) for i in range(1, len(self.data[0]) + 1)]

def is_adjacent(tile1, tile2):
    tile1_sides = tile1.get_sides() + list(map(lambda s: ''.join(list(reversed(s))), tile1.get_sides()))
    tile2_sides = tile2.get_sides() + list(map(lambda s: ''.join(list(reversed(s))), tile2.get_sides()))
    for side1 in tile1_sides:
        for side2 in tile2_sides:
            if side1 in [side2, ''.join(list(reversed(side2)))]:
                return True

def arranging_tiles(tile, visited_tiles):
    id_direction = ['right', 'down']
    visited_tiles.append(tile.index)
    for side_id, side in enumerate(tile.get_sides()[1:3]):
        for adj_tile in tile.unarranged_adjacent_tiles:
            if adj_tile.index not in visited_tiles:
                for r in range(8):
                    if adj_tile.get_sides()[side_id - 1] == side:
                        tile.adjacent_tiles[id_direction[side_id]] = adj_tile
                        break
                    else:
                        adj_tile.rotate()
                        if r in [3, 7]:
                            adj_tile.flip()
    for adj_tile in tile.adjacent_tiles.values():
        if adj_tile:
            if adj_tile.index not in visited_tiles:
                arranging_tiles(adj_tile, visited_tiles)


# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_20.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_20.py [-h | --help]')
            print('Advent of Code 2020 Day 20')
            sys.exit()

    file_input = open('inputs/2020/Input_20.txt', 'r')
    input_strings = file_input.read()
    file_input.close()
    tiles = []
    for tile_id, tile_data in re.findall(r'Tile (\d+):\n([.#\n]+)', input_strings):
        tile_data = [t for t in tile_data.split('\n') if t]
        tiles.append(Tile(tile_id, tile_data))

    for tile1, tile2 in itertools.combinations(tiles, 2):
        if is_adjacent(tile1, tile2):
            tile1.unarranged_adjacent_tiles.append(tile2)
            tile2.unarranged_adjacent_tiles.append(tile1)

    corner_tile_id_multiplication = 1
    corner_tile = None
    for tile in tiles:
        if len(tile.unarranged_adjacent_tiles) == 2:
            corner_tile_id_multiplication *= int(tile.index)
            corner_tile = tile
    print(corner_tile_id_multiplication)

    direction_check = 0
    while direction_check != 2:
        for side_id, side in enumerate(corner_tile.get_sides()[1:3]):
            for adj_tile in corner_tile.unarranged_adjacent_tiles:
                for r in range(8):
                    if adj_tile.get_sides()[side_id - 1] == side:
                        direction_check += 1
                        break
                    else:
                        adj_tile.rotate()
                        if r in [3, 7]:
                            adj_tile.flip()
        if direction_check != 2:
            corner_tile.rotate()
            direction_check = 0

    visited_tiles_id = []
    arranging_tiles(corner_tile, visited_tiles_id)

    full_image_tiles = [[] for _ in range(12)]
    row_starting_tile = corner_tile
    for row in range(12):
        current_tile = row_starting_tile
        for column in range(12):
            full_image_tiles[row].append(current_tile)
            current_tile = current_tile.adjacent_tiles['right']
        row_starting_tile = row_starting_tile.adjacent_tiles['down']

    full_image_data = []
    tile_length = len(tiles[0].data[0])
    for row_tiles in full_image_tiles:
        for i in range(1, tile_length - 1):
            full_image_data.append(''.join([tile.data[i][1:-1] for tile in row_tiles]))

    sea_monster_pattern = ['                  # ',
                           '#    ##    ##    ###',
                           ' #  #  #  #  #  #   ']
    full_image_tile = Tile('9999', full_image_data)
    sea_monster_count = 0
    for p in range(8):
        for row in range(len(full_image_data) - 2):
            for column in range(len(full_image_data[0]) - 19):
                if full_image_tile.data[row][column + 18] == '#':
                    further_checkingn_location = [
                        full_image_tile.data[row + 1][column],
                        full_image_tile.data[row + 1][column + 5],
                        full_image_tile.data[row + 1][column + 6],
                        full_image_tile.data[row + 1][column + 11],
                        full_image_tile.data[row + 1][column + 12],
                        full_image_tile.data[row + 1][column + 17],
                        full_image_tile.data[row + 1][column + 18],
                        full_image_tile.data[row + 1][column + 19]]
                    if all(c == '#' for c in further_checkingn_location):
                        last_checkingn_location = [
                            full_image_tile.data[row + 2][column + 1],
                            full_image_tile.data[row + 2][column + 4],
                            full_image_tile.data[row + 2][column + 7],
                            full_image_tile.data[row + 2][column + 10],
                            full_image_tile.data[row + 2][column + 13],
                            full_image_tile.data[row + 2][column + 16]]
                        if all(c == '#' for c in last_checkingn_location):
                            sea_monster_count += 1
        if sea_monster_count > 0:
            total_sharp_count = sum(r.count('#') for r in full_image_tile.data)
            sea_monster_sharp_count = sum(r.count('#') for r in sea_monster_pattern) * sea_monster_count
            print(total_sharp_count - sea_monster_sharp_count)
            break
        else:
            full_image_tile.rotate()
            if p in [3, 7]:
                full_image_tile.flip()


if __name__ == "__main__":
    main(sys.argv[1:])