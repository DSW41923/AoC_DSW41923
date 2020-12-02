import sys
import getopt

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_02.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_02.py [-h | --help]')
            print('Advent of Code 2020 Day 02')
            sys.exit()

    file_input = open('Input_02.txt', 'r')
    password_entries_input = file_input.readlines()
    password_entries = []
    correct_entries_count = 0
    for x in password_entries_input:
        new_entry = x.split(' ')
        lowest_apearance_time = int(new_entry[0].split('-')[0])
        highest_apearance_time = int(new_entry[0].split('-')[1])
        letter = new_entry[1].replace(':', '')
        actual_appearance_time = list(new_entry[2]).count(letter)
        password_entries.append((lowest_apearance_time, highest_apearance_time, letter, new_entry[2]))
        if lowest_apearance_time <= actual_appearance_time <= highest_apearance_time:
            correct_entries_count += 1
    file_input.close()
    print("{} password entries are valid!".format(correct_entries_count))

    new_valid_entries_count = 0
    for first_pos, sencond_pos, letter, password in password_entries:
        if password[first_pos - 1] == letter and password[sencond_pos - 1] != letter:
            new_valid_entries_count += 1
        elif password[sencond_pos - 1] == letter and password[first_pos - 1] != letter:
            new_valid_entries_count += 1
        else:
            continue
    print("{} password entries are valid!".format(new_valid_entries_count))



if __name__ == "__main__":
    main(sys.argv[1:])