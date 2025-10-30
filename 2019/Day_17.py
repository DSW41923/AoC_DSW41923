import argparse

from Day_13 import IntCodeComputer
from copy import deepcopy


def part_1(input_string):
    computer = IntCodeComputer(input_string)
    computer.run()
    outputs = computer.get_outputs()
    scaffolds = []
    pos = 0
    for output in outputs:
        if chr(output) == '#':
            scaffolds.append(pos)
            pos += 1
        elif chr(output) == '.':
            pos += 1
        elif chr(output) == '\n':
            pos -= int(pos.real)
            pos += 1j
        # print(chr(output), end='')
    intersections = []
    result = 0
    for scaffold in scaffolds:
        if scaffold-1 in scaffolds and scaffold+1 in scaffolds and scaffold-1j in scaffolds and scaffold+1j in scaffolds:
            intersections.append((int(scaffold.real), int(scaffold.imag)))
            result += (int(scaffold.real) * int(scaffold.imag))
    print(result)


def part_2(input_string):
    computer = IntCodeComputer(input_string)
    computer.run()
    outputs = computer.get_outputs()
    scaffolds = []
    pos = 0
    bot = (None, None)
    for output in outputs:
        if chr(output) == '#':
            scaffolds.append(pos)
            pos += 1
        elif chr(output) == '.':
            pos += 1
        elif chr(output) == '\n':
            pos -= int(pos.real)
            pos += 1j
        elif chr(output) == '^':
            bot = (pos, -1j)
            pos += 1
        # print(chr(output), end='')

    intersections = []
    for scaffold in scaffolds:
        if scaffold-1 in scaffolds and scaffold+1 in scaffolds and scaffold-1j in scaffolds and scaffold+1j in scaffolds:
            intersections.append(scaffold)

    facing_options = [1j, -1, -1j, 1]
    fronts = [(bot, [], scaffolds+intersections)]
    routes = []
    while fronts:
        new_fronts = []
        for bot, steps, untraversed in fronts:
            if len(untraversed) == 0:
                routes.append(steps)
                continue
            bot_pos, bot_facing = bot
            if bot_pos == (38+11j) and 50 in untraversed:
                continue
            if bot_pos == (44+39) and any([t.real > 44 for t in untraversed]):
                continue
            if bot_pos == (28+43j) and any([t.real > 28 for t in untraversed]):
                continue
            for facing in facing_options:
                new_pos = bot_pos+facing
                if new_pos.real < 0 or new_pos.imag < 0:
                    continue
                new_facing = facing
                new_steps = deepcopy(steps)
                new_untraversed = deepcopy(untraversed)
                if new_pos in new_untraversed:
                    new_untraversed.remove(new_pos)
                    if facing == bot_facing:
                        new_steps[-1] += 1
                    else:
                        if bot_pos in intersections:
                            continue
                        if facing_options.index(facing) - facing_options.index(bot_facing) == 1 or (facing == 1j and bot_facing == 1):
                            new_steps.extend(['R', 1])
                        elif facing_options.index(facing) - facing_options.index(bot_facing) == -1 or (facing == 1 and bot_facing == 1j):
                            new_steps.extend(['L', 1])
                        else:
                            continue
                    new_fronts.append(((new_pos, new_facing), new_steps, new_untraversed))
            
        fronts = new_fronts

    route = routes[0]
    route = [(route[i], str(route[i+1])) for i in range(0, len(route), 2)]
    sub_routes = {'A':[], 'B': [], 'C': []}
    for sub in sub_routes:
        pointers = []
        for i, r in enumerate(route):
            if i not in sub_routes['A'] + sub_routes['B'] + sub_routes['C']:
                if len(pointers) == 0:
                    pointers.append([i])
                    continue
                if route[pointers[0][0]] == r and pointers[0][0] != i:
                    pointers.append([i])
        while pointers:
            new_pointers = []
            for p in pointers:
                new_p = p + [p[-1]+1]
                if new_p[-1] >= len(route):
                    continue
                if len(new_pointers) == 0:
                    new_pointers.append([new_p])
                    continue
                for nps in new_pointers:
                    if tuple([route[i] for i in nps[-1]]) == tuple([route[i] for i in new_p]):
                        nps.append(new_p)
                        break
                if all([new_p not in nps for nps in new_pointers]):
                    new_pointers.append([new_p])
            new_pointers.sort(key=lambda p:len(p), reverse=True)
            if len(new_pointers[0]) < len(pointers) and len(pointers[0]) > 1:
                break
            pointers = new_pointers[0]
            # print(pointers)
        for p in pointers:
            sub_routes[sub] += p

    functions = {'A':"", 'B': "", 'C': ""}
    for sub in sub_routes:
        for i in range(len(sub_routes[sub])):
            if len(functions[sub]) > 1:
                functions[sub] += ','
            functions[sub] += ','.join(route[sub_routes[sub][i]])
            if sub_routes[sub][i+1] - sub_routes[sub][i] > 1:
                break

    main_routine = ""
    cur = 0
    while cur < len(route):
        if len(main_routine) > 0:
            main_routine += ','
        for sub in sub_routes:
            if cur in sub_routes[sub]:
                main_routine += sub
                cur += (functions[sub].count('L')+functions[sub].count('R'))
                break

    inputs = []
    for c in main_routine:
        inputs.append(ord(c))
    inputs.append(ord('\n'))
    for function in functions:
        for c in functions[function]:
            inputs.append(ord(c))
        inputs.append(ord('\n'))
    inputs.append(ord('n'))  # Video streaming, y/n
    inputs.append(ord('\n'))

    new_computer = IntCodeComputer(input_string)
    new_computer.set_memory(0, 2)
    for i in inputs:
        new_computer.add_input(i)
    new_computer.run()
    outputs = new_computer.get_outputs()
    print(outputs[-1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_17.txt', 'r')
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
