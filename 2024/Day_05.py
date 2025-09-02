import argparse
import re


def parse_input(input_string):
    rules_string, updates_string = input_string.split('\n\n')
    rules = {}
    for page0, page1 in re.findall(r'(\d+)\|(\d+)', rules_string):
        if page0 not in rules:
            rules[page0] = [page1]
        else:
            rules[page0] += [page1]
    return rules, list(map(lambda u: u.split(','), updates_string.split('\n')))


def is_correct_update(rules, update_data):
    for i in range(1,len(update_data)):
        for prev in update_data[:i]:
            if prev in rules[update_data[i]]:
                return False
    return True


def part_1(input_string):
    rules, updates = parse_input(input_string)
    result = 0
    for u in updates:
        if is_correct_update(rules, u):
            result += int(u[len(u)//2])
    print(result)


def part_2(input_string):
    rules, updates = parse_input(input_string)
    incorrect_updates = []
    for u in updates:
        if not is_correct_update(rules, u):
            incorrect_updates.append(u)
    result = 0
    for u in incorrect_updates:
        corrected_u = [u[0]]
        for i in range(1,len(u)):
            for j in range(len(corrected_u)):
                if corrected_u[j] in rules[u[i]]:
                    corrected_u = corrected_u[:j] + [u[i]] + corrected_u[j:]
                    break
            if u[i] not in corrected_u:
                corrected_u.append(u[i])
        result += int(corrected_u[len(corrected_u)//2])
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_05.txt', 'r')
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
