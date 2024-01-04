import sys
import getopt
import re

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_16.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_16.py [-h | --help]')
            print('Advent of Code 2020 Day 16')
            sys.exit()

    file_input = open('inputs/2020/Input_16.txt', 'r')
    input_strings = file_input.read().split('\n\n')
    file_input.close()
    field_rules_input, my_ticket_input, nearby_tickets_input = input_strings
    field_rules = {}
    for field_name, range_1, range_2 in re.findall(r'([\w ]+): ([\d-]+) or ([\d-]+)', field_rules_input):
        range_1_start, range_1_end = tuple(map(int, range_1.split('-')))
        range_2_start, range_2_end = tuple(map(int, range_2.split('-')))
        value_range = list(range(range_1_start, range_1_end + 1)) + list(range(range_2_start, range_2_end + 1))
        field_rules.update({field_name: value_range})

    nearby_tickets = []
    ticket_scanning_error_rate = 0
    for ticket_text in re.findall(r'[\d,]+', nearby_tickets_input):
        ticket_fields = tuple(map(int, ticket_text.split(',')))
        nearby_tickets.append(ticket_fields)
        for field in ticket_fields:
            if all(field not in r for r in field_rules.values()):
                ticket_scanning_error_rate += field
                nearby_tickets.remove(ticket_fields)
    print(ticket_scanning_error_rate)

    possible_field_names = []
    for i in range(len(field_rules.keys())):
        possible_field_names.append([])
        field_value_aggregate = [t[i] for t in nearby_tickets]
        for field_name, valid_field_values in field_rules.items():
            if all(v in valid_field_values for v in field_value_aggregate):
                possible_field_names[i].append(field_name)

    actual_field_names = [''] * len(field_rules.keys())
    while any(len(n) > 0 for n in possible_field_names):
        field_index = 0
        for index, possible_field_name in enumerate(possible_field_names):
            if len(possible_field_name) == 1:
                actual_field_names[index] = possible_field_name[0]
                field_index = index
                break

        for possible_field_name in possible_field_names:
            if actual_field_names[field_index] in possible_field_name:
                possible_field_name.remove(actual_field_names[field_index])

    print(actual_field_names)
    result_value = 1
    my_ticket_fields = tuple(map(int, re.search(r'[\d,]+', my_ticket_input).group(0).split(',')))
    for field_name, value in zip(actual_field_names, my_ticket_fields):
        if field_name.startswith('departure'):
            result_value *= value
    print(result_value)



if __name__ == "__main__":
    main(sys.argv[1:])