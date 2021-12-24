import argparse
import copy
import heapq
import re

from math import inf


ENERGY_COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
HALLWAY_ROOM_POS = {'A': 3, 'B': 5, 'C': 7, 'D': 9}


def get_index(state):
    index = {'A': [], 'B': [], 'C': [], 'D': []}
    for i, s in enumerate(state['hallway']):
        if s in index:
            index[s].append(f"H{str(i).zfill(2)}")

    for r, amphipods in state['rooms'].items():
        for i, a in enumerate(amphipods):
            if a in index:
                index[a].append(f"{r}{str(i).zfill(2)}")

    return ''.join(''.join(sorted(i)) for i in index.values())


def print_state(state):
    template = ["#############",
                "#...........#",
                "###D#A#B#C###",
                "  #B#A#D#C#",
                "  #########",
                "Current energy cost is {}".format(state['energy_cost'])]
    template[1] = ''.join(state['hallway'])
    template[2] = "###{}#{}#{}#{}###".format(state['rooms']['A'][0],
                                             state['rooms']['B'][0],
                                             state['rooms']['C'][0],
                                             state['rooms']['D'][0])
    template[3] = "  #{}#{}#{}#{}#".format(state['rooms']['A'][1],
                                           state['rooms']['B'][1],
                                           state['rooms']['C'][1],
                                           state['rooms']['D'][1])

    print('\n'.join(template))


def get_room(layout_strings):
    rooms = {'A': [], 'B': [], 'C': [], 'D': []}
    for r, amphipods in enumerate(re.findall(r'([ABCD])', ''.join(layout_strings[2:-1]))):
        if r % 4 == 0:
            rooms['A'].append(amphipods)
        if r % 4 == 1:
            rooms['B'].append(amphipods)
        if r % 4 == 2:
            rooms['C'].append(amphipods)
        if r % 4 == 3:
            rooms['D'].append(amphipods)

    return rooms


def get_state_history(initial_state, target_index):
    initial_state_index = get_index(initial_state)
    states = [(0, initial_state_index, initial_state)]
    state_history = {initial_state_index: 0}

    while states:
        cost, state_index, state = heapq.heappop(states)
        print(f"Proceesing Index: {state_index}, Energy Cost: {state_history[state_index]}", end='\r')

        possible_new_states = []
        for s, space in enumerate(state['hallway']):
            if space in state['rooms']:
                moving_amphipod = space
                hallway_to_des = state['hallway'][min(s + 1, HALLWAY_ROOM_POS[moving_amphipod]):
                                                  max(s, HALLWAY_ROOM_POS[moving_amphipod] + 1)]
                if all(ss == '.' for ss in hallway_to_des):
                    if all(a in ['.', moving_amphipod] for a in state['rooms'][moving_amphipod]):
                        moving_dest_pos = state['rooms'][space].count('.') - 1
                        new_state = copy.deepcopy(state)
                        new_state['rooms'][moving_amphipod][moving_dest_pos] = moving_amphipod
                        new_state['hallway'][s] = '.'
                        moving_energy_cost = ENERGY_COST[moving_amphipod] * (
                                abs(s - HALLWAY_ROOM_POS[moving_amphipod]) + moving_dest_pos + 1)
                        possible_new_states.append((new_state, moving_energy_cost))

        for r, amphipods in state['rooms'].items():
            if not all(a == r for a in amphipods):
                for i, a in enumerate(amphipods):
                    if a != '.':
                        moving_amphipod = a

                        for j, s in enumerate(state['hallway'][:HALLWAY_ROOM_POS[r]][::-1]):
                            if s in state['rooms']:
                                break
                            moving_dest_pos = HALLWAY_ROOM_POS[r] - j - 1
                            if s == '.' and moving_dest_pos not in HALLWAY_ROOM_POS.values():
                                moving_energy_cost = ENERGY_COST[moving_amphipod] * (
                                        abs(moving_dest_pos - HALLWAY_ROOM_POS[r]) + i + 1)
                                new_state = copy.deepcopy(state)
                                new_state['hallway'][moving_dest_pos] = moving_amphipod
                                new_state['rooms'][r][i] = '.'
                                possible_new_states.append((new_state, moving_energy_cost))

                        for j, s in enumerate(state['hallway'][HALLWAY_ROOM_POS[r] + 1:]):
                            if s in state['rooms']:
                                break
                            moving_dest_pos = HALLWAY_ROOM_POS[r] + j + 1
                            if s == '.' and moving_dest_pos not in HALLWAY_ROOM_POS.values():
                                moving_energy_cost = ENERGY_COST[moving_amphipod] * (
                                        abs(moving_dest_pos - HALLWAY_ROOM_POS[r]) + i + 1)
                                new_state = copy.deepcopy(state)
                                new_state['hallway'][moving_dest_pos] = moving_amphipod
                                new_state['rooms'][r][i] = '.'
                                possible_new_states.append((new_state, moving_energy_cost))

                        break

        for new_state, moving_energy_cost in possible_new_states:
            new_state_index = get_index(new_state)
            new_energy_cost = moving_energy_cost + state_history[state_index]

            if new_state_index in state_history:
                old_energy_cost = state_history[new_state_index]
                state_history[new_state_index] = min(new_energy_cost, old_energy_cost)
                if target_index in state_history:
                    if state_history[new_state_index] >= state_history[target_index] and \
                            new_state_index != target_index:
                        continue
                if state_history[new_state_index] != old_energy_cost:
                    heapq.heappush(states, (new_energy_cost, new_state_index, new_state))
            else:
                state_history.update({
                    new_state_index: new_energy_cost
                })
                heapq.heappush(states, (new_energy_cost, new_state_index, new_state))

    return state_history


