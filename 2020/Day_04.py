import sys
import getopt
import re

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_04.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_04.py [-h | --help]')
            print('Advent of Code 2020 Day 04')
            sys.exit()

    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    file_input = open('Input_04.txt', 'r')
    raw_data = file_input.read().split('\n\n')
    passport_data = []
    valid_passport_count = 0
    for data in raw_data:
        data = data.replace('\n', ' ').split(' ')
        new_passport_data = {}
        for key_value_pairs in data:
            field, value = key_value_pairs.split(':')
            new_passport_data.update({field: value})
        passport_data.append(new_passport_data)
        if all([f in new_passport_data.keys() for f in required_fields]):
            valid_passport_count += 1
    print(valid_passport_count)

    stricter_valid_passport_count = 0
    for passport in passport_data:
        if all([f in passport.keys() for f in required_fields]):
            try:
                byr = int(passport['byr'])
                iyr = int(passport['iyr'])
                eyr = int(passport['eyr'])
            except ValueError:
                continue

            if not ((1920 <= byr <= 2002) and (2010 <= iyr <= 2020) and (2020 <= eyr <= 2030)):
                continue

            try:
                hgt = passport['hgt']
                if hgt.endswith('cm'):
                    hgt_cm = int(hgt.replace('cm', ''))
                    if not (150 <= hgt_cm <= 193):
                        raise ValueError
                elif hgt.endswith('in'):
                    hgt_in = int(hgt.replace('in', ''))
                    if not (59 <= hgt_in <= 76):
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                continue

            if not re.search(r'#[0-9abcdef]{6}', passport['hcl']):
                continue

            if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                continue

            if len(passport['pid']) != 9:
                continue

            stricter_valid_passport_count += 1
    print(stricter_valid_passport_count)
if __name__ == "__main__":
    main(sys.argv[1:])