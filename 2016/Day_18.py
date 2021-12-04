import argparse


def get_tile_type(tile_0, tile_1, tile_2):
    return '^' if (tile_0+tile_1+tile_2) in ['^^.', '.^^', '^..', '..^'] else '.'


def get_safe_tiles_count(first_row_tiles, row_num):
    safe_tiles_count = 0
    row_tiles = first_row_tiles
    for i in range(row_num):
        if i == 0:
            safe_tiles_count += row_tiles.count('.')
            continue

        new_row_tiles = ''
        for j in range(len(row_tiles)):
            if j == 0:
                new_row_tiles += get_tile_type('.', row_tiles[j], row_tiles[j + 1])
                continue

            if j == len(row_tiles) - 1:
                new_row_tiles += get_tile_type(row_tiles[j - 1], row_tiles[j], '.')
                continue

            new_row_tiles += get_tile_type(row_tiles[j - 1], row_tiles[j], row_tiles[j + 1])

        row_tiles = new_row_tiles
        safe_tiles_count += row_tiles.count('.')

    return safe_tiles_count


def part_1(first_row_tiles):
    row_num = 40
    print(get_safe_tiles_count(first_row_tiles, row_num))


def part_2(first_row_tiles):
    row_num = 400000
    print(get_safe_tiles_count(first_row_tiles, row_num))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    first_row_tiles = '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^' \
                      '.^...^^^...^^^^..^...^...^^.^.^.....' \
                      '..^..^^...^.^.^^..^^^^^...^.'

    if args.part == '1':
        part_1(first_row_tiles)
    elif args.part == '2':
        part_2(first_row_tiles)
    else:
        part_1(first_row_tiles)
        part_2(first_row_tiles)


if __name__ == "__main__":
    main()