def part_1(input_string, by_hand=False):
    layout_strings = input_string.splitlines()
    rooms = get_room(layout_strings)

    if by_hand:
        min_energy_cost = inf
        state = {
            'rooms': copy.deepcopy(rooms),
            'hallway': list(layout_strings[1]),
            'energy_cost': 0
        }

        while True:
            print("Current State:")
            print_state(state)
            moving = input("Moving which amphipod from where to where? "
                           "(A, B, C, D for rooms; H for hallway, by index, such as A0,H4): ")
            moving_source, moving_dest = moving.split(',')
            moving_amphipod_pos = int(moving_source[1:])
            if moving_source[0] == 'H':
                moving_amphipod = state['hallway'][moving_amphipod_pos]
                if moving_dest[0] == 'H':
                    moving_dest_pos = int(moving_dest[1:])
                    state['energy_cost'] += ENERGY_COST[moving_amphipod] * abs(moving_amphipod_pos - moving_dest_pos)
                    state['hallway'][moving_amphipod_pos] = '.'
                    state['hallway'][moving_dest_pos] = moving_amphipod
                elif moving_dest[0] in state['rooms']:
                    if moving_amphipod != moving_dest[0]:
                        continue
                    moving_dest_pos = int(moving_dest[1])
                    state['energy_cost'] += ENERGY_COST[moving_amphipod] * (
                            abs(moving_amphipod_pos - HALLWAY_ROOM_POS[moving_amphipod]) + moving_dest_pos + 1)
                    state['hallway'][moving_amphipod_pos] = '.'
                    state['rooms'][moving_dest[0]][moving_dest_pos] = moving_amphipod

            elif moving_source[0] in state['rooms']:
                moving_amphipod = state['rooms'][moving_source[0]][moving_amphipod_pos]
                if moving_dest[0] == 'H':
                    moving_dest_pos = int(moving_dest[1:])
                    state['energy_cost'] += ENERGY_COST[moving_amphipod] * (
                            abs(moving_dest_pos - HALLWAY_ROOM_POS[moving_source[0]]) + moving_amphipod_pos + 1)
                    state['rooms'][moving_source[0]][moving_amphipod_pos] = '.'
                    state['hallway'][moving_dest_pos] = moving_amphipod
                elif moving_dest[0] in state['rooms']:
                    if moving_amphipod != moving_dest[0]:
                        continue
                    moving_dest_pos = int(moving_dest[1])
                    state['energy_cost'] += ENERGY_COST[moving_amphipod] * (
                            moving_amphipod_pos + moving_dest_pos +
                            abs(HALLWAY_ROOM_POS[moving_source[0]] - HALLWAY_ROOM_POS[moving_dest[0]]) + 2)
                    state['rooms'][moving_source[0]][moving_amphipod_pos] = '.'
                    state['rooms'][moving_dest[0]][moving_dest_pos] = moving_amphipod
            else:
                moving_amphipod = None

            if not moving_amphipod:
                continue

            if all(all(a == r for a in state['rooms'][r]) for r in state['rooms']):
                min_energy_cost = min(state['energy_cost'], min_energy_cost)
                print("All amphipods returned to the right room!")
                print("Minimium energy cost till now is {}".format(min_energy_cost))
                restarting = input("Restart? (Y/N) ") == 'Y'
                if not restarting:
                    break

                state = {
                    'rooms': copy.deepcopy(rooms),
                    'hallway': list(layout_strings[1]),
                    'energy_cost': 0
                }

    if not by_hand:
        initial_state = {
            'rooms': copy.deepcopy(rooms),
            'hallway': list(layout_strings[1])
        }
        target_index = "A00A01B00B01C00C01D00D01"
        state_history = get_state_history(initial_state, target_index)

        print()
        print(state_history[target_index])


def part_2(input_string):
    layout_strings = input_string.splitlines()
    layout_strings.insert(3, "  #D#C#B#A#")
    layout_strings.insert(4, "  #D#B#A#C#")

    rooms = get_room(layout_strings)
    initial_state = {
        'rooms': copy.deepcopy(rooms),
        'hallway': list(layout_strings[1])
    }
    target_index = "A00A01A02A03B00B01B02B03C00C01C02C03D00D01D02D03"
    state_history = get_state_history(initial_state, target_index)

    print()
    print(state_history[target_index])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    parser.add_argument("--by_hand",
                        help="Specify solving puzzle 1 by hand or not. False by default.",
                        required=False)
    args = parser.parse_args()
    input_string = "#############\n" \
                   "#...........#\n" \
                   "###D#A#B#C###\n" \
                   "  #B#A#D#C#\n" \
                   "  #########"

    if args.part == '1':
        part_1(input_string, args.by_hand in ['True', 'T', 'Y', 'Yes'])
    elif args.part == '2':
        part_2(input_string)
    else:
        part_1(input_string)
        part_2(input_string)


if __name__ == "__main__":
    main()
