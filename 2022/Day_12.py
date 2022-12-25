import argparse
import heapq
import string


def get_steps_map(src, heightmap):
    steps_map = {src: 0}
    front_pos = [(0, src)]
    while front_pos:
        steps, pos = heapq.heappop(front_pos)
        pos_x, pos_y = pos
        possible_next_pos = []
        if 0 < pos_x:
            possible_next_pos.append((pos_x - 1, pos_y))
        if pos_x < len(heightmap) - 1:
            possible_next_pos.append((pos_x + 1, pos_y))
        if 0 < pos_y:
            possible_next_pos.append((pos_x, pos_y - 1))
        if pos_y < len(heightmap[pos_x]) - 1:
            possible_next_pos.append((pos_x, pos_y + 1))

        for next_pos in possible_next_pos:
            next_pos_x, next_pos_y = next_pos
            pos_height = string.ascii_lowercase.index(heightmap[pos_x][pos_y])
            next_pos_height = string.ascii_lowercase.index(heightmap[next_pos_x][next_pos_y])
            # Comparison for part 1
            if heightmap[src[0]][src[1]] == 'a' and next_pos_height - pos_height > 1:
                continue
            # Comparison for part 2
            if heightmap[src[0]][src[1]] == 'z' and next_pos_height - pos_height < -1:
                continue
            new_steps = steps + 1
            if next_pos in steps_map:
                old_steps = steps_map[next_pos]
                steps_map[next_pos] = min(steps + 1, old_steps)
                # Some tricks to speed up parsing, but removed so as to reuse this function
                # if des in steps_map:
                #     if steps_map[next_pos] >= steps_map[des] and next_pos != des:
                #         continue
                if steps_map[next_pos] != old_steps:
                    heapq.heappush(front_pos, (new_steps, next_pos))
            else:
                steps_map.update({
                    next_pos: new_steps
                })
                heapq.heappush(front_pos, (new_steps, next_pos))
    return steps_map


def part_1(input_string):
    heightmap = list(map(list, input_string.split('\n')))
    src = ()
    des = ()
    for x in range(len(heightmap)):
        for y in range(len(heightmap[x])):
            if heightmap[x][y] == 'S':
                src = (x, y)
                heightmap[x][y] = 'a'
                continue
            if heightmap[x][y] == 'E':
                des = (x, y)
                heightmap[x][y] = 'z'
                continue
            if len(src) * len(des) != 0:
                break
    steps_map = get_steps_map(src, heightmap)
    print(steps_map[des])


def part_2(input_string):
    heightmap = list(map(list, input_string.split('\n')))
    src = ()
    des = []
    for x in range(len(heightmap)):
        for y in range(len(heightmap[x])):
            if heightmap[x][y] == 'S':
                heightmap[x][y] = 'a'

            if heightmap[x][y] == 'a':
                des.append((x, y))
                continue
            
            if heightmap[x][y] == 'E':
                src = (x, y)
                heightmap[x][y] = 'z'
                continue

    steps_map = get_steps_map(src, heightmap)
    print(min(steps_map.get(d, max(steps_map.values()) + 1) for d in des))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_12.txt', 'r')
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
