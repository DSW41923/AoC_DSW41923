import argparse
import heapq
import re

from itertools import combinations


def part_1(input_string):
    valves_data = {}
    worth_open_valves = []
    for valve_name, flow_rate, linked_valves in re.findall(r'.+ ([A-Z]+) .+=(\d+).+to valves? ([A-Z, ]+)', input_string):
        valves_data.update({
            valve_name: {
                'flow_rate': int(flow_rate),
                'linked_valves': linked_valves.split(', ')}
            })
        if flow_rate != '0':
            worth_open_valves.append(valve_name)
    visiting_valves = worth_open_valves + ['AA']
    valves_map = {}
    for valve in visiting_valves:
        valve_map = {}
        front = [(0, valve)]
        while front:
            distance, front_valve = heapq.heappop(front)
            for next_valve in valves_data[front_valve]['linked_valves']:
                new_distance = distance + 1
                edge = valve + next_valve
                if edge in valve_map:
                    old_distance = valve_map[edge]
                    valve_map[edge] = min(new_distance, valve_map[edge])
                    if valve_map[edge] != old_distance:
                        heapq.heappush(front, (new_distance, next_valve))
                else:
                    valve_map.update({edge: new_distance})
                    heapq.heappush(front, (new_distance, next_valve))
        for edge in valve_map:
            valve_0, valve_1 = edge[:2], edge[2:]
            if valve_0 == valve_1:
                continue

            if valve_0 not in visiting_valves or valve_1 not in visiting_valves:
                continue

            if valve_0 not in valves_map:
                valves_map.update({valve_0: {}})

            valves_map[valve_0].update({valve_1: valve_map[edge] + 1})

    paths = [['AA']]
    for path in paths:
        time_elapsed = 0 if len(path) == 1 else sum([valves_map[valve_0][valve_1] for valve_0, valve_1 in zip(path[:-1], path[1:])])
        for valve in valves_map[path[-1]]:
            if valve not in path and time_elapsed + valves_map[path[-1]][valve] <= 30:
                paths.append(path + [valve])
    max_released_pressure = 0
    for path in paths:
        rest_minutes = 30
        released_pressure = 0
        for valve_0, valve_1 in zip(path[:-1], path[1:]):
            rest_minutes -= (valves_map[valve_0][valve_1])
            released_pressure += rest_minutes * valves_data[valve_1]['flow_rate']
        max_released_pressure = max(max_released_pressure, released_pressure)
    print(max_released_pressure)


def part_2(input_string):
    valves_data = {}
    worth_open_valves = []
    for valve_name, flow_rate, linked_valves in re.findall(r'.+ ([A-Z]+) .+=(\d+).+to valves? ([A-Z, ]+)', input_string):
        valves_data.update({
            valve_name: {
                'flow_rate': int(flow_rate),
                'linked_valves': linked_valves.split(', ')}
            })
        if flow_rate != '0':
            worth_open_valves.append(valve_name)
    visiting_valves = worth_open_valves + ['AA']
    valves_map = {}
    for valve in visiting_valves:
        valve_map = {}
        front = [(0, valve)]
        while front:
            distance, front_valve = heapq.heappop(front)
            for next_valve in valves_data[front_valve]['linked_valves']:
                new_distance = distance + 1
                edge = valve + next_valve
                if edge in valve_map:
                    old_distance = valve_map[edge]
                    valve_map[edge] = min(new_distance, valve_map[edge])
                    if valve_map[edge] != old_distance:
                        heapq.heappush(front, (new_distance, next_valve))
                else:
                    valve_map.update({edge: new_distance})
                    heapq.heappush(front, (new_distance, next_valve))
        for edge in valve_map:
            valve_0, valve_1 = edge[:2], edge[2:]
            if valve_0 == valve_1:
                continue

            if valve_0 not in visiting_valves or valve_1 not in visiting_valves:
                continue

            if valve_0 not in valves_map:
                valves_map.update({valve_0: {}})

            valves_map[valve_0].update({valve_1: valve_map[edge] + 1})

    paths = [['AA']]
    for path in paths:
        time_elapsed = 0 if len(path) == 1 else sum([valves_map[valve_0][valve_1] for valve_0, valve_1 in zip(path[:-1], path[1:])])
        for valve in valves_map[path[-1]]:
            if valve not in path and time_elapsed + valves_map[path[-1]][valve] <= 26:
                paths.append(path + [valve])
    print('\n'.join(list(map(str, valves_map.items()))))
    def get_released_pressure(p):
        rest_minutes = 26
        released = 0
        for valve_0, valve_1 in zip(p[:-1], p[1:]):
            rest_minutes -= (valves_map[valve_0][valve_1])
            released += rest_minutes * valves_data[valve_1]['flow_rate']
        return released
    released_pressures = {''.join(p): get_released_pressure(p) for p in paths}
    paths.sort(key=lambda x: released_pressures[''.join(x)], reverse=True)
    max_released_pressure = 0
    for p0, path_0 in enumerate(paths):
        if released_pressures[''.join(path_0)] < max_released_pressure // 2:
            continue
        for p in range(p0, len(paths)):
            path_1 = paths[p]
            if list(set(path_0[1:]) & set(path_1[1:])):
                continue
            released_pressure = released_pressures[''.join(path_0)] + released_pressures[''.join(path_1)]
            max_released_pressure = max(max_released_pressure, released_pressure)
    print(max_released_pressure)



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

