import argparse


def get_next_pos(pos, facing):
    if facing == 0:
        return (pos[0]-1, pos[1])
    elif facing == 1:
        return (pos[0], pos[1]+1)
    elif facing == 2:
        return (pos[0]+1, pos[1])
    elif facing == 3:
        return (pos[0], pos[1]-1)


def get_tracks_data(input_string):
    tracks_map = list(map(list, input_string.split('\n')))
    x_range = len(tracks_map)
    y_range = len(tracks_map[0])
    carts = []
    for x in range(x_range):
        for y in range(y_range):
            if tracks_map[x][y] == '^':
                carts.append((0, x, y, 0))
                tracks_map[x][y] = '|'
            if tracks_map[x][y] == '>':
                carts.append((1, x, y, 0))
                tracks_map[x][y] = '-'
            if tracks_map[x][y] == 'v':
                carts.append((2, x, y, 0))
                tracks_map[x][y] = '|'
            if tracks_map[x][y] == '<':
                carts.append((3, x, y, 0))
                tracks_map[x][y] = '-'
    return tracks_map, carts


def part_1(input_string):
    tracks_map, carts = get_tracks_data(input_string)

    while True:
        new_carts = []
        for facing, pos_x, pos_y, turn_count in carts:
            pos = (pos_x, pos_y)
            next_pos_x, next_pos_y = get_next_pos(pos, facing)

            if (next_pos_x, next_pos_y) in [(c[1], c[2]) for c in new_carts]:
                print('{},{}'.format(next_pos_y, next_pos_x))
                return

            if tracks_map[next_pos_x][next_pos_y] == '/':
                new_carts.append((facing^1, next_pos_x, next_pos_y, turn_count))
            elif tracks_map[next_pos_x][next_pos_y] == '\\':
                new_carts.append((3-facing, next_pos_x, next_pos_y, turn_count))
            elif tracks_map[next_pos_x][next_pos_y] == '+':
                if turn_count == 0:
                    new_carts.append(((facing-1)%4, next_pos_x, next_pos_y, turn_count+1))
                elif turn_count == 1:
                    new_carts.append((facing, next_pos_x, next_pos_y, turn_count+1))
                elif turn_count == 2:
                    new_carts.append(((facing+1)%4, next_pos_x, next_pos_y, 0))
            else:
                new_carts.append((facing, next_pos_x, next_pos_y, turn_count))
                
        new_carts.sort(key=lambda c: c[1]*1000+c[2])
        carts = new_carts


def part_2(input_string):
    tracks_map, carts = get_tracks_data(input_string)

    while len(carts) > 1:
        new_carts = []
        crashed_carts = []
        for id, cart in enumerate(carts):
            if cart in crashed_carts:
                continue
            facing, pos_x, pos_y, turn_count = cart
            pos = (pos_x, pos_y)
            next_pos_x, next_pos_y = get_next_pos(pos, facing)

            crashed = False
            for i, c in enumerate(new_carts):
                if (next_pos_x, next_pos_y) == (c[1], c[2]):
                    new_carts.pop(i)
                    crashed = True
                    break
            for i, c in enumerate(carts[id+1:]):
                if (next_pos_x, next_pos_y) == (c[1], c[2]):
                    crashed_carts.append(c)
                    crashed = True
                    break
            if crashed:
                continue

            if tracks_map[next_pos_x][next_pos_y] == '/':
                new_carts.append((facing^1, next_pos_x, next_pos_y, turn_count))
            elif tracks_map[next_pos_x][next_pos_y] == '\\':
                new_carts.append((3-facing, next_pos_x, next_pos_y, turn_count))
            elif tracks_map[next_pos_x][next_pos_y] == '+':
                if turn_count == 0:
                    new_carts.append(((facing-1)%4, next_pos_x, next_pos_y, turn_count+1))
                elif turn_count == 1:
                    new_carts.append((facing, next_pos_x, next_pos_y, turn_count+1))
                elif turn_count == 2:
                    new_carts.append(((facing+1)%4, next_pos_x, next_pos_y, 0))
            else:
                new_carts.append((facing, next_pos_x, next_pos_y, turn_count))
                
        new_carts.sort(key=lambda c: c[1]*1000+c[2])
        carts = new_carts

    print('{},{}'.format(carts[0][2], carts[0][1]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_13.txt', 'r')
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
