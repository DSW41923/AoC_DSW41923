import argparse

from copy import deepcopy
from math import inf
from string import ascii_lowercase, ascii_uppercase


def part_1(input_string):
    area_map = list(map(list, input_string.split('\n')))
    x_range = len(area_map[0])
    y_range = len(area_map)
    targets = {
        'start': {
            'pos': None,
            'routes': {}
        }
    }
    door_keys = []
    for x in range(x_range):
        for y in range(y_range):
            if area_map[y][x] in ascii_lowercase:
                door_keys.append(area_map[y][x])
                targets[area_map[y][x]] = {
                    'pos': x+y*1j,
                    'routes': {}
                }
            elif area_map[y][x] == '@':
                targets['start']['pos'] = x+y*1j
                area_map[y][x] = '.'
    # print(door_keys)

    for target in targets:
        target_pos = targets[target]['pos']
        fronts = [(0, target_pos, [], [])]
        history = {target_pos: 0}
        while fronts:
            new_fronts = []
            for steps, pos, doors, traversed in fronts:
                directions = [1j, -1, -1j, 1]
                new_steps = steps + 1
                for d in directions:
                    new_pos = pos + d
                    new_pos_stat = area_map[int(new_pos.imag)][int(new_pos.real)]
                    new_doors = deepcopy(doors)
                    new_traversed = deepcopy(traversed)
                    if new_pos in new_traversed:
                        continue
                    new_traversed.append(new_pos)
                    if new_pos_stat == '#':
                        continue
                    if new_pos_stat in ascii_uppercase:
                        new_doors.append(new_pos_stat)
                    if new_pos_stat in ascii_lowercase:
                        if new_pos_stat != target:
                            if new_pos_stat not in targets[target]['routes']:
                                targets[target]['routes'].update({
                                    new_pos_stat: {
                                        'steps': new_steps,
                                        'doors': doors
                                    }
                                })
                                targets[new_pos_stat]['routes'].update({
                                    target: {
                                        'steps': new_steps,
                                        'doors': doors
                                    }
                                })
                            else:
                                if new_steps < targets[target]['routes'][new_pos_stat]['steps']:
                                    targets[target]['routes'][new_pos_stat]['steps'] = new_steps
                    if new_pos in history:
                        if new_steps >= history[new_pos]:
                            continue
                    history[new_pos] = new_steps
                    new_fronts.append((new_steps, new_pos, new_doors, new_traversed))
                fronts = new_fronts
        # print(targets[target])
    # print(targets)

    states = [(0, 'start', '')]
    states_history = {('start', ''): 0}
    result = inf
    while states:
        new_states = states[1000:]
        for steps, pos, held_keys in states[:1000]:
        # for steps, pos, held_keys in states:
            for t in targets[pos]['routes']:
                if t != 'start' and t not in held_keys:
                    if all(d.lower() in held_keys for d in targets[pos]['routes'][t]['doors']):
                        new_steps = steps + targets[pos]['routes'][t]['steps']
                        if new_steps >= result:
                            continue
                        new_pos = t
                        new_held_keys = held_keys
                        new_held_keys += t
                        new_held_keys = list(new_held_keys)
                        new_held_keys.sort()
                        new_held_keys = ''.join(new_held_keys)
                        if all(k in new_held_keys for k in door_keys):
                            result = new_steps
                            continue
                        if (new_pos, new_held_keys) in states_history:
                            if new_steps >= states_history[(new_pos, new_held_keys)]:
                                continue
                        states_history[(new_pos, new_held_keys)] = new_steps
                        if any([p == new_pos and k == new_held_keys and s <= new_steps for s, p, k in new_states]):
                            continue
                        new_states.append((new_steps, new_pos, new_held_keys))
        states = new_states
        states.sort(key=lambda s: len(s[2])*100000-s[0], reverse=True)
        # print(len(states), result)
    print(result)


