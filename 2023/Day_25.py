import argparse
import heapq
import re

from collections import Counter
from copy import deepcopy
from itertools import combinations

def part_1(input_string):
    components = []
    wires = []
    for component, connected_components in re.findall(r"(\w{3}): ([\w ]+)", input_string):
        connected_components = connected_components.split(' ')
        if component not in components:
            components.append(component)
        for c in connected_components:
            if c not in components:
                components.append(c)
            wire = (component, c)
            reversed_wire = (c, component)
            if wire not in wires and reversed_wire not in wires:
                wires.append(wire)
    def traverse(start, result):
        front_components = [(0, start, '')]
        while front_components:
            steps, component, path = heapq.heappop(front_components)
            next_components = []
            for wire in wires:
                if component in wire:
                    if wire[0] != component:
                        next_components.append(wire[0])
                    else: next_components.append(wire[1])

            for next_component in next_components:
                new_steps = steps + 1
                new_path = path + ',' + str(component)
                if path == '':
                    new_path = str(component)
                if next_component in result[start]:
                    old_steps = result[start][next_component]['steps']
                    result[start][next_component]['steps'] = min(new_steps, old_steps)
                    if result[start][next_component]['steps'] != old_steps:
                        result[start][next_component]['path'] = new_path
                        heapq.heappush(front_components, (new_steps, next_component, new_path))
                else:
                    result[start].update({
                        next_component: {
                            'steps': new_steps,
                            'path': new_path
                        }
                    })
                    heapq.heappush(front_components, (new_steps, next_component, new_path))
    traversed_result = {components[0]:{}}
    traverse(components[0], traversed_result)
    longest_distance = max([c['steps'] for c in traversed_result[components[0]].values()])
    furthest_components = [c for c in traversed_result[components[0]] if traversed_result[components[0]][c]['steps'] == longest_distance]
    for i in range(3):
        traversed_result.update({furthest_components[i]:{}})
        traverse(furthest_components[i], traversed_result)
        path = traversed_result[furthest_components[i]][components[0]]['path'].split(',') + [components[0]]
        for j in range(len(path)-1):
            if (p:=(path[j],path[j+1])) in wires:
                wires.remove(p)
            else: 
                wires.remove(tuple(reversed(p)))
    traversed_result.update({components[0]:{}})
    traverse(components[0], traversed_result)
    print(len(traversed_result[components[0]])*(len(components)-len(traversed_result[components[0]])))


def part_2(input_string):
    print("Merry Christmas!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2023/Input_25.txt', 'r')
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
