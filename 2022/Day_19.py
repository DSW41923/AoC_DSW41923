import argparse
import heapq
import re


def part_1(input_string):
    blueprints = [{}]
    for data in re.findall(r'ore robot costs (\d+) ore.+clay robot costs (\d+) ore.+obsidian robot costs (\d+) ore and (\d+) clay.+geode robot costs (\d+) ore and (\d+) obsidian', input_string):
        ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost = tuple(map(int, data))
        blueprints.append({
            'ore_robot_costs': {
                'ore': ore_robot_ore_cost
                },
            'clay_robot_costs': {
                'ore': clay_robot_ore_cost
                },
            'obsidian_robot_costs': {
                'ore': obsidian_robot_ore_cost,
                'clay': obsidian_robot_clay_cost
                },
            'geode_robot_costs': {
                'ore': geode_robot_ore_cost,
                'obsidian': geode_robot_obsidian_cost
                },
            })
    print(blueprints)
    quality_level_sum = 0
    time_limit = 24
    for i, blueprint in enumerate(blueprints):
        if i == 0:
            continue
        max_geode_opened = 0
        max_ore_required = max(blueprint['ore_robot_costs']['ore'], blueprint['clay_robot_costs']['ore'], blueprint['obsidian_robot_costs']['ore'], blueprint['geode_robot_costs']['ore'])
        max_clay_required = blueprint['obsidian_robot_costs']['clay']
        max_obsidian_required = blueprint['geode_robot_costs']['obsidian']

        # geode opened, ore count, clay count, obsidain count, ore robot count, clay robot count, obsidian robot count geode robot count
        initial_state = (0, 0, 0, 0, 1, 0, 0, 0)
        states_map = {initial_state: 0}
        states = [(0, initial_state)]
        while states:
            time, state = heapq.heappop(states)
            possible_next_states = []
            new_geode_count = state[0] + state[7]
            new_ore_count = state[1] + state[4]
            new_clay_count = state[2] + state[5]
            new_obsidian_count = state[3] + state[6]
            if state[1] >= blueprint['ore_robot_costs']['ore'] and state[4] < max_ore_required:
                possible_next_states.append(
                        (new_geode_count,
                            new_ore_count - blueprint['ore_robot_costs']['ore'],
                            new_clay_count, new_obsidian_count,
                            state[4] + 1) + state[5:])

            if state[1] >= blueprint['clay_robot_costs']['ore'] and state[5] < max_clay_required:
                possible_next_states.append(
                        (new_geode_count,
                            new_ore_count - blueprint['clay_robot_costs']['ore'],
                            new_clay_count, new_obsidian_count, state[4],
                            state[5] + 1) + state[6:])

            if state[1] >= blueprint['obsidian_robot_costs']['ore'] and state[2] >= blueprint['obsidian_robot_costs']['clay'] and state[6] < max_obsidian_required:
                possible_next_states.append(
                        (new_geode_count,
                            new_ore_count - blueprint['obsidian_robot_costs']['ore'],
                            new_clay_count - blueprint['obsidian_robot_costs']['clay'],
                            new_obsidian_count) + state[4:6] + (state[6] + 1, state[7]))

            if state[1] >= blueprint['geode_robot_costs']['ore'] and state[3] >= blueprint['geode_robot_costs']['obsidian']:
                possible_next_states.append(
                        (new_geode_count,
                            new_ore_count - blueprint['geode_robot_costs']['ore'],
                            new_clay_count,
                            new_obsidian_count - blueprint['geode_robot_costs']['obsidian']) + state[4:7] + (state[7] + 1,))

            possible_next_states.append((new_geode_count, new_ore_count, new_clay_count, new_obsidian_count) + state[4:])

            time_elapsed = time + 1
            #print(time, len(states), max_geode_opened)
            if time_elapsed > time_limit:
                continue
            for next_state in possible_next_states:
                time_left = time_limit - time_elapsed
                max_possible_geodes = next_state[0] + (next_state[7] + (time_left - 1) / 2) * time_left
                if max_possible_geodes < max_geode_opened:
                    continue
                if next_state in states_map:
                    old_time_record = states_map[next_state]
                    states_map[next_state] = min(time_elapsed, old_time_record)
                    if states_map[next_state] != old_time_record:
                        heapq.heappush(states, (time_elapsed, next_state))
                    continue

                states_map.update({next_state: time_elapsed})
                heapq.heappush(states, (time_elapsed, next_state))
                max_geode_opened = max(max_geode_opened, next_state[0])
        print(i, max_geode_opened)
        quality_level_sum += i * max_geode_opened
    print(quality_level_sum)


