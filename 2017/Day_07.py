import argparse
import re

from collections import Counter


def part_1(input_string):
    holdees = []
    root_candidates = []
    for line in input_string.split('\n'):
        if '->' in line:
            holder_info, holdee_info = line.split('->')
            holder = re.findall(r'[a-z]+', holder_info)[0]
            holdee = re.findall(r'[a-z]+', holdee_info)
            holdees.extend(holdee)
            if holder not in holdees:
                root_candidates.append(holder)
    for candidate in root_candidates:
        if candidate not in holdees:
            print(candidate)


def part_2(input_string):
    programs = {}
    for line in input_string.split('\n'):
        if '->' not in line:
            holder, weight = re.findall(r'([a-z]+) \((\d+)\)', line)[0]
            programs.update({
                holder: {
                    'weight': int(weight),
                    'holdee': [],
                    'total_weight': int(weight)
                }
            })
            continue
        holder_info, holdee_info = line.split('->')
        holder, weight = re.findall(r'([a-z]+) \((\d+)\)', holder_info)[0]
        holdee = re.findall(r'[a-z]+', holdee_info)
        programs.update({
            holder: {
                'weight': int(weight),
                'holdee': holdee,
                'total_weight': 0
            }
        })

    while True:
        for program in programs:
            if len(programs[program]['holdee']) > 0 and programs[program]['total_weight'] == 0:
                holdee_weights = [programs[p]['total_weight'] for p in programs[program]['holdee']]
                if all(w != 0 for w in holdee_weights):
                    if len(set(holdee_weights)) == 1:
                        programs[program].update({'total_weight': sum(holdee_weights) + programs[program]['weight']})
                    else:
                        counter = Counter(holdee_weights).most_common()
                        for holdee in programs[program]['holdee']:
                            if programs[holdee]['total_weight'] == counter[-1][0]:
                                print(programs[holdee]['weight'] + (counter[0][0] - counter[-1][0]))
                                return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_07.txt', 'r')
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
