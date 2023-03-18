import argparse
import re


def part_1(input_string):
    programs = {}
    for program, containee in re.findall(r'(\d+) <-> ([\d, ]+)', input_string):
        programs.update({
            program: {
                'contains': containee.split(', ')
            }
        })

    is_contain_zero = ['0']
    for p in is_contain_zero:
        for program in programs:
            if p in programs[program]['contains']:
                if program not in is_contain_zero:
                    is_contain_zero.append(program)
    print(len(is_contain_zero))
        


def part_2(input_string):
    programs = {}
    for program, containee in re.findall(r'(\d+) <-> ([\d, ]+)', input_string):
        programs.update({
            program: {
                'contains': containee.split(', ')
            }
        })

    groups = 0
    while any('group' not in programs[p] for p in programs):
        is_contain = []
        for program in programs:
            if 'group' not in programs[program]:
                is_contain.append(program)
                break
        for p in is_contain:
            for program in programs:
                if p in programs[program]['contains'] or program == p:
                    programs[program].update({'group': groups})
                    if program not in is_contain:
                        is_contain.append(program)
        groups += 1
    print(groups)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_12.txt', 'r')
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
