import sys
import getopt
import string

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_06.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_06.py [-h | --help]')
            print('Advent of Code 2020 Day 06')
            sys.exit()

    file_input = open('Input_06.txt', 'r')
    raw_data = file_input.read().split('\r\n\r\n')
    file_input.close()
    form_data = []
    total_yes_count = 0
    for data in raw_data:
        answer_data = data.replace('\r\n', ' ')
        yes_count = 0
        for letter in string.ascii_lowercase:
            if letter in answer_data:
                yes_count += 1
        form_data.append(answer_data)
        total_yes_count += yes_count
    print(total_yes_count)

    total_everyone_yes_count = 0
    for data in form_data:
        answer_data = data.split(' ')
        everyone_yes_count = 0
        for letter in answer_data[0]:
            yes_count = 1
            for other_answer in answer_data[1:]:
                if letter in other_answer:
                    yes_count += 1
            if yes_count == len(answer_data):
                everyone_yes_count += 1
        total_everyone_yes_count += everyone_yes_count
    print(total_everyone_yes_count)


if __name__ == "__main__":
    main(sys.argv[1:])