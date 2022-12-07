import argparse
import re


def part_1(input_string):
    lines = input_string.split('\n')
    stacks_count = len([l for l in list(lines[8]) if l != ' '])
    crates_stacks = {i+1: [] for i in range(stacks_count)}
    for l in lines[:8]:
        for c, crate in enumerate(l[1::4]):
            if crate != ' ':
                crates_stacks[c+1].insert(0, crate)
    procedure_steps = lines[10:]
    for procedure_step in procedure_steps:
        moving_count, src, des = re.match(r'move (\d+) from (\d+) to (\d+)', procedure_step).groups()
        for _ in range(int(moving_count)):
            crates_stacks[int(des)].append(crates_stacks[int(src)].pop())
    print(''.join([crates_stacks[i].pop() if crates_stacks[i] else '' for i in range(1, 10)]))


def part_2(input_string):
    lines = input_string.split('\n')
    stacks_count = len([l for l in list(lines[8]) if l != ' '])
    crates_stacks = {i+1: [] for i in range(stacks_count)}
    for l in lines[:8]:
        for c, crate in enumerate(l[1::4]):
            if crate != ' ':
                crates_stacks[c+1].insert(0, crate)
    procedure_steps = lines[10:]
    for procedure_step in procedure_steps:
        moving_count, src, des = re.findall(r'move (\d+) from (\d+) to (\d+)', procedure_step)[0]
        crates_stacks[int(des)].extend(crates_stacks[int(src)][-int(moving_count):])
        crates_stacks[int(src)] = crates_stacks[int(src)][:-int(moving_count)]
    print(''.join([crates_stacks[i].pop() if crates_stacks[i] else '' for i in range(1, 10)]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_05.txt', 'r')
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
