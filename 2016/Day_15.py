import argparse
import re


def get_disc_settings(input_string):
    discs = []
    desired_pos = []
    for i, pos in enumerate(re.findall(
            r'Disc #\d has (\d+) positions; at time=0, it is at position (\d+).', input_string)):
        all_pos, init_pos = pos
        discs.append({'pos': int(init_pos), 'all_pos': int(all_pos)})
        desired_pos.append((int(all_pos) - i - 1) % int(all_pos))

    return discs, desired_pos


def get_pressing_time(discs, desired_pos):
    time = 0
    while tuple([disc['pos'] for disc in discs]) != tuple(desired_pos):
        for disc in discs:
            disc['pos'] = (disc['pos'] + 1) % disc['all_pos']
        time += 1
    return time


def part_1(input_string):
    discs, desired_pos = get_disc_settings(input_string)
    pressing_time = get_pressing_time(discs, desired_pos)
    print(pressing_time)


def part_2(input_string):
    input_string += "Disc #7 has 11 positions; at time=0, it is at position 0."
    discs, desired_pos = get_disc_settings(input_string)
    pressing_time = get_pressing_time(discs, desired_pos)
    print(pressing_time)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2016/Input_15.txt', 'r')
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
