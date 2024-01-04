import argparse

from collections import Counter


def get_surroundings(x, y):
    return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y), (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]


def get_side(x, y, s):
    if s == 0:
        return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
        pass
    if s == 1:
        return [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
        pass
    if s == 2:
        return [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)]
        pass
    if s == 3:
        return [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]


def part_1(input_string):
    elves = []
    for r, row in enumerate(input_string.split('\n')):
        for c, column in enumerate(list(row)):
            if column == '#':
                elves.append({
                    'pos': (c, r),
                    'next_pos': (c, r)
                    })

    for i in range(10):
        elves_pos = [e['pos'] for e in elves]
        next_pos = Counter()
        # First half round
        for elve in elves:
            surroundings = get_surroundings(*elve['pos'])
            can_propose = False
            for pos in elves_pos:
                if pos in surroundings:
                    can_propose = True
                    break
            if can_propose:
                for s in range(i, i + 4):
                    can_move = True
                    side = get_side(*elve['pos'], s % 4)
                    for pos in elves_pos:
                        if pos in side:
                            can_move = False
                            break
                    if can_move:
                        elve['next_pos'] = side[1]
                        next_pos[elve['next_pos']] += 1
                        break
        # Second half round
        for elve in elves:
            if elve['pos'] == elve['next_pos']:
                continue
            if next_pos[elve['next_pos']] == 1:
                elve['pos'] = elve['next_pos']
                continue
            elve['next_pos'] = elve['pos']

    all_elve_pos = [e['pos'] for e in elves]
    min_x, max_x = min([e[0] for e in all_elve_pos]), max([e[0] for e in all_elve_pos])
    min_y, max_y = min([e[1] for e in all_elve_pos]), max([e[1] for e in all_elve_pos])
    print((max_x - min_x + 1) * (max_y - min_y + 1) - len(elves))

            
def part_2(input_string):
    map_input = input_string.split('\n')
    map_row_max = 3 * len(map_input) + 1
    map_column_max = 3 * len(map_input[0]) + 1
    map_data = [['.' for _ in range(map_column_max)] for _ in range(map_row_max)]
    for r, row in enumerate(map_input):
        for c, column in enumerate(list(row)):
            if column == '#':
                map_data[len(map_input) + r][len(map_input[0]) + c] = '#'
    moving = True
    i = 0
    while moving:
        moving = False
        elves_pos = {}
        next_pos = Counter()
        # First half round
        for r, row in enumerate(map_data):
            for c, column in enumerate(row):
                if column == '#':
                    surroundings = get_surroundings(c, r)
                    if all([map_data[s[1]][s[0]] == '.' for s in surroundings]):
                        continue
                    for d in range(i, i + 4):
                        side = get_side(c, r, d % 4)
                        if all([map_data[s[1]][s[0]] == '.' for s in side]):
                            elves_pos.update({(c, r): side[1]})
                            next_pos[side[1]] += 1
                            break
        # Second half round
        for elve, pos in elves_pos.items():
            if next_pos[pos] == 1:
                map_data[elve[1]][elve[0]] = '.' 
                map_data[pos[1]][pos[0]] = '#' 
                moving = True
        i += 1
    print(i)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2022/Input_23.txt', 'r')
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