def part_2(input_string):
    input_string = '\n'.join(input_string.split('\n')[:3])
    blueprints = [{}]
    for data in re.findall(r'ore robot costs (\d+) ore.+clay robot costs (\d+) ore.+obsidian robot costs (\d+) ore and (\d+) clay.+geode robot costs (\d+) ore and (\d+) obsidian', input_string):
        ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost = tuple(map(int, data))
        blueprints.append({
            'ore_robot_costs': {
                'ore': ore_robot_ore_cost
                },
            'clay_robot_costs': {
                'ore': clay_robot_ore_cost
                },
            'obsidian_robot_costs': {
                'ore': obsidian_robot_ore_cost,
                'clay': obsidian_robot_clay_cost
                },
            'geode_robot_costs': {
                'ore': geode_robot_ore_cost,
                'obsidian': geode_robot_obsidian_cost
                },
            })
    desired_num = 1
    time_limit = 32
    for i, blueprint in enumerate(blueprints):
        if i == 0:
            continue
        max_geode_opened = 0
        max_ore_required = max(blueprint['ore_robot_costs']['ore'], blueprint['clay_robot_costs']['ore'], blueprint['obsidian_robot_costs']['ore'], blueprint['geode_robot_costs']['ore'])
        max_clay_required = blueprint['obsidian_robot_costs']['clay']
        max_obsidian_required = blueprint['geode_robot_costs']['obsidian']

        # geode opened, ore count, clay count, obsidain count, ore robot count, clay robot count, obsidian robot count geode robot count
        initial_state = (0, 0, 0, 0, 1, 0, 0, 0)
        states_map = {initial_state: 0}
        states = [(0, initial_state)]
        while states:
            time, state = heapq.heappop(states)
            possible_next_states = []
            new_geode_count = state[0] + state[7]
            new_ore_count = state[1] + state[4]
            new_clay_count = state[2] + state[5]
            new_obsidian_count = state[3] + state[6]
            if state[1] >= blueprint['ore_robot_costs']['ore'] and state[4] < max_ore_required:
                possible_next_states.append(
                        (new_geode_count,
                            new_ore_count - blueprint['ore_robot_costs']['ore'],
                            new_clay_count, new_obsidian_count,
                            state[4] + 1) + state[5:])

            if state[1] >= blueprint['clay_robot_costs']['ore'] and state[5] < max_clay_required:
                possible_next_states.append(
                        (new_geode_count,
                            new_ore_count - blueprint['clay_robot_costs']['ore'],
                            new_clay_count, new_obsidian_count, state[4],
                            state[5] + 1) + state[6:])

            if state[1] >= blueprint['obsidian_robot_costs']['ore'] and state[2] >= blueprint['obsidian_robot_costs']['clay'] and state[6] < max_obsidian_required:
                possible_next_states.append(
                        (new_geode_count,
                            new_ore_count - blueprint['obsidian_robot_costs']['ore'],
                            new_clay_count - blueprint['obsidian_robot_costs']['clay'],
                            new_obsidian_count) + state[4:6] + (state[6] + 1, state[7]))

            if state[1] >= blueprint['geode_robot_costs']['ore'] and state[3] >= blueprint['geode_robot_costs']['obsidian']:
                possible_next_states.append(
                        (new_geode_count,
                            new_ore_count - blueprint['geode_robot_costs']['ore'],
                            new_clay_count,
                            new_obsidian_count - blueprint['geode_robot_costs']['obsidian']) + state[4:7] + (state[7] + 1,))

            possible_next_states.append((new_geode_count, new_ore_count, new_clay_count, new_obsidian_count) + state[4:])

            time_elapsed = time + 1
            #print(time, len(states), max_geode_opened)
            if time_elapsed > time_limit:
                continue
            for next_state in possible_next_states:
                time_left = time_limit - time_elapsed
                max_possible_geodes = next_state[0] + (next_state[7] + (time_left - 1) / 2) * time_left
                if max_possible_geodes < max_geode_opened:
                    continue
                if next_state in states_map:
                    old_time_record = states_map[next_state]
                    states_map[next_state] = min(time_elapsed, old_time_record)
                    if states_map[next_state] != old_time_record:
                        print("!")
                        heapq.heappush(states, (time_elapsed, next_state))
                    continue

                states_map.update({next_state: time_elapsed})
                heapq.heappush(states, (time_elapsed, next_state))
                max_geode_opened = max(max_geode_opened, next_state[0] + next_state[7] * time_left)
        print(i, max_geode_opened)
        desired_num *= max_geode_opened
    print(desired_num)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_19.txt', 'r')
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

