import sys
import getopt
import re

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_14.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_14.py [-h | --help]')
            print('Advent of Code 2020 Day 14')
            sys.exit()

    file_input = open('Input_14.txt', 'r')
    initialization_strings = file_input.readlines()
    file_input.close()
    mask = ''
    memory = {}
    for x in initialization_strings:
        if x.startswith('mask'):
            mask = x.split(' = ')[-1].replace('\r\n', '')
        elif x.startswith('mem'):
            unmasked_address, value = re.findall(r'\d+', x)
            value = bin(int(value)).replace('0b', '')
            while len(value) < len(mask):
                value = '0' + value
            masked_value = list(mask)
            for index, v in enumerate(masked_value):
                if v == 'X':
                    masked_value[index] = value[index]
            memory.update({unmasked_address: int(''.join(masked_value), 2)})
    print(sum(memory.values()))

    new_memory = {}
    for x in initialization_strings:
        if x.startswith('mask'):
            mask = x.split(' = ')[-1].replace('\r\n', '')
        elif x.startswith('mem'):
            unmasked_address, value = re.findall(r'\d+', x)
            value = int(value)
            unmasked_address = bin(int(unmasked_address)).replace('0b', '')
            while len(unmasked_address) < len(mask):
                unmasked_address = '0' + unmasked_address
            masked_address = list(mask)
            for index, v in enumerate(masked_address):
                if v == '1':
                    masked_address[index] = '1'
                elif v == '0':
                    masked_address[index] = unmasked_address[index]
            masked_floated_addresses = [''.join(masked_address)]
            while any('X' in a for a in masked_floated_addresses):
                new_addresses = []
                for address in masked_floated_addresses:
                    new_addresses.append(address.replace('X', '0', 1))
                    new_addresses.append(address.replace('X', '1', 1))
                masked_floated_addresses = new_addresses
            for address in masked_floated_addresses:
                new_memory.update({address: value})
    print(sum(new_memory.values()))


if __name__ == "__main__":
    main(sys.argv[1:])