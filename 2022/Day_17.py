import argparse


def settle_units(settled_units, unit_count, unit_heights, chamber, jet_index, jet_string):
    while settled_units < unit_count:
        new_unit = list(unit_heights.keys())[settled_units % 5]
        initial_height = len(chamber) + 3
        if new_unit == '-':
            new_unit_bounds = {
                    'l': [(initial_height, 2)],
                    'r': [(initial_height, 7)],
                    'b': [(i, c) for i in range(initial_height - 1, initial_height) for c in range(3, 7)]}
        if new_unit == '+':
            new_unit_bounds = {
                    'l': [
                        (initial_height, 3),
                        (initial_height + 1, 2),
                        (initial_height + 2, 3)],
                    'r': [
                        (initial_height, 5),
                        (initial_height + 1, 6),
                        (initial_height + 2, 5)],
                    'b': [
                        (initial_height, 3),
                        (initial_height - 1, 4),
                        (initial_height, 5)]
                    }
        if new_unit == 'J':
            new_unit_bounds = {
                    'l': [
                        (initial_height, 2),
                        (initial_height + 1, 4),
                        (initial_height + 2, 4)],
                    'r': [(i, 6) for i in range(initial_height, initial_height + 3)],
                    'b': [(initial_height - 1, i) for i in range(3, 6)],
                    }
        if new_unit == 'I':
            new_unit_bounds = {
                    'l': [(i, 2) for i in range(initial_height, initial_height + 4)],
                    'r': [(i, 4) for i in range(initial_height, initial_height + 4)],
                    'b': [(initial_height - 1, 3)]
                    }
        if new_unit == 'o':
            new_unit_bounds = {
                    'l': [
                        (initial_height, 2),
                        (initial_height + 1, 2)],
                    'r': [
                        (initial_height, 5),
                        (initial_height + 1, 5)],
                    'b': [
                        (initial_height - 1, 3),
                        (initial_height - 1, 4)]
                    }
        jet_index = settle_next_unit(unit_heights[new_unit], new_unit_bounds, jet_string, jet_index, chamber)
        # print('\n'.join(list(map(lambda s: ''.join(s), reversed(chamber)))))
        settled_units += 1
    return jet_index

def settle_next_unit(unit_height, unit_bounds, jet_string, jet_index, chamber):
    while True:
        movement = jet_string[jet_index]
        if movement == '>':
            moving = True
            for c_y, c_x in unit_bounds['r']:
                if not 0 < c_x < 8:
                    moving = False
                    break
                if c_y < len(chamber):
                    if chamber[c_y][c_x] != '.':
                        moving = False
                        break
            if moving:
                unit_bounds.update({
                    'l': [(y, x + 1) for y, x in unit_bounds['l']],
                    'r': [(y, x + 1) for y, x in unit_bounds['r']],
                    'b': [(y, x + 1) for y, x in unit_bounds['b']]
                })
        elif movement == '<':
            moving = True
            for c_y, c_x in unit_bounds['l']:
                if not 0 < c_x < 8:
                    moving = False
                    break
                if c_y < len(chamber):
                    if chamber[c_y][c_x] != '.':
                        moving = False
                        break
            if moving:
                 unit_bounds.update({
                    'l': [(y, x - 1) for y, x in unit_bounds['l']],
                    'r': [(y, x - 1) for y, x in unit_bounds['r']],
                    'b': [(y, x - 1) for y, x in unit_bounds['b']]
                })
        jet_index += 1
        jet_index %= len(jet_string)

        falling = True
        for c_y, c_x in unit_bounds['b']:
            if c_y < len(chamber):
                if chamber[c_y][c_x] != '.':
                    falling = False
                    break
        if falling:
            unit_bounds.update({
                'l': [(y - 1, x) for y, x in unit_bounds['l']],
                'r': [(y - 1, x) for y, x in unit_bounds['r']],
                'b': [(y - 1, x) for y, x in unit_bounds['b']]
            })
            continue
        break
    new_chamber_rows = [
            '|' + ''.join(['#' if left_bound[1] < c < right_bound[1] else '.' for c in range(1, 8)]) + '|' \
                for left_bound, right_bound in zip(unit_bounds['l'], unit_bounds['r'])]
    y_base = min([y for y, x in unit_bounds['b']]) + 1
    for b in range(unit_height):
        if y_base + b >= len(chamber):
            chamber.append(list(new_chamber_rows[b]))
        else:
            for i, (c, nc) in enumerate(zip(chamber[y_base + b], new_chamber_rows[b])):
                if c == nc:
                    continue
                if '#' in [c, nc]:
                    chamber[y_base + b][i] = '#'
                if c == nc == '#':
                    raise
    return jet_index


