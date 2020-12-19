import sys
import getopt
import copy


def split_by_length(text, length):

    return [text[i:i + length] for i in range(0, len(text), length)]

def get_match_for_rule_num(rules, rule_id):
    possible_matches_applying = copy.deepcopy(rules[rule_id])
    while any(s not in ['a', 'b'] for s in ' '.join(possible_matches_applying).split(' ')):
        new_matches = []
        for match in possible_matches_applying:
            applying_rules = match.split(' ')
            if all(r in ['a', 'b'] for r in applying_rules):
                new_matches.append(match)
            else:
                new_matches_applying = ['']
                for rule in applying_rules:
                    new_matches_applying_rule = copy.deepcopy(new_matches_applying)
                    if rule not in ['a', 'b']:
                        rule_results = rules[rule]
                    else:
                        rule_results = [rule]

                    for applying_match in new_matches_applying_rule:
                        for rule_result in rule_results:
                            if applying_match == '':
                                new_matches_applying.append(applying_match + rule_result)
                            else:
                                new_matches_applying.append(applying_match + ' ' + rule_result)
                        new_matches_applying.remove(applying_match)
                new_matches.extend(new_matches_applying)
        possible_matches_applying = new_matches

    return [''.join(match.split(' ')) for match in possible_matches_applying]

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_19.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_19.py [-h | --help]')
            print('Advent of Code 2020 Day 19')
            sys.exit()

    file_input = open('Input_19.txt', 'r')
    rule_strings, messages = file_input.read().split('\n\n')
    file_input.close()
    rules = {}
    for rule_string in rule_strings.split('\n'):
        rule_index, rule_content = rule_string.split(': ')
        if rule_content in ['"a"', '"b"']:
            rules[rule_index] = eval(rule_content)
        else:
            rules[rule_index] = rule_content.split(' | ')

    possible_matches = {'0': get_match_for_rule_num(rules, '0')}
    print(sum(m in possible_matches['0'] for m in messages.split('\n')))

    new_rules = copy.deepcopy(rules)
    new_rules.update({
        '8': ['42', '42 8'],
        '11': ['42 31', '42 11 31']
    })
    possible_matches.update({'42': get_match_for_rule_num(rules, '42'),
                             '31': get_match_for_rule_num(rules, '31')})
    # print(list(set([len(p) for p in possible_matches_applying['42']])))
    # print(list(set([len(p) for p in possible_matches_applying['31']])))
    # print(list(set(possible_matches_applying['42']) & set(possible_matches_applying['31'])))
    message_component_length = 8
    match_count = 0
    for message in messages.split('\n'):
        if len(message) % 8 == 0:
            splitted_message = split_by_length(message, message_component_length)
            components = []
            for component in splitted_message:
                if component in possible_matches['42'] and component in possible_matches['31']:
                    components.append('73')
                elif component in possible_matches['42']:
                    components.append('42')
                elif component in possible_matches['31']:
                    components.append('31')
                else:
                    components.append('0')

            if '73' in components:
                print("Complicated!")
            if '0' in components:
                print("Got You!")

            if 1 <= components.count('31') < components.count('42') and components.count('42') >= 2:
                while components[0] == '42' and components[-1] == '31':
                    components = components[1:-1]
                    if len(components) == 0:
                        break
                if components.count('31') == 0:
                    match_count += 1

        else:
            print("Got You!")
            print(len(message))
    print(match_count)

if __name__ == "__main__":
    main(sys.argv[1:])