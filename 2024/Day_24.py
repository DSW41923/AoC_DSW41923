import argparse
import re

from copy import deepcopy
from itertools import combinations


def get_wire_status(input_string):
    wires = list(set(re.findall(r'([a-z0-9]{3})', input_string)))
    wires.sort()
    wire_status = {}
    for wire in wires:
        wire_status.update({
            wire: {
                'value': '',
                'src': [],
                'operand': ''
            }
        })
    for wire, init_value in re.findall(r'([a-z0-9]{3}): (\d)', input_string):
        wire_status[wire]['value'] = int(init_value)

    for wire_0, operand, wire_1, wire_target in re.findall(r'([a-z0-9]{3}) (\w{2,3}) ([a-z0-9]{3}) -> ([a-z0-9]{3})', input_string):
        wire_status[wire_target].update({
            'src': [wire_0, wire_1],
            'operand': operand
        })

    return wire_status


def evaluate_wire(wire_status):
    loop_count = 0
    empty_count = len([w for w in wire_status if w.startswith('z') and wire_status[w]['value'] == ''])
    while any([wire_status[s]['value'] == '' for s in wire_status]):
        for wire in wire_status:
            if wire_status[wire]['value'] == '':
                src = wire_status[wire]['src']
                if all([wire_status[s]['value'] != '' for s in src]):
                    if wire_status[wire]['operand'] == "AND":
                        wire_status[wire]['value'] = wire_status[src[0]]['value'] & wire_status[src[1]]['value']
                    if wire_status[wire]['operand'] == "OR":
                        wire_status[wire]['value'] = wire_status[src[0]]['value'] | wire_status[src[1]]['value']
                    if wire_status[wire]['operand'] == "XOR":
                        wire_status[wire]['value'] = wire_status[src[0]]['value'] ^ wire_status[src[1]]['value']
        new_empty_count = len([w for w in wire_status if w.startswith('z') and wire_status[w]['value'] == ''])
        if new_empty_count == empty_count:
            loop_count += 1
        else:
            empty_count = new_empty_count
        
        if loop_count > 20:
            break


def get_wires_value(wire_status, initial):
    i = [(w, wire_status[w]['value']) for w in wire_status if w.startswith(initial)]
    i.sort(key=lambda r: r[0], reverse=True)
    return int(''.join([str(r[1]) for r in i]), 2)


def is_correct_wire(wire, wire_status):
    if wire.startswith('x') or wire.startswith('y'):
        return True
    operand = wire_status[wire]['operand']
    if wire.startswith('z'):
        target_bit = int(wire[1:])
        if target_bit < 45:
            return operand == 'XOR'
        return operand == 'OR'
    src = wire_status[wire]['src']
    if operand == 'OR':
        return all([wire_status[w]['operand'] == 'AND' for w in src])
    if operand in ['AND', 'XOR']:
        return all([wire_status[w]['operand'] != 'AND' for w in src])
    return False


def get_sus_incorrect_src_wire(wire, wire_status):
    operand = wire_status[wire]['operand']
    src = wire_status[wire]['src']
    if operand == 'OR':
        if not all([wire_status[w]['operand'] == 'AND' for w in src]):
            return src
    if operand == 'AND':
        src_operands = [wire_status[w]['operand'] for w in src]
        if src_operands.count('AND') > 1 or src_operands.count('XOR') < 1:
            return src
    if operand == 'XOR':
        src_operands = [wire_status[w]['operand'] for w in src]
        if src_operands.count('XOR') == 2:
            if not all([w.startswith('x') or w.startswith('y') for w in src]):
                return src
        if src_operands.count('AND') > 1 or src_operands.count('XOR') < 1:
            return src
    return []


def get_dependencies(wire, wire_status):
    dependencies = wire_status[wire]['src']
    if not dependencies:
        return []
    return dependencies + get_dependencies(dependencies[0], wire_status) + get_dependencies(dependencies[1], wire_status)


