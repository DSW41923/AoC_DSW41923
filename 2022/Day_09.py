import argparse
import re


def move(pos, direction):
    if direction == 'U':
        pos['y'] += 1
        return
    if direction == 'R':
        pos['x'] += 1
        return
    if direction == 'D':
        pos['y'] -= 1
        return
    if direction == 'L':
        pos['x'] -= 1
        return


def is_adjacent(pos_0, pos_1):
    if (pos_0['x'] - pos_1['x'])**2 + (pos_0['y'] - pos_1['y'])**2 <= 2:
        return True
    return False


# pos_1 follows pos_0
def follow(pos_0, pos_1):
 
    if pos_1['x'] < pos_0['x']:
        move(pos_1, 'R')
        if pos_1['y'] == pos_0['y']:
            return

    if pos_1['x'] > pos_0['x']:
        move(pos_1, 'L')
        if pos_1['y'] == pos_0['y']:
            return

    if pos_1['y'] < pos_0['y']:
        move(pos_1, 'U')
        if pos_1['x'] == pos_0['x']:
            return

    if pos_1['y'] > pos_0['y']:
        move(pos_1, 'D')
        if pos_1['x'] == pos_0['x']:
            return

   
def part_1(input_string):
    head_pos = {'x': 0, 'y': 0}
    tail_pos = {'x': 0, 'y': 0}
    tail_pos_history = [(0, 0)]
    for direction, movement in re.findall(r'([URDL]) (\d+)', input_string):
        for _ in range(int(movement)):
            move(head_pos, direction)
            if(not is_adjacent(head_pos, tail_pos)):
                follow(head_pos, tail_pos)
                if (tail_pos['x'], tail_pos['y']) not in tail_pos_history:
                    tail_pos_history.append((tail_pos['x'], tail_pos['y']))
    print(len(tail_pos_history))


def part_2(input_string):
    knots_pos = [{'x': 0, 'y': 0} for _ in range(10)]
    tail_pos_history = [(0, 0)]
    for direction, movement in re.findall(r'([URDL]) (\d+)', input_string):
        for _ in range(int(movement)):
            move(knots_pos[0], direction)
            for i in range(1, 10):
                if(not is_adjacent(knots_pos[i - 1], knots_pos[i])):
                    follow(knots_pos[i - 1], knots_pos[i])
            if (knots_pos[-1]['x'], knots_pos[-1]['y']) not in tail_pos_history:
                tail_pos_history.append((knots_pos[-1]['x'], knots_pos[-1]['y']))
    print(len(tail_pos_history))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2022/Input_09.txt', 'r')
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

