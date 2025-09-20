import argparse

from copy import deepcopy


def get_adjacents(x, y):
    return [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]


def manhatton_distance(p0, p1):
    return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])


class Unit(object):

    def __init__(self, type, pos):
        self.type = type
        self.pos = pos
        self.atk = 3
        self.hp = 200

    def adjacents(self):
        x, y = self.pos
        return get_adjacents(x, y)

    def __str__(self):
        return str(self.type) + " " + str(self.pos) + " " + str((self.atk, self.hp))


def parse_data(input_string):
    units = []
    area_map = list(map(list, input_string.split('\n')))
    x_range = len(area_map)
    y_range = len(area_map[0])
    for x in range(x_range):
        for y in range(y_range):
            if area_map[x][y] == 'E':
                units.append(Unit('Elf', (x, y)))
                area_map[x][y] = '.'
            if area_map[x][y] == 'G':
                units.append(Unit('Goblin', (x, y)))
                area_map[x][y] = '.'
    return units, area_map


def print_out(turn, units, area_map):
    x_range = len(area_map)
    y_range = len(area_map[0])
    print(turn)
    e_pos = [(u.pos[0], u.pos[1]) for u in units if u.type == 'Elf']
    g_pos = [(u.pos[0], u.pos[1]) for u in units if u.type == 'Goblin']
    for x in range(x_range):
        for y in range(y_range):
            if (x, y) in e_pos:
                print('E', end='')
            elif (x, y) in g_pos:
                print('G', end='')
            else:
                print(area_map[x][y],end='')
        print()


def combat(units, area_map, part=1):
    turn = 0
    while not (all([unit.type == 'Elf' for unit in units]) or all([unit.type == 'Goblin' for unit in units])):
        for unit in units:

            if all([u.type == 'Elf' for u in units if u.hp > 0]) or all([u.type == 'Goblin' for u in units if u.hp > 0]):
                if part == 2:
                    return turn*sum([u.hp for u in units if u.hp > 0]), len([u for u in units if u.type == 'Elf' and u.hp > 0])
                return turn*sum([u.hp for u in units if u.hp > 0])

            if unit.hp <= 0:
                continue

            all_units_pos = []
            enemy_units = []
            in_range_attack_targets = []
            for u in units:
                if u.hp <= 0:
                    continue
                all_units_pos.append(u.pos)
                if u.type != unit.type:
                    enemy_units.append(u)
                    if manhatton_distance(u.pos, unit.pos) == 1:
                        in_range_attack_targets.append(u)

            # No enemy in range -> move before attack
            if not in_range_attack_targets:
                in_range_targets = []
                for enemy_unit in enemy_units:
                    for x, y in enemy_unit.adjacents():
                        if (x, y) not in all_units_pos and area_map[x][y] == '.':
                            in_range_targets.append((x, y))

                fronts = [(0, (unit.pos[0], unit.pos[1]), None)]
                visited = {
                    (unit.pos[0], unit.pos[1]): (0, None)
                }
                reaching_target = None
                while fronts and not reaching_target:
                    step, front, pre = fronts.pop(0)
                    next_fronts = get_adjacents(*front)
                    for x, y in next_fronts:
                        new_step = step + 1
                        new_pre = pre
                        if new_pre is None:
                            if x == front[0]:
                                if y < front[1]:
                                    new_pre = 1
                                if y > front[1]:
                                    new_pre = 2
                            if y == front[1]:
                                if x < front[0]:
                                    new_pre = 0
                                if x > front[0]:
                                    new_pre = 3
                        if (x, y) not in all_units_pos and area_map[x][y] == '.':
                            if (x, y) in visited:
                                if new_step < visited[(x, y)][0]:
                                    visited[(x, y)] = (new_step, new_pre)
                                elif new_step == visited[(x, y)][0] and new_pre < visited[(x, y)][1]:
                                    visited[(x, y)] = (new_step, new_pre)
                            else:
                                visited.update({
                                    (x, y): (new_step, new_pre)
                                })
                                fronts.append((new_step, (x, y), new_pre))
                    fronts.sort(key=lambda f:f[0])

                    for x, y in in_range_targets:
                        if (x, y) in visited:
                            if not reaching_target:
                                if not fronts:
                                    reaching_target = ((x, y), visited[(x, y)])
                                elif visited[(x, y)][0] < fronts[0][0]:
                                    reaching_target = ((x, y), visited[(x, y)])
                            else:
                                if visited[(x, y)][0] < reaching_target[1][0]:
                                    reaching_target = ((x, y), visited[(x, y)])
                                elif visited[(x, y)][0] == reaching_target[1][0]:
                                    if (x*100+y) < (reaching_target[0][0]*100+reaching_target[0][1]):
                                        reaching_target = ((x, y), visited[(x, y)])
                if reaching_target:
                    unit.pos = unit.adjacents()[reaching_target[1][1]]
                    in_range_attack_targets = []
                    for enemy_unit in enemy_units:
                        if manhatton_distance(enemy_unit.pos, unit.pos) == 1:
                            in_range_attack_targets.append(enemy_unit)

            # attack
            if in_range_attack_targets:
                in_range_attack_targets.sort(key=lambda u: u.hp*10000+u.pos[0]*100+u.pos[1])
                target = in_range_attack_targets[0]
                target.hp -= unit.atk

        new_units = []
        for unit in units:
            if unit.hp > 0:
                new_units.append(unit)
        units = new_units
        units.sort(key=lambda u: u.pos[0]*100+u.pos[1])
        turn += 1
    
    if part == 2:
        return turn*sum([u.hp for u in units if u.hp > 0]), len([u for u in units if u.type == 'Elf' and u.hp > 0])
    return turn*sum([unit.hp for unit in units if unit.hp > 0])


def part_1(input_string):
    units, area_map = parse_data(input_string)
    print(combat(units, area_map))


def part_2(input_string):
    units, area_map = parse_data(input_string)
    elves_count = len([u for u in units if u.type == 'Elf' and u.hp > 0])
    result, trial_elves_count = 0, 0
    while trial_elves_count != elves_count:
        for unit in units:
            if unit.type == 'Elf':
                unit.atk += 1
        trial_units = deepcopy(units)
        result, trial_elves_count = combat(trial_units, area_map, part=2)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_15.txt', 'r')
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
