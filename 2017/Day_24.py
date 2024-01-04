import argparse


def part_1(input_string):
    components = list(map(lambda p: tuple(p.split('/')), input_string.split('\n')))
    bridges = [(0, '0')]
    max_strength = 0
    while bridges:
        new_bridges = []
        strength, bridge = bridges.pop(0)
        bridge_components = bridge.split('/')
        last_bridge_component = ''
        for bc in bridge_components:
            if bridge_components.count(bc) % 2:
                last_bridge_component = bc
                break
        for component in components:
            if last_bridge_component in component:
                bridge_component = '/'.join(component)
                bridge_component_strength = int(component[0]) + int(component[1])
                if bridge_component not in bridge:
                    new_bridges.append((strength + bridge_component_strength, bridge + '/' + bridge_component))
        bridges.extend(new_bridges)
        bridges.sort(key=lambda b: b[0], reverse=True)
        if bridges:
            max_strength = max(max_strength, bridges[0][0])
    print(max_strength)


def part_2(input_string):
    components = list(map(lambda p: tuple(p.split('/')), input_string.split('\n')))
    bridges = [(0, '0')]
    max_length = 0
    max_strength = 0
    while bridges:
        new_bridges = []
        strength, bridge = bridges.pop(0)
        bridge_components = bridge.split('/')
        last_bridge_component = ''
        for bc in bridge_components:
            if bridge_components.count(bc) % 2:
                last_bridge_component = bc
                break
        for component in components:
            if last_bridge_component in component:
                bridge_component = '/'.join(component)
                bridge_component_strength = int(component[0]) + int(component[1])
                if bridge_component not in bridge:
                    new_bridges.append((strength + bridge_component_strength, bridge + '/' + bridge_component))
        bridges.extend(new_bridges)
        bridges.sort(key=lambda b: b[1].count('/'), reverse=True)
        if bridges:
            max_length = max(max_length, bridges[0][1].count('/'))
            if max_length == bridges[0][1].count('/'):
                max_strength = max(max_strength, bridges[0][0])
    print(max_strength)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2017/Input_24.txt', 'r')
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
