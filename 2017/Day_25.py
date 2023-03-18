import argparse
import re


def part_1(input_string):
    state, steps = re.search(r'Begin in state ([\w]).\nPerform a diagnostic checksum after (\d+) steps.', input_string).groups()
    steps = int(steps)
    slots = [0 for _ in range(steps)]
    cur = 0
    for _ in range(steps):
        if state == 'A':
            if slots[cur] == 0:
                slots[cur] = 1
                cur += 1
                state = 'B'
                continue
            if slots[cur] == 1:
                slots[cur] = 0
                cur += 1
                state = 'F'
                continue
        if state == 'B':
            if slots[cur] == 0:
                # slots[cur] = 1
                cur -= 1
                state = 'B'
                continue
            if slots[cur] == 1:
                # slots[cur] = 1
                cur -= 1
                state = 'C'
                continue
        if state == 'C':
            if slots[cur] == 0:
                slots[cur] = 1
                cur -= 1
                state = 'D'
                continue
            if slots[cur] == 1:
                slots[cur] = 0
                cur += 1
                state = 'C'
                continue
        if state == 'D':
            if slots[cur] == 0:
                slots[cur] = 1
                cur -= 1
                state = 'E'
                continue
            if slots[cur] == 1:
                # slots[cur] = 1
                cur += 1
                state = 'A'
                continue
        if state == 'E':
            if slots[cur] == 0:
                slots[cur] = 1
                cur -= 1
                state = 'F'
                continue
            if slots[cur] == 1:
                slots[cur] = 0
                cur -= 1
                state = 'D'
                continue
        if state == 'F':
            if slots[cur] == 0:
                slots[cur] = 1
                cur += 1
                state = 'A'
                continue
            if slots[cur] == 1:
                slots[cur] = 0
                cur -= 1
                state = 'E'
                continue
    print(slots.count(1))


def part_2(input_string):
    print("Merry Christmas!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_25.txt', 'r')
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
