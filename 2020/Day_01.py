import sys
import getopt

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_01.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_01.py [-h | --help]')
            print('Advent of Code 2020 Day 01')
            sys.exit()

    file_input = open('Input_01.txt', 'r')
    number_strings = file_input.readlines()
    numbers = []
    for x in number_strings:
        new_number = int(x)
        numbers.append(new_number)
        if (2020 - new_number) in numbers:
            print(new_number * (2020 - new_number))
    file_input.close()

    for a in numbers:
        first_remainder = 2020 - a
        for b in numbers:
            if b != a:
                c = first_remainder - b
                if c != b and c in numbers:
                    print(a * b * c)
                    sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])