import argparse
import re

from math import lcm


def get_modules_data(input_string):
    modules = {}
    for type, name, destinations in re.findall(r"([&%]?)([\w]+) -> ([\w, ]+)", input_string):
        if name not in modules:
            modules.update({
                name: {
                    'type': type if type else 'B', # Use B for non-typed broadcast
                    'sent': None,
                    'destinations': destinations.split(', '),
                }
            })
            for dest in modules[name]['destinations']:
                if dest not in modules:
                    modules.update({
                        dest: {
                            'type': None,
                            'sent': None,
                            'destinations': [],
                        }
                    })
        else:
            modules[name].update({
                'type': type if type else 'B', # Use B for non-typed broadcast
                'destinations': destinations.split(', '),
            })
    
    for name in modules:
        if modules[name]['type'] == '%':
            modules[name].update({'state': 0}) # 0 also stands for off
        else:
            modules[name].update({'inputs': {}})

    for name in modules:
        for dest in modules[name]['destinations']:
            if modules[dest]['type'] != '%':
                modules[dest]['inputs'].update({name: 0}) # 0 stands for low pulse
    
    return modules


def part_1(input_string):
    modules = get_modules_data(input_string)
    pushing_times = 1000
    sent = [0, 0]
    for _ in range(pushing_times):
        sent[0] += 1
        modules['broadcaster']['sent'] = 0
        sent[0] += len(modules['broadcaster']['destinations'])
        trasmitting_modules = [('broadcaster', m) for m in modules['broadcaster']['destinations']]
        while trasmitting_modules:
            next_trasmitting_modules = []
            for src, dest in trasmitting_modules:
                if modules[dest]['type'] == '%' and modules[src]['sent'] == 0:
                    modules[dest]['state'] ^= 1
                    modules[dest]['sent'] = modules[dest]['state']
                    sent[modules[dest]['sent']] += len(modules[dest]['destinations'])
                    for m in modules[dest]['destinations']:
                        if (dest, m) not in next_trasmitting_modules:
                            next_trasmitting_modules.append((dest, m))
                if modules[dest]['type'] == '&':
                    modules[dest]['inputs'][src] = modules[src]['sent']
                    modules[dest]['sent'] = 1^all([r == 1 for r in modules[dest]['inputs'].values()])
                    sent[modules[dest]['sent']] += len(modules[dest]['destinations'])
                    for m in modules[dest]['destinations']:
                        if (dest, m) not in next_trasmitting_modules:
                            next_trasmitting_modules.append((dest, m))

            trasmitting_modules = next_trasmitting_modules
        for module in modules.values():
            module['sent'] = None
    print(sent[0] * sent[1])


def part_2(input_string):
    modules = get_modules_data(input_string)
    cycles = {}
    target_modules = ['rx']
    while target_modules:
        next_modules = []
        for target_module in target_modules:
            if all([modules[m]['type'] == '%' for m in modules[target_module]['inputs']]):
                if target_module not in cycles:
                    cycles.update({target_module: 0})
            else:
                next_modules.extend(list(modules[target_module]['inputs'].keys()))
        target_modules = list(set(next_modules))
    pushing_times = 0
    while True:
        pushing_times += 1
        modules['broadcaster']['sent'] = 0
        trasmitting_modules = [('broadcaster', m) for m in modules['broadcaster']['destinations']]
        while trasmitting_modules:
            next_trasmitting_modules = []
            for src, dest in trasmitting_modules:
                if modules[dest]['type'] == '%' and modules[src]['sent'] == 0:
                    modules[dest]['state'] ^= 1
                    modules[dest]['sent'] = modules[dest]['state']
                    for m in modules[dest]['destinations']:
                        if (dest, m) not in next_trasmitting_modules:
                            next_trasmitting_modules.append((dest, m))
                if modules[dest]['type'] == '&':
                    modules[dest]['inputs'][src] = modules[src]['sent']
                    modules[dest]['sent'] = 1^all([r == 1 for r in modules[dest]['inputs'].values()])
                    for m in modules[dest]['destinations']:
                        if (dest, m) not in next_trasmitting_modules:
                            next_trasmitting_modules.append((dest, m))
                for module in cycles:
                    if modules[module]['sent'] == 0:
                        if not cycles[module]:
                            cycles[module] = pushing_times
            trasmitting_modules = next_trasmitting_modules
        
        if all([c for c in cycles.values()]):
            break

        for module in modules.values():
            module['sent'] = None

    print(lcm(*[c for c in cycles.values()]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2023/Input_20.txt', 'r')
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
