import argparse


def traverse_rooms(regex, pos, steps, rooms):
    fork_pos = []
    for r in regex:
        if r == '^':
            continue
        elif r == 'N':
            pos += 1j
            steps += 1
            if pos not in rooms:
                rooms.update({pos: steps})
            else:
                if steps < rooms[pos]:
                    rooms.update({pos: steps})
        elif r == 'E':
            pos += 1
            steps += 1
            if pos not in rooms:
                rooms.update({pos: steps})
            else:
                if steps < rooms[pos]:
                    rooms.update({pos: steps})
        elif r == 'W':
            pos -= 1
            steps += 1
            if pos not in rooms:
                rooms.update({pos: steps})
            else:
                if steps < rooms[pos]:
                    rooms.update({pos: steps})
        elif r == 'S':
            pos -= 1j
            steps += 1
            if pos not in rooms:
                rooms.update({pos: steps})
            else:
                if steps < rooms[pos]:
                    rooms.update({pos: steps})
        elif r == '(':
            fork_pos.append((pos, steps))
        elif r == '|':
            pos, steps = fork_pos[-1]
        elif r == ')':
            fork_pos.pop()
        elif r == '$':
            break


def part_1(input_string):
    rooms = {}
    pos = 0+0j
    rooms.update({pos: 0})
    traverse_rooms(input_string, pos, 0, rooms)
    print(max(rooms.values()))


def part_2(input_string):
    rooms = {}
    pos = 0+0j
    rooms.update({pos: 0})
    traverse_rooms(input_string, pos, 0, rooms)
    print(len([v for v in rooms.values() if v >= 1000]))



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_20.txt', 'r')
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
