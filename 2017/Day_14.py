import argparse

from Day_10 import knot_hash


def part_1(input_string):
    key_string = input_string + "-{}"
    used_count = 0
    for i in range(128):
        used_count += list(bin(int(knot_hash(key_string.format(i)), 16))[2:].zfill(128)).count('1')
    print(used_count)



def part_2(input_string):
    key_string = input_string + "-{}"
    grids = []
    for i in range(128):
        grids.extend(list(bin(int(knot_hash(key_string.format(i)), 16))[2:].zfill(128)))
    
    region = 0
    while '1' in grids:
        region += 1
        region_grids = [grids.index('1')]
        grids[region_grids[-1]] = region
        for i in region_grids:
            adj_grids = []
            if (i + 1) % 128 != 0 and i + 1 < len(grids):
                adj_grids.append(i + 1)
            if (i - 1) % 128 != 127:
                adj_grids.append(i - 1)
            if i >= 128:
                adj_grids.append(i - 128)
            if i + 128 < len(grids):
                adj_grids.append(i + 128)

            for grid in adj_grids:
                if grids[grid] == '1':
                    grids[grid] = region
                    region_grids.append(grid)
    print(region)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_14.txt', 'r')
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
