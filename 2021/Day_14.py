import argparse
import re

from collections import Counter


def part_1(input_string):
    template = input_string.split('\n')[0].strip()
    rules = re.findall(r'([A-Z]+) -> ([A-Z])', input_string)
    steps = 10
    while steps > 0:
        next_template = list(template)
        for rule_pair, rule_element in rules:
            for t in range(len(template) - 1):
                if template[t:t+2] == rule_pair:
                    next_template[t] += rule_element
        template = ''.join(next_template)
        steps -= 1

    element_count = Counter(template)
    print(max(element_count.values()) - min(element_count.values()))


def part_2(input_string):
    template = input_string.split('\n')[0].strip()
    rules = re.findall(r'([A-Z]+) -> ([A-Z])', input_string)
    steps = 40
    pairs_count = Counter([template[i:i + 2] for i in range(0, len(template) - 1)])

    while steps > 0:
        new_pairs_count = {}
        for pair, count in pairs_count.items():
            for rule_pair, rule_element in rules:
                if pair == rule_pair:
                    new_pairs_count.update({
                        pair[0] + rule_element: new_pairs_count.get(pair[0] + rule_element, 0) + count,
                        rule_element + pair[1]: new_pairs_count.get(rule_element + pair[1], 0) + count
                    })
        pairs_count = new_pairs_count
        steps -= 1

    element_count = {}
    for pair, count in pairs_count.items():
        element_0, element_1 = tuple(pair)
        if element_0 == element_1:
            element_count.update({
                element_0: element_count.get(element_0, 0) + count * 2
            })
            continue

        element_count.update({
            element_0: element_count.get(element_0, 0) + count,
            element_1: element_count.get(element_1, 0) + count
        })

    element_count[template[0]] += 1
    element_count[template[-1]] += 1

    print((max(element_count.values()) - min(element_count.values())) // 2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2021/Input_14.txt', 'r')
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