def get_wire_groups(wire_status):
    xs = len([w for w in wire_status if w.startswith('x')])
    wire_groups = []
    for i in range(xs):
        z_wire = 'z'+str(i).zfill(2)
        wire_group = {
            'XOR': '',
            'AND_0': '',
            'AND_1': '',
            'OR': '',
            'OUT': (z_wire, wire_status[z_wire])
        }
        dependencies = wire_status[z_wire]['src']
        while dependencies:
            new_dependencies = []
            for d in dependencies:
                new_dependencies.extend(wire_status[d]['src'])
                if all([(d, wire_status[d]) not in wire_groups[-i].values() for i in range(1, len(wire_groups)+1)]):
                    if wire_status[d]['operand'] == 'OR':
                        wire_group['OR'] = (d, wire_status[d])
                    elif wire_status[d]['operand'] == 'XOR':
                        if all([s.startswith('x') or s.startswith('y') for s in wire_status[d]['src']]):
                            wire_group['XOR'] = (d, wire_status[d])
                        else:
                            wire_group['OUT'] = (d, wire_status[d])
                    elif wire_status[d]['operand'] == 'AND':
                        if all([s.startswith('x') or s.startswith('y') for s in wire_status[d]['src']]):
                            wire_group['AND_0'] = (d, wire_status[d])
                        else:
                            wire_group['AND_1'] = (d, wire_status[d])
            dependencies = new_dependencies
        wire_groups.append(wire_group)
    return wire_groups


def part_1(input_string):
    wire_status = get_wire_status(input_string)
    evaluate_wire(wire_status)
    print(get_wires_value(wire_status, 'z'))


def part_2(input_string):
    wire_status = get_wire_status(input_string)
    wire_groups = get_wire_groups(wire_status)

    bad_wires = []
    sus_wires = []
    swap_pairs = []
    for id, wire_group in enumerate(wire_groups):
        if wire_group['OUT'][1]['operand'] != 'XOR':
            # First simple check, output should be 'XOR' gate with one 'XOR' input and one 'OR' input
            bad_wires.append(wire_group['OUT'][0])
            # print(id, wire_group)
            for wire in wire_status:
                if wire_status[wire]['operand'] == 'XOR':
                    src = wire_status[wire]['src']
                    if tuple([wire_status[s]['operand'] for s in src]) in [('XOR', 'OR'), ('OR', 'XOR')]:
                        check = 0
                        if wire_status[src[1]]['operand'] == 'XOR':
                            check = 1
                        if all([(w.startswith('x') or w.startswith('y')) and (int(w[1:]) == id) for w in wire_status[src[check]]['src']]):
                            # print(wire, wire_status[wire])
                            # print(wire_status[src[check]])
                            swap_pairs.append((wire_group['OUT'][0], wire))
                            bad_wires.append(wire)
        else:
            # Second simple check
            src = wire_group['OUT'][1]['src']
            for s in src:
                if id > 1 and wire_status[s]['operand'] not in ['XOR', 'OR']:
                    sus_wires.append(s)

    new_wire_status = deepcopy(wire_status)
    for w_a, w_b in swap_pairs:
        new_wire_status[w_a], new_wire_status[w_b] = new_wire_status[w_b], new_wire_status[w_a]
    # new_wire_groups = get_wire_groups(new_wire_status)
    # for i in range(len(new_wire_groups)):
    #     print(i, new_wire_groups[i])

    # print(sus_wires)
    unswapped_wires = []
    for wire in wire_status:
        if wire not in (bad_wires+sus_wires):
            if not wire.startswith('x') and not wire.startswith('y'):
                if wire.startswith('z') and wire_status[wire]['operand'] == 'XOR':
                    continue
                elif wire_status[wire]['operand'] == 'OR':
                    continue
                else:
                    unswapped_wires.append(wire)
    # print(len(unswapped_wires))
    # print(unswapped_wires)

    x_value = get_wires_value(wire_status, 'x')
    y_value = get_wires_value(wire_status, 'y')
    target = x_value+y_value
    for sus_wire in sus_wires:
        found_swap = False
        for w in unswapped_wires:
            trial_wire_status = deepcopy(new_wire_status)
            trial_wire_status[sus_wire], trial_wire_status[w] = trial_wire_status[w], trial_wire_status[sus_wire]
            evaluate_wire(trial_wire_status)
            if any([trial_wire_status[w]['value'] == '' for w in trial_wire_status if w.startswith('z')]):
                continue
            new_z = get_wires_value(trial_wire_status, 'z')
            if new_z == target:
                swap_pairs.append((sus_wire, w))
                bad_wires.extend([sus_wire, w])
                found_swap = True
                break
        if found_swap:
            break
    bad_wires.sort()
    print(','.join(bad_wires))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_24.txt', 'r')
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
