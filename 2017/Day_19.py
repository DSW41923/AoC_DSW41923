import argparse
import string


def move(x, y, direction):
    if direction == 's':
        return x + 1, y
    if direction == 'w':
        return x, y - 1
    if direction == 'n':
        return x - 1, y
    if direction == 'e':
        return x, y + 1


def part_1(input_string):
    diagram = list(map(list, input_string.split('\n')))
    cur = (0, diagram[0].index('|'))
    collection = []
    direction = 's'
    while True:
        x, y = cur
        cur_path = diagram[x][y]
        if cur_path in string.ascii_uppercase:
            collection.append(cur_path)
            cur = move(x, y, direction)
            continue
        next_x, next_y = move(x, y, direction)
        if cur_path != '+':
            if diagram[next_x][next_y] == ' ':
                break
            cur = (next_x, next_y)
        else:
            if diagram[next_x][next_y] not in [' ', '+']:
                if direction in ['s', 'n'] and diagram[next_x][next_y] == '-':
                    print("!")
                if direction in ['w', 'e'] and diagram[next_x][next_y] == '|':
                    print("!")
                cur = (next_x, next_y)
                continue 

            next_adjacents = []
            if x > 0 and direction != 's':
                next_adjacents.append((x - 1, y, 'n'))
            if y > 0 and direction != 'e':
                next_adjacents.append((x, y - 1, 'w'))
            if x < len(diagram) - 1 and direction != 'n':
                next_adjacents.append((x + 1, y, 's'))
            if y < len(diagram[0]) - 1 and direction != 'w':
                next_adjacents.append((x, y + 1, 'e'))
            for adj in next_adjacents:
                adj_x, adj_y, adj_direction = adj
                if diagram[adj_x][adj_y] not in [' ', '+']:
                    cur = (adj_x, adj_y)
                    direction = adj_direction
                    break
    print(''.join(collection))


def part_2(input_string):
    diagram = list(map(list, input_string.split('\n')))
    cur = (0, diagram[0].index('|'))
    steps = 1
    direction = 's'
    while True:
        x, y = cur
        cur_path = diagram[x][y]
        # if cur_path in string.ascii_uppercase:
        #     collection.append(cur_path)
        #     cur = move(x, y, direction)
        #     continue
        next_x, next_y = move(x, y, direction)
        if cur_path != '+':
            if diagram[next_x][next_y] == ' ':
                break
            cur = (next_x, next_y)
            steps += 1
        else:
            if diagram[next_x][next_y] not in [' ', '+']:
                if direction in ['s', 'n'] and diagram[next_x][next_y] == '-':
                    print("!")
                if direction in ['w', 'e'] and diagram[next_x][next_y] == '|':
                    print("!")
                cur = (next_x, next_y)
                steps += 1
                continue 

            next_adjacents = []
            if x > 0 and direction != 's':
                next_adjacents.append((x - 1, y, 'n'))
            if y > 0 and direction != 'e':
                next_adjacents.append((x, y - 1, 'w'))
            if x < len(diagram) - 1 and direction != 'n':
                next_adjacents.append((x + 1, y, 's'))
            if y < len(diagram[0]) - 1 and direction != 'w':
                next_adjacents.append((x, y + 1, 'e'))
            for adj in next_adjacents:
                adj_x, adj_y, adj_direction = adj
                if diagram[adj_x][adj_y] not in [' ', '+']:
                    cur = (adj_x, adj_y)
                    direction = adj_direction
                    steps += 1
                    break
    print(steps)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_19.txt', 'r')
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