def part_2(input_string):
    area_map = list(map(list, input_string.split('\n')))
    x_range = len(area_map[0])
    y_range = len(area_map)
    targets = {}
    door_keys = []
    for x in range(x_range):
        for y in range(y_range):
            if area_map[y][x] in ascii_lowercase:
                door_keys.append(area_map[y][x])
                targets[area_map[y][x]] = {
                    'pos': x+y*1j,
                    'routes': {}
                }
            elif area_map[y][x] == '@':
                area_map[y-1][x-1] = '.'
                area_map[y-1][x] = '#'
                area_map[y-1][x+1] = '.'
                area_map[y][x-1] = '#'
                area_map[y][x] = '#'
                area_map[y][x+1] = '#'
                area_map[y+1][x-1] = '.'
                area_map[y+1][x] = '#'
                area_map[y+1][x+1] = '.'
                for i, pos in enumerate([(y-1, x-1), (y-1, x+1), (y+1, x-1), (y+1, x+1)]):
                    a, b = pos
                    targets.update({
                        'robot'+str(i):{
                            'pos': a+b*1j,
                            'routes': {}
                        }
                    })
    # print(door_keys)

    for target in targets:
        target_pos = targets[target]['pos']
        fronts = [(0, target_pos, [], [])]
        history = {target_pos: 0}
        while fronts:
            new_fronts = []
            for steps, pos, doors, traversed in fronts:
                directions = [1j, -1, -1j, 1]
                new_steps = steps + 1
                for d in directions:
                    new_pos = pos + d
                    new_pos_stat = area_map[int(new_pos.imag)][int(new_pos.real)]
                    new_doors = deepcopy(doors)
                    new_traversed = deepcopy(traversed)
                    if new_pos in new_traversed:
                        continue
                    new_traversed.append(new_pos)
                    if new_pos_stat == '#':
                        continue
                    if new_pos_stat in ascii_uppercase:
                        new_doors.append(new_pos_stat)
                    if new_pos_stat in ascii_lowercase:
                        if new_pos_stat != target:
                            if new_pos_stat not in targets[target]['routes']:
                                targets[target]['routes'].update({
                                    new_pos_stat: {
                                        'steps': new_steps,
                                        'doors': doors
                                    }
                                })
                                targets[new_pos_stat]['routes'].update({
                                    target: {
                                        'steps': new_steps,
                                        'doors': doors
                                    }
                                })
                            else:
                                if new_steps < targets[target]['routes'][new_pos_stat]['steps']:
                                    targets[target]['routes'][new_pos_stat]['steps'] = new_steps
                    if new_pos in history:
                        if new_steps >= history[new_pos]:
                            continue
                    history[new_pos] = new_steps
                    new_fronts.append((new_steps, new_pos, new_doors, new_traversed))
                fronts = new_fronts
    # print(targets)

    states = [(0, ('robot0', 'robot1', 'robot2', 'robot3'), '')]
    states_history = {(('robot0', 'robot1', 'robot2', 'robot3'), ''): 0}
    result = inf
    while states:
        new_states = states[1000:]
        for steps, pos, held_keys in states[:1000]:
        # for steps, pos, held_keys in states:
            for i, pp in enumerate(pos):
                for t in targets[pp]['routes']:
                    if not t.startswith('robot') and t not in held_keys:
                        if all(d.lower() in held_keys for d in targets[pp]['routes'][t]['doors']):
                            new_steps = steps + targets[pp]['routes'][t]['steps']
                            if new_steps >= result:
                                continue
                            new_pos = list(deepcopy(pos))
                            new_pos[i] = t
                            new_pos = tuple(new_pos)
                            new_held_keys = held_keys
                            new_held_keys += t
                            new_held_keys = list(new_held_keys)
                            new_held_keys.sort()
                            new_held_keys = ''.join(new_held_keys)
                            if all(k in new_held_keys for k in door_keys):
                                result = new_steps
                                continue
                            if (new_pos, new_held_keys) in states_history:
                                if new_steps >= states_history[(new_pos, new_held_keys)]:
                                    continue
                            states_history[(new_pos, new_held_keys)] = new_steps
                            if any([p == new_pos and k == new_held_keys and s <= new_steps for s, p, k in new_states]):
                                continue
                            new_states.append((new_steps, new_pos, new_held_keys))
        states = new_states
        states.sort(key=lambda s: len(s[2])*100000-s[0], reverse=True)
        # print(len(states), result)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_18.txt', 'r')
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
