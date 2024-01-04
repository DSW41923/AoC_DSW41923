import argparse
import heapq


def part_1(input_string):
    blocks = [list(map(int, list(r)))for r in input_string.split('\n')]
    block_x_range = len(blocks)
    block_y_range = len(blocks[0])
    dest = (block_x_range-1, block_y_range-1)
    heat_loss_map = {((0, 0), ('', 0)): 0}
    states = [(0, (0, 0), ('', 0))]
    while states:
        heat_loss, pos, consecutive_state = heapq.heappop(states)
        pos_x, pos_y = pos
        possible_next_pos = []
        if 0 < pos_x and consecutive_state[0] != 'D':
            if consecutive_state[0] == 'U':
                if consecutive_state[1] < 3:
                    possible_next_pos.append(((pos_x - 1, pos_y), ('U', consecutive_state[1]+1)))
            else:
                possible_next_pos.append(((pos_x - 1, pos_y), ('U', 1)))
        if pos_x < block_x_range - 1 and consecutive_state[0] != 'U':
            if consecutive_state[0] == 'D':
                if consecutive_state[1] < 3:
                    possible_next_pos.append(((pos_x + 1, pos_y), ('D', consecutive_state[1]+1)))
            else:
                possible_next_pos.append(((pos_x + 1, pos_y), ('D', 1)))
        if 0 < pos_y and consecutive_state[0] != 'R':
            if consecutive_state[0] == 'L':
                if consecutive_state[1] < 3:
                    possible_next_pos.append(((pos_x, pos_y - 1), ('L', consecutive_state[1]+1)))
            else:
                possible_next_pos.append(((pos_x, pos_y - 1), ('L', 1)))
        if pos_y < block_y_range - 1 and consecutive_state[0] != 'L':
            if consecutive_state[0] == 'R':
                if consecutive_state[1] < 3:
                    possible_next_pos.append(((pos_x, pos_y + 1), ('R', consecutive_state[1]+1)))
            else:
                possible_next_pos.append(((pos_x, pos_y + 1), ('R', 1)))

        for next_pos, next_consecutive_state in possible_next_pos:
            new_heat_loss = heat_loss + blocks[next_pos[0]][next_pos[1]]
            if (next_pos, next_consecutive_state) in heat_loss_map:
                old_heat_loss = heat_loss_map[(next_pos, next_consecutive_state)]
                if new_heat_loss < old_heat_loss:
                    heat_loss_map[(next_pos, next_consecutive_state)] = new_heat_loss
                    heapq.heappush(states, (new_heat_loss, next_pos, next_consecutive_state))
            else:
                heat_loss_map.update({
                    (next_pos, next_consecutive_state): new_heat_loss
                })
                heapq.heappush(states, (new_heat_loss, next_pos, next_consecutive_state))
    print(min([heat_loss for heat_loss_key, heat_loss in heat_loss_map.items() if heat_loss_key[0] == dest]))


def part_2(input_string):
    blocks = [list(map(int, list(r)))for r in input_string.split('\n')]
    block_x_range = len(blocks)
    block_y_range = len(blocks[0])
    dest = (block_x_range-1, block_y_range-1)
    heat_loss_map = {((0, 0), (None, 0)): 0}
    states = [(0, (0, 0), (None, 4))]
    dirs = {'R':(0,1), 'L':(0,-1), 'D':(1,0), 'U':(-1,0)}
    newdirs = {'R' : ('U','D'),  'L' : ('D','U'), 'U' : ('L','R'),  'D': ('R', 'L'), None : ('R','D') }
    while states:
        heat_loss, pos, consecutive_state = heapq.heappop(states)
        pos_x, pos_y = pos
        possible_next_pos = []
        if consecutive_state[0] != None:
            newpos = (pos_x+dirs[consecutive_state[0]][0], pos_y+dirs[consecutive_state[0]][1])
            if 0 <= newpos[0] < block_x_range and 0 <= newpos[1] < block_y_range and consecutive_state[1]+1 <= 10:
                possible_next_pos.append( (newpos, ( consecutive_state[0], consecutive_state[1]+1)))   # straight

        for newdir in newdirs[consecutive_state[0]]: # turns
            newpos = (pos_x+4*dirs[newdir][0], pos_y+4*dirs[newdir][1])
            if 0 <= newpos[0] < block_x_range and 0 <= newpos[1] < block_y_range:
                i, j = newpos
                possible_next_pos.append( (newpos, ( newdir, 4)) )

        for next_pos, next_consecutive_state in possible_next_pos:
            incurred_heat_losses = 0
            if next_consecutive_state[1] == 4:
                match next_consecutive_state[0]:
                    case 'R': incurred_heat_losses = blocks[pos_x][pos_y+1] + blocks[pos_x][pos_y+2] + blocks[pos_x][pos_y+3] + blocks[pos_x][pos_y+4]
                    case 'L': incurred_heat_losses = blocks[pos_x][pos_y-1] + blocks[pos_x][pos_y-2] + blocks[pos_x][pos_y-3] + blocks[pos_x][pos_y-4]
                    case 'U': incurred_heat_losses = blocks[pos_x-1][pos_y] + blocks[pos_x-2][pos_y] + blocks[pos_x-3][pos_y] + blocks[pos_x-4][pos_y]
                    case 'D': incurred_heat_losses = blocks[pos_x+1][pos_y] + blocks[pos_x+2][pos_y] + blocks[pos_x+3][pos_y] + blocks[pos_x+4][pos_y]
            else:
                incurred_heat_losses = blocks[next_pos[0]][next_pos[1]]
            new_heat_loss = heat_loss + incurred_heat_losses
            if (next_pos, next_consecutive_state) in heat_loss_map:
                old_heat_loss = heat_loss_map[(next_pos, next_consecutive_state)]
                if new_heat_loss < old_heat_loss:
                    heat_loss_map[(next_pos, next_consecutive_state)] = new_heat_loss
                    heapq.heappush(states, (new_heat_loss, next_pos, next_consecutive_state))
            else:
                heat_loss_map.update({
                    (next_pos, next_consecutive_state): new_heat_loss
                })
                heapq.heappush(states, (new_heat_loss, next_pos, next_consecutive_state))
    print(min([heat_loss for heat_loss_key, heat_loss in heat_loss_map.items() if heat_loss_key[0] == dest]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_17.txt', 'r')
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
