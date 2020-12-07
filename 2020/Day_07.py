import sys
import getopt
import re

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_07.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_07.py [-h | --help]')
            print('Advent of Code 2020 Day 07')
            sys.exit()

    file_input = open('Input_07.txt', 'r')
    raw_data = file_input.readlines()
    file_input.close()
    rules = {}
    for rule in raw_data:
        rule = rule.split(' contain ')
        outer_bag_color = re.search(r'([\w ]+) bags', rule[0]).group(1)
        rules.update({
            outer_bag_color: {}
        })
        for inner_bag_amount, inner_bags_color in re.findall(r'(\d) ([\w ]+) bag', rule[1]):
            rules[outer_bag_color].update({
                inner_bags_color: int(inner_bag_amount)
            })
    target_bag_colors = ['shiny gold']
    count = 0
    for color in target_bag_colors:
        for bag_color in rules.keys():
            if bag_color not in target_bag_colors and color in rules[bag_color].keys():
                count += 1
                if bag_color not in target_bag_colors:
                    target_bag_colors.append(bag_color)
    print(count)
    containing_bags = ['shiny gold']
    for color in containing_bags:
        for bag_color in rules[color].keys():
            for _ in range(rules[color][bag_color]):
                containing_bags.append(bag_color)
    print(len(containing_bags) - 1)
    # Maybe this should be done by tree~


if __name__ == "__main__":
    main(sys.argv[1:])