import argparse
import re

from copy import deepcopy


def part_1(input_string):
    workflows_data, part_ratings_data = input_string.split('\n\n')
    workflows = {}
    for name, data in re.findall(r"(\w+)\{([\w\d><=:,]+)\}", workflows_data):
        workflows.update({name:[]})
        rules = data.split(',')
        rules[-1] = 'fin:'+rules[-1]
        for rule in rules:
            condition, dest = rule.split(':')
            workflows[name].append((condition.replace('=', '=='), dest))
    accepted_rating = 0
    for x, m, a, s in re.findall(r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}", part_ratings_data):
        x, m, a, s = tuple(map(int, (x, m, a, s)))
        cur = 'in'
        while cur not in ['A', 'R']:
            for rule, dest in workflows[cur]:
                if rule == 'fin':
                    cur = dest
                    continue
                if eval(rule):
                    cur = dest
                    break
        if cur == 'A':
            accepted_rating += sum([x, m, a, s])
    print(accepted_rating)


def part_2(input_string):
    workflows_data = input_string.split('\n\n')[0]
    workflows = {}
    for name, data in re.findall(r"(\w+)\{([\w\d><=:,]+)\}", workflows_data):
        workflows.update({name:[]})
        rules = data.split(',')
        rules[-1] = 'fin:'+rules[-1]
        for rule in rules:
            condition, dest = rule.split(':')
            workflows[name].append((condition, dest))
    all_ratings = {'in': {'x':(1, 4000), 'm':(1, 4000), 'a':(1, 4000), 's':(1, 4000)}}
    accepted_ratings = []
    while not all([cur in ['A', 'R'] for cur in all_ratings]):
        new_ratings = {}
        for cur, cur_rating in all_ratings.items():
            if cur in ['A', 'R']: continue
            for rule, dest in workflows[cur]:
                if rule == 'fin':
                    if dest == 'A':
                        accepted_ratings.append(cur_rating)
                    else:
                        new_ratings.update({dest: cur_rating})
                    continue
                rule_target, rule_criteria, rule_value = rule[0], rule[1], int(rule[2:])
                cur_target_range = cur_rating[rule_target]
                if rule_criteria == '<':
                    if cur_target_range[1] < rule_value:
                        if dest == 'A':
                            accepted_ratings.append(cur_rating)
                        else:
                            new_ratings.update({dest: cur_rating})
                        continue
                    if cur_target_range[0] <= rule_value:
                        passed_rating = deepcopy(cur_rating)
                        passed_rating.update({rule_target: (cur_target_range[0], rule_value-1)})
                        if dest == 'A':
                            accepted_ratings.append(passed_rating)
                        else:
                            new_ratings.update({dest: passed_rating})
                        cur_rating.update({rule_target: (rule_value, cur_target_range[1])})
                elif rule_criteria == '>':
                    if cur_target_range[0] > rule_value:
                        if dest == 'A':
                            accepted_ratings.append(cur_rating)
                        else:
                            new_ratings.update({dest: cur_rating})
                            continue
                    if cur_target_range[1] >= rule_value:
                        passed_rating = deepcopy(cur_rating)
                        passed_rating.update({rule_target: (rule_value+1, cur_target_range[1])})
                        if dest == 'A':
                            accepted_ratings.append(passed_rating)
                        else:
                            new_ratings.update({dest: passed_rating})
                        cur_rating.update({rule_target: (cur_target_range[0], rule_value)})
        all_ratings = new_ratings
    accepted_rating_count = 0
    for accepted_rating in accepted_ratings:
        accepted_rating_count += ((accepted_rating['x'][1]-accepted_rating['x'][0]+1)*(accepted_rating['m'][1]-accepted_rating['m'][0]+1)*(accepted_rating['a'][1]-accepted_rating['a'][0]+1)*(accepted_rating['s'][1]-accepted_rating['s'][0]+1))
    print(accepted_rating_count)


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
