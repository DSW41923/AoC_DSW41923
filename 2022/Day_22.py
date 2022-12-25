import argparse
import re


def get_next_tile_data(map_data, row, column, facing):
    if facing == 0:
        if column < map_data[row][1][1]:
            return map_data[row][0][column + 1], row, column + 1
        return map_data[row][0][map_data[row][1][0]], row, map_data[row][1][0]

    if facing == 1:
        if row < len(map_data) - 1:
            next_row = (row + 1) % len(map_data)
            if map_data[next_row][1][0] <= column <= map_data[next_row][1][1]:
                return map_data[next_row][0][column], next_row, column
        for i in range(1, len(map_data)):
            if map_data[i][1][0] <= column <= map_data[i][1][1]:
                return map_data[i][0][column], i, column

    if facing == 2:
        if column > map_data[row][1][0]:
            return map_data[row][0][column - 1], row, column - 1
        return map_data[row][0][map_data[row][1][1]], row, map_data[row][1][1]

    if facing == 3:
        if row > 1:
            if map_data[row - 1][1][0] <= column <= map_data[row - 1][1][1]:
                return map_data[row - 1][0][column], row - 1, column
        for i in range(len(map_data) - 1, 0, -1):
            if map_data[i][1][0] <= column <= map_data[i][1][1]:
                return map_data[i][0][column], i, column


def get_next_tile_data_part_2(map_data, row, column, facing):
    current_region = 2 * ((row - 1) // 50) + ((column - 1) // 50)
    # print(current_region)
    if facing == 0:
        if column < map_data[row][1][1]:
            return map_data[row][0][column + 1], row, column + 1, facing
        if current_region == 2:
            new_row = 151 - row
            new_column = map_data[new_row][1][1]
            return map_data[new_row][0][new_column], new_row, new_column, 2
        if current_region == 3:
            new_row = 50
            new_column = row + 50
            return map_data[new_row][0][new_column], new_row, new_column, 3
        if current_region == 5:
            new_row = 151 - row
            new_column = map_data[new_row][1][1]
            return map_data[new_row][0][new_column], new_row, new_column, 2
        if current_region == 6:
            new_row = 150
            new_column = row - 100
            return map_data[new_row][0][new_column], new_row, new_column, 3
        # In region 1, 4 move right directly into region 2, 5
        raise ValueError

    if facing == 1:
        if row < len(map_data) - 1:
            next_row = (row + 1) % len(map_data)
            if map_data[next_row][1][0] <= column <= map_data[next_row][1][1]:
                return map_data[next_row][0][column], next_row, column, facing
        
        if current_region == 2:
            new_row = column - 50
            new_column = map_data[new_row][1][1]
            return map_data[new_row][0][new_column], new_row, new_column, 2
        if current_region == 5:
            new_row = column + 100
            new_column = map_data[new_row][1][1]
            return map_data[new_row][0][new_column], new_row, new_column, 2
        if current_region == 6:
            new_row = 1
            new_column = column + 100
            return map_data[new_row][0][new_column], new_row, new_column, 1
        # In region 1, 3, 4 move down directly into region 3, 5, 6
        raise ValueError

    if facing == 2:
        if column > map_data[row][1][0]:
            return map_data[row][0][column - 1], row, column - 1, facing
        if current_region == 1:
            new_row = 151 - row
            new_column = map_data[new_row][1][0]
            return map_data[new_row][0][new_column], new_row, new_column, 0
        if current_region == 3:
            new_row = 101
            new_column = row - 50
            return map_data[new_row][0][new_column], new_row, new_column, 1
        if current_region == 4:
            new_row = 151 - row
            new_column = map_data[new_row][1][0]
            return map_data[new_row][0][new_column], new_row, new_column, 0
        if current_region == 6:
            new_row = 1
            new_column = row - 100
            return map_data[new_row][0][new_column], new_row, new_column, 1
        # In region 2, 5 move left directly into region 1, 4
        raise ValueError

    if facing == 3:
        if row > 1:
            if map_data[row - 1][1][0] <= column <= map_data[row - 1][1][1]:
                return map_data[row - 1][0][column], row - 1, column, facing
        if current_region == 1:
            new_row = column + 100
            new_column = 1
            return map_data[new_row][0][new_column], new_row, new_column, 0
        if current_region == 2:
            new_row = 200
            new_column = column - 100
            return map_data[new_row][0][new_column], new_row, new_column, 3
        if current_region == 4:
            new_row = column + 50
            new_column = map_data[new_row][1][0]
            return map_data[new_row][0][new_column], new_row, new_column, 0
        # In region 3, 5, 6 move up directly into region 1, 3, 4
        raise ValueError


def part_1(input_string):
    input_data = input_string.split('\n')
    descriptions = re.findall(r'(\d+)([LR])?', input_data[-2])
    map_input = list(map(list, input_data[:-3]))
    max_map_len = max([len(m) for m in map_input])
    map_data = [()]
    for m_data in map_input:
        row = [' ']
        row_min, row_max = max_map_len, 0
        for i, m in enumerate(m_data):
            row.append(m)
            if m != ' ':
                row_min = min(row_min, i + 1)
                row_max = max(row_max, i + 1)
        row.extend([' ' for _ in range(max_map_len - len(m_data))])
        map_data.append((row, (row_min, row_max)))
    pos = {'row': 1, 'column': map_data[1][1][0], 'facing': 0}
    for description in descriptions:
        steps, turn = description
        steps = int(steps)
        for _ in range(steps):
            next_tile_data = get_next_tile_data(map_data, pos['row'], pos['column'], pos['facing'])
            if next_tile_data[0] == '#':
                break

            if next_tile_data[0] == '.':
                pos.update({
                    'row': next_tile_data[1],
                    'column': next_tile_data[2]})

        if turn == 'R':
            pos['facing'] += 1
        elif turn == 'L':
            pos['facing'] -= 1
        pos['facing'] %= 4
    print(1000 * pos['row'] + 4 * pos['column'] + pos['facing'])


def part_2(input_string):
    input_data = input_string.split('\n')
    descriptions = re.findall(r'(\d+)([LR])?', input_data[-2])
    map_input = list(map(list, input_data[:-3]))
    max_map_len = max([len(m) for m in map_input])
    map_data = [()]
    # id of region is (row - 1) // 50 * 2 + (column - 1) // 50
    for mdi, m_data in enumerate(map_input):
        row = [' ']
        row_min, row_max = max_map_len, 0
        for i, m in enumerate(m_data):
            row.append(m)
            if m != ' ':
                row_min = min(row_min, i + 1)
                row_max = max(row_max, i + 1)
        row.extend([' ' for _ in range(max_map_len - len(m_data))])
        map_data.append((row, (row_min, row_max)))
    pos = {'row': 1, 'column': map_data[1][1][0], 'facing': 0}
    for description in descriptions:
        steps, turn = description
        steps = int(steps)
        # print(description, pos)
        for _ in range(steps):
            next_tile_data = get_next_tile_data_part_2(map_data, pos['row'], pos['column'], pos['facing'])
            # print(next_tile_data)
            if next_tile_data[0] == '#':
                break

            if next_tile_data[0] == '.':
                pos.update({
                    'row': next_tile_data[1],
                    'column': next_tile_data[2],
                    'facing': next_tile_data[3]})

        if turn == 'R':
            pos['facing'] += 1
        elif turn == 'L':
            pos['facing'] -= 1
        pos['facing'] %= 4
        # print(pos)
        # print()
    # print(pos)
    print(1000 * pos['row'] + 4 * pos['column'] + pos['facing'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_22.txt', 'r')
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

