import argparse
import re

from copy import deepcopy


class UnitGroup(object):

    def __init__(self, type, unit_count, hp, weak, immunity, atk, atk_type, atk_initiative):
        self.type = type
        self.unit_count = unit_count
        self.hp = hp
        self.weak = weak
        self.immune = immunity
        self.atk = atk
        self.atk_type = atk_type
        self.atk_initiative = atk_initiative

    def effective_power(self):
        return self.unit_count*self.atk

    def __str__(self):
        return " ".join(list(map(str, [self.type, self.unit_count, self.hp, self.weak, self.immune, self.atk, self.atk_type, self.atk_initiative])))


def parse_data_line(line):
    unit_count = re.search(r"(\d+) units", line)
    if unit_count:
        unit_count = int(unit_count.group(1))
    else:
        unit_count = -1
    hp = re.search(r"(\d+) hit points", line)
    if hp:
        hp = int(hp.group(1))
    else:
        hp = -1
    weak = re.search(r"weak to ([\w, ]+)[\);]", line)
    if weak:
        weak = weak.group(1).split(', ')
    else:
        weak = []
    immunity = re.search(r"immune to ([\w, ]+)[\);]", line)
    if immunity:
        immunity = immunity.group(1).split(', ')
    else:
        immunity = []
    atk = re.search(r"attack that does (\d+)", line)
    if atk:
        atk = int(atk.group(1))
    else:
        atk = -1
    atk_type = re.search(r"(\w+) damage", line)
    if atk_type:
        atk_type = atk_type.group(1)
    else:
        atk_type = None
    atk_initiative = re.search(r"initiative (\d+)", line)
    if atk_initiative:
        atk_initiative = int(atk_initiative.group(1))
    else:
        atk_initiative = -1
    return unit_count, hp, weak, immunity, atk, atk_type, atk_initiative


def parse_data(input_string):
    unit_groups = []
    immune_system_unit_groups_data, infection_unit_groups_data = input_string.split('\n\n')
    for line in immune_system_unit_groups_data.split('\n'):
        unit_type = "IS"
        unit_count, hp, weak, immunity, atk, atk_type, atk_initiative = parse_data_line(line)
        # print(line)
        # print(unit_type, unit_count, hp, weak, immunity, atk, atk_type, atk_initiative)
        if unit_count == -1 or hp == -1 or atk == -1 or atk_initiative == -1:
            continue
        unit_groups.append(UnitGroup(unit_type, unit_count, hp, weak, immunity, atk, atk_type, atk_initiative))
    for line in infection_unit_groups_data.split('\n'):
        unit_type = "IF"
        unit_count, hp, weak, immunity, atk, atk_type, atk_initiative = parse_data_line(line)
        # print(line)
        # print(unit_type, unit_count, hp, weak, immunity, atk, atk_type, atk_initiative)
        if unit_count == -1 or hp == -1 or atk == -1 or atk_initiative == -1:
            continue
        unit_groups.append(UnitGroup(unit_type, unit_count, hp, weak, immunity, atk, atk_type, atk_initiative))
    return unit_groups


def get_attacking_damage(attacker, target):
    if attacker.atk_type in target.immune:
        return 0
    return attacker.effective_power() * (1 + 1 * (attacker.atk_type in target.weak))


def combat(unit_groups):
    while not (all([unit.type == 'IS' for unit in unit_groups]) or all([unit.type == 'IF' for unit in unit_groups])):
        # target selecting
        unit_groups.sort(key=lambda g: g.effective_power()*100+g.atk_initiative, reverse=True)
        unit_groups_str = ', '.join(list(map(str, unit_groups)))
        targets = [None for _ in range(len(unit_groups))]
        for i, unit_group in enumerate(unit_groups):
            target_evaluations = []
            for j, target_ug in enumerate(unit_groups):
                if j != i and j not in targets and target_ug.type != unit_group.type:
                    attacking_damage = get_attacking_damage(unit_group, target_ug)
                    if attacking_damage > 0:
                        target_evaluations.append((j, get_attacking_damage(unit_group, target_ug)))
            if target_evaluations:
                target_evaluations.sort(key=lambda e: e[1]*100000000+unit_groups[e[0]].effective_power()*100+unit_groups[e[0]].atk_initiative, reverse=True)
                targets[i] = target_evaluations[0][0]
        # print(targets)
        battling_pair = []
        for i, t in enumerate(targets):
            if t is None:
                battling_pair.append((unit_groups[i], None))
                continue
            battling_pair.append((unit_groups[i], unit_groups[t]))
        battling_pair.sort(key=lambda p: p[0].atk_initiative, reverse=True)
        # attacking
        for attacker, target in battling_pair:
            if target:
                attacking_damage = get_attacking_damage(attacker, target)
                if attacking_damage == 0:
                    continue
                defeated_units = attacking_damage//target.hp
                defeated_units = min(defeated_units, target.unit_count)
                # print('({}) attacks ({})'.format(attacker, target), end='')
                # print(' with {} damage'.format(attacking_damage), end='')
                # print(', defeated {} units'.format(defeated_units))
                target.unit_count -= defeated_units
            # else:
            #     print(attacker, end='')
            #     print(' attacks no one!')
        remaining_unit_groups = []
        for unit_group in unit_groups:
            if unit_group.unit_count > 0:
                remaining_unit_groups.append(unit_group)
        remaining_unit_groups.sort(key=lambda ug: ug.atk_initiative, reverse=True)
        if ', '.join(list(map(str, remaining_unit_groups))) == unit_groups_str:
            break
        unit_groups = remaining_unit_groups
        # for g in unit_groups: print(g)
    return unit_groups


def part_1(input_string):
    unit_groups = parse_data(input_string)
    unit_groups = combat(unit_groups)
    print(sum([ug.unit_count for ug in unit_groups]))


def part_2(input_string):
    unit_groups = parse_data(input_string)
    trial_units_groups = deepcopy(unit_groups)
    while not all([unit.type == 'IS' for unit in trial_units_groups]):
        for unit_group in unit_groups:
            if unit_group.type == 'IS':
                unit_group.atk += 1
        trial_units_groups = deepcopy(unit_groups)
        trial_units_groups = combat(trial_units_groups)
    print(sum([ug.unit_count for ug in trial_units_groups]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_24.txt', 'r')
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