def part_1(input_string):
    input_string = input_string[:-1]
    unit_heights = {
            '-': 1,
            '+': 3,
            'J': 3,
            'I': 4,
            'o': 2}
    chamber = [list('+-------+')]
    settle_units(0, 2022, unit_heights, chamber, 0, input_string)
    print(len(chamber) - 1)


def part_2(input_string):
    input_string = input_string[:-1]
    unit_heights = {
            '-': 1,
            '+': 3,
            'J': 3,
            'I': 4,
            'o': 2}
    settled_units = 0
    chamber_memo = {}
    chamber_history = []
    chamber = [list('+-------+')]
    jet_index = 0
    loop_context = {}
    # First identifying loops
    while True:
        new_unit = list(unit_heights.keys())[settled_units % 5]
        initial_height = len(chamber) + 3
        if new_unit == '-':
            new_unit_bounds = {
                    'l': [(initial_height, 2)],
                    'r': [(initial_height, 7)],
                    'b': [(i, c) for i in range(initial_height - 1, initial_height) for c in range(3, 7)]}
        if new_unit == '+':
            new_unit_bounds = {
                    'l': [
                        (initial_height, 3),
                        (initial_height + 1, 2),
                        (initial_height + 2, 3)],
                    'r': [
                        (initial_height, 5),
                        (initial_height + 1, 6),
                        (initial_height + 2, 5)],
                    'b': [
                        (initial_height, 3),
                        (initial_height - 1, 4),
                        (initial_height, 5)]
                    }
        if new_unit == 'J':
            new_unit_bounds = {
                    'l': [
                        (initial_height, 2),
                        (initial_height + 1, 4),
                        (initial_height + 2, 4)],
                    'r': [(i, 6) for i in range(initial_height, initial_height + 3)],
                    'b': [(initial_height - 1, i) for i in range(3, 6)],
                    }
        if new_unit == 'I':
            new_unit_bounds = {
                    'l': [(i, 2) for i in range(initial_height, initial_height + 4)],
                    'r': [(i, 4) for i in range(initial_height, initial_height + 4)],
                    'b': [(initial_height - 1, 3)]
                    }
        if new_unit == 'o':
            new_unit_bounds = {
                    'l': [
                        (initial_height, 2),
                        (initial_height + 1, 2)],
                    'r': [
                        (initial_height, 5),
                        (initial_height + 1, 5)],
                    'b': [
                        (initial_height - 1, 3),
                        (initial_height - 1, 4)]
                    }
        jet_index = settle_next_unit(unit_heights[new_unit], new_unit_bounds, input_string, jet_index, chamber)
        settled_units += 1
        highest = []
        for i in range(1, 8):
            for j in range(len(chamber) - 1, -1, -1):
                if chamber[j][i] != '.':
                    highest.append(j)
                    break
        if (jet_index, new_unit, tuple(highest)) in chamber_memo:
            loop_context.update({
                'units': settled_units - chamber_memo[(jet_index, new_unit, tuple(highest))][0],
                'height': len(chamber) + len(chamber_history) - 1 - chamber_memo[(jet_index, new_unit, tuple(highest))][1],
                'key': (jet_index, new_unit, tuple(highest)),
                'value': (settled_units, len(chamber) + len(chamber_history) - 1)
                })
            break
        else:
            chamber_memo.update({
                (jet_index, new_unit, tuple(highest)): (settled_units, len(chamber) + len(chamber_history) - 1)
                })
        if list('|#######|') in chamber:
            blocked_row_index = chamber.index(list('|#######|'))
            for c in chamber[1:blocked_row_index + 1]:
                c_int = int(''.join(['1' if c_char == '#' else '0' for c_char in c[1:8]]), 2)
                chamber_history.append(c_int)
            chamber = [chamber[0]] + chamber[blocked_row_index + 1:]

    # Computing rest units to be settled
    target_settled_units = 1000000000000
    preloop_units = chamber_memo[loop_context['key']][0]
    preloop_height = chamber_memo[loop_context['key']][1]
    precomputed_height = preloop_height + ((target_settled_units - preloop_units) // loop_context['units']) * loop_context['height'] - len(chamber) + 1
    settled_units = target_settled_units - (target_settled_units - preloop_units) % loop_context['units']
    settle_units(settled_units, target_settled_units, unit_heights, chamber, jet_index, input_string)
    print(precomputed_height + len(chamber) - 1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2022/Input_17.txt', 'r')
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

