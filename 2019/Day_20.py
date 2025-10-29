import argparse

from string import ascii_uppercase


def part_1(input_string):
    maze_map = list(map(list, input_string.split('\n')))
    x_range = len(maze_map[0])
    y_range = len(maze_map)
    portals_data = {}
    for x in range(x_range):
        for y in range(y_range):
            if maze_map[y][x] in ascii_uppercase:
                if 0 < x < x_range-1 and 0 < y < y_range-1:
                    if maze_map[y][x-1] == '.':
                        portal_name = ''.join(maze_map[y][x:x+2])
                        portal_pos = (x-1)+y*1j
                    elif maze_map[y][x+1] == '.':
                        portal_name = ''.join(maze_map[y][x-1:x+1])
                        portal_pos = (x+1)+y*1j
                    elif maze_map[y-1][x] == '.':
                        portal_name = ''.join([maze_map[y][x], maze_map[y+1][x]])
                        portal_pos = x+(y-1)*1j
                    elif maze_map[y+1][x] == '.':
                        portal_name = ''.join([maze_map[y-1][x], maze_map[y][x]])
                        portal_pos = x+(y+1)*1j
                    else:
                        continue
                    if portal_name not in portals_data:
                        portals_data.update({portal_name: [portal_pos]})
                    else:
                        portals_data[portal_name].append(portal_pos)
    
    # print(portals_data)
    portals = {}
    for p in portals_data.values():
        if len(p) > 1:
            portals[p[0]] = p[1] 
            portals[p[1]] = p[0]
    # print(portals)

    start = portals_data['AA'][0]
    goal = portals_data['ZZ'][0]
    fronts = [(0, start)]
    history = {start: 0}
    while fronts:
        new_fronts = []
        for steps, pos in fronts:
            new_positions = []
            for d in [1j, -1, -1j, 1]:
                new_positions.append(pos + d)
            if pos in portals:
                new_positions.append(portals[pos])
            new_steps = steps + 1
            if goal in history:
                if new_steps >= history[goal]:
                    continue
            for new_pos in new_positions:
                new_pos_stat = maze_map[int(new_pos.imag)][int(new_pos.real)]
                if new_pos_stat != '.':
                    continue
                if new_pos in history:
                    if new_steps >= history[new_pos]:
                        continue
                history[new_pos] = new_steps
                new_fronts.append((new_steps, new_pos))
        fronts = new_fronts
        # print(len(fronts))
        # print(fronts)
    print(history[goal])


def part_2(input_string):
    maze_map = list(map(list, input_string.split('\n')))
    x_range = len(maze_map[0])
    y_range = len(maze_map)
    portals_data = {}
    for x in range(x_range):
        for y in range(y_range):
            if maze_map[y][x] in ascii_uppercase:
                if 0 < x < x_range-1 and 0 < y < y_range-1:
                    if maze_map[y][x-1] == '.':
                        portal_name = ''.join(maze_map[y][x:x+2])
                        portal_pos = (x-1)+y*1j
                        if x+1 == x_range-1:
                            portal_type = -1
                        else:
                            portal_type = 1
                    elif maze_map[y][x+1] == '.':
                        portal_name = ''.join(maze_map[y][x-1:x+1])
                        portal_pos = (x+1)+y*1j
                        if x-1 == 0:
                            portal_type = -1
                        else:
                            portal_type = 1
                    elif maze_map[y-1][x] == '.':
                        portal_name = ''.join([maze_map[y][x], maze_map[y+1][x]])
                        portal_pos = x+(y-1)*1j
                        if y+1 == y_range-1:
                            portal_type = -1
                        else:
                            portal_type = 1
                    elif maze_map[y+1][x] == '.':
                        portal_name = ''.join([maze_map[y-1][x], maze_map[y][x]])
                        portal_pos = x+(y+1)*1j
                        if y-1 == 0:
                            portal_type = -1
                        else:
                            portal_type = 1
                    else:
                        continue
                    if portal_name not in portals_data:
                        portals_data.update({portal_name: [(portal_pos, portal_type)]})
                    else:
                        portals_data[portal_name].append((portal_pos, portal_type))
    
    targets = {}
    for k, v in portals_data.items():
        if len(v) > 1:
            for p in v:
                if p[1] == 1:
                    targets.update({
                        k+'_i': {
                            'pos': p[0],
                            'routes': {}
                        }
                    })
                if p[1] == -1:
                    targets.update({
                        k+'_o': {
                            'pos': p[0],
                            'routes': {}
                        }
                    })
            continue
        targets.update({
            k: {
                'pos': v[0][0],
                'routes': {}
            }
        })

    for target in targets:
        target_pos = targets[target]['pos']
        fronts = [target_pos]
        history = {target_pos: 0}
        steps = 0
        while fronts:
            steps += 1
            new_fronts = []
            for pos in fronts:
                for d in [1j, -1, -1j, 1]:
                    new_pos = pos + d
                    new_pos_stat = maze_map[int(new_pos.imag)][int(new_pos.real)]
                    if new_pos_stat != '.':
                        continue
                    if new_pos in history:
                        if steps >= history[new_pos]:
                            continue
                    history[new_pos] = steps
                    new_fronts.append(new_pos)
            fronts = new_fronts
            # print(len(fronts))
            # print(fronts)
        # print(history)
        for t in targets:
            if t == target:
                continue
            if targets[t]['pos'] in history:
                targets[target]['routes'][t] = history[targets[t]['pos']]
            if t[:2] == target[:2]:
                targets[target]['routes'][t] = 1
        # print(targets[target])
    # print(targets)

    start = 'AA'
    goal = (0, 'ZZ')
    fronts = [(0, 0, start)]
    history = {(0, start): 0}
    while fronts:
        new_fronts = []
        for steps, level, pos in fronts:
            for t in targets[pos]['routes']:
                if level > 0 and t in ['AA', 'ZZ']:
                    continue
                new_steps = steps + targets[pos]['routes'][t]
                new_level = level
                if pos[:2] == t[:2]:
                    if pos.endswith('i') and t.endswith('o'):
                        new_level += 1
                    if pos.endswith('o') and t.endswith('i'):
                        new_level -= 1
                if new_level < 0:
                    continue
                new_pos = t
                if goal in history:
                    if new_steps >= history[goal]:
                        continue
                if (new_level, new_pos) in history:
                    if new_steps >= history[(new_level, new_pos)]:
                        continue
                history[(new_level, new_pos)] = new_steps
                new_fronts.append((new_steps, new_level, new_pos))
        fronts = new_fronts
        # print(len(fronts))
        # print(fronts)
    print(history[goal])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_20.txt', 'r')
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
