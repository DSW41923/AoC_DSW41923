import sys
import getopt

from operator import itemgetter

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_13.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_13.py [-h | --help]')
            print('Advent of Code 2020 Day 13')
            sys.exit()

    file_input = open('Input_13.txt', 'r')
    input_data = file_input.readlines()
    file_input.close()
    earliest_timestamp = int(input_data[0])
    bus_numbers = []
    scheduling = []
    for x in input_data[1].split(','):
        if x != 'x':
            bus_number = int(x)
            bus_numbers.append(bus_number)
            next_bus_depart = bus_number - (earliest_timestamp % bus_number)
            scheduling.append((bus_number, next_bus_depart))
    fastest_depart = min(scheduling, key=itemgetter(1))
    print(fastest_depart[0] * fastest_depart[1])

    bus_number_with_remainder = []
    for index, x in enumerate(input_data[1].split(',')):
        if x != 'x':
            bus_number = int(x)
            remainder = -index
            while remainder < 0:
                remainder += bus_number
            bus_number_with_remainder.append((bus_number, remainder))

    desire_timestamp = (1, 0)
    for bus_number, remainder in bus_number_with_remainder:
        desire_timestamp_multiply = desire_timestamp[0] * bus_number
        desire_timestamp_remainder = desire_timestamp[1]
        while desire_timestamp_remainder % bus_number != remainder:
            desire_timestamp_remainder += desire_timestamp[0]
        desire_timestamp = (desire_timestamp_multiply, desire_timestamp_remainder)
    print(desire_timestamp[1])


if __name__ == "__main__":
    main(sys.argv[1:])