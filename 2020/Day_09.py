import sys
import getopt
import itertools

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_09.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_09.py [-h | --help]')
            print('Advent of Code 2020 Day 09')
            sys.exit()

    file_input = open('inputs/2020/Input_09.txt', 'r')
    number_strings = file_input.readlines()
    file_input.close()
    numbers = []
    for x in number_strings:
        numbers.append(int(x))

    def get_all_valid_numbers(numbers_before):
        all_combination = itertools.combinations(numbers_before, 2)
        return [n[0] + n[1] for n in all_combination]

    invalid_number = 0
    for index, number in enumerate(numbers[25:]):
        valid_numbers = get_all_valid_numbers(numbers[index:index+25])
        if number not in valid_numbers:
            invalid_number = number
            break
    print(invalid_number)

    weakness_numbers = []
    for x in range(len(numbers)):
        total = numbers[x]
        for y in range(x+1, len(numbers)):
            total += numbers[y]
            if total > invalid_number:
                break
            elif total == invalid_number:
                weakness_numbers = numbers[x:y+1]
    encryption_weakness = min(weakness_numbers) + max(weakness_numbers)
    print(encryption_weakness)


if __name__ == "__main__":
    main(sys.argv[1:])