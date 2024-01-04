import argparse


def count_energized_tiles(tiles, start):
    tile_x_range = len(tiles)
    tile_y_range = len(tiles[0])
    beam_fronts = [start]
    visited = []
    energized_tiles = []
    while beam_fronts:
        beam_front, direction = beam_fronts.pop(0)
        visited.append((beam_front, direction))

        beam_front_x, beam_front_y = beam_front
        next_front = None
        if direction == 'R' and beam_front_y < tile_y_range - 1:
            next_front = (beam_front_x, beam_front_y+1)
        elif direction == 'D' and beam_front_x < tile_x_range - 1:
            next_front = (beam_front_x+1, beam_front_y)
        elif direction == 'L' and 0 < beam_front_y:
            next_front = (beam_front_x, beam_front_y-1)
        elif direction == 'U' and 0 < beam_front_x:
            next_front = (beam_front_x-1, beam_front_y)

        if not next_front:
            continue

        if tiles[next_front[0]][next_front[1]] == '/':
            if direction == 'R':
                beam_fronts.append((next_front, 'U'))
            elif direction == 'D':
                beam_fronts.append((next_front, 'L'))
            elif direction == 'L':
                beam_fronts.append((next_front, 'D'))
            elif direction == 'U':
                beam_fronts.append((next_front, 'R'))
        elif tiles[next_front[0]][next_front[1]] == '\\':
            if direction == 'R':
                beam_fronts.append((next_front, 'D'))
            elif direction == 'D':
                beam_fronts.append((next_front, 'R'))
            elif direction == 'L':
                beam_fronts.append((next_front, 'U'))
            elif direction == 'U':
                beam_fronts.append((next_front, 'L'))
        elif tiles[next_front[0]][next_front[1]] == '|':
            if direction in ['L', 'R']:
                beam_fronts.append((next_front, 'U'))
                beam_fronts.append((next_front, 'D'))
            elif direction in ['U', 'D']:
                beam_fronts.append((next_front, direction))
        elif tiles[next_front[0]][next_front[1]] == '-':
            if direction in ['L', 'R']:
                beam_fronts.append((next_front, direction))
            elif direction in ['U', 'D']:
                beam_fronts.append((next_front, 'L'))
                beam_fronts.append((next_front, 'R'))
        else:
            beam_fronts.append((next_front, direction))
        
        beam_fronts = list(set(beam_fronts) - set(visited))
        for front in beam_fronts:
            energized_tiles.append(front[0])

    return len(set(energized_tiles))


def part_1(input_string):
    tiles = [list(row) for row in input_string.split('\n')]
    print(count_energized_tiles(tiles, ((0, -1), 'R')))
    


def part_2(input_string):
    tiles = [list(row) for row in input_string.split('\n')]
    tile_x_range = len(tiles)
    tile_y_range = len(tiles[0])
    starts = [((x, -1), 'R') for x in range(tile_x_range)] + [((-1, y), 'D') for y in range(tile_y_range)] + \
             [((x, tile_y_range), 'L') for x in range(tile_x_range)] + [((tile_x_range, y), 'U') for y in range(tile_y_range)]
    energized_tiles_counts = []
    for start in starts:
        energized_tiles_counts.append(count_energized_tiles(tiles, start))
    print(max(energized_tiles_counts))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_16.txt', 'r')
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
