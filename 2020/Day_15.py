import sys
import getopt


def get_next_number(numbers):
    for i in range(2, len(numbers) + 1):
        if numbers[-i] == numbers[-1]:
            return i - 1

    return 0


# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_15.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_15.py [-h | --help]')
            print('Advent of Code 2020 Day 15')
            sys.exit()

    starting_numbers = [7,12,1,0,16,2]
    number_history = starting_numbers
    for _ in range(6, 2020):
        number_history.append(get_next_number(number_history))
    print(number_history[2019])

    number_record = [-1] * 30000000
    for i, n in enumerate(number_history):
        number_record[n] = i + 1
    last_number = number_history[-1]
    for i in range(2020, 30000000):
        if number_record[last_number] == -1:
            next_number = 0
        else:
            next_number = i - number_record[last_number]
        number_record[last_number] = i
        last_number = next_number
    print(last_number)


if __name__ == "__main__":
    main(sys.argv[1:])