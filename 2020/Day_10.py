import sys
import getopt

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_10.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_10.py [-h | --help]')
            print('Advent of Code 2020 Day 10')
            sys.exit()

    file_input = open('Input_10.txt', 'r')
    adapter_strings = file_input.readlines()
    file_input.close()
    adapters = []
    for x in adapter_strings:
        adapters.append(int(x))
    adapters.extend([0, max(adapters) + 3])
    adapters = sorted(adapters)
    voltage_difference = [0] * 3
    for i in range(1, len(adapters)):
        voltage_difference[adapters[i] - adapters[i - 1] - 1] += 1
    print(voltage_difference[0] * voltage_difference[2])

    possible_arrangements = 1
    must_adapters = [0]
    for i in range(1, len(adapters)):
        if adapters[i] - adapters[i - 1] == 3:
            must_adapters.extend([adapters[i], adapters[i - 1]])
    must_adapters = sorted(list(set(must_adapters)))
    for j in range(1, len(must_adapters)):
        optional_adapters_count = sum([must_adapters[j - 1] < v < must_adapters[j] for v in adapters])
        if must_adapters[j] - must_adapters[j - 1] > 3:
            possible_arrangements *= (2 ** optional_adapters_count - 1)
        else:
            possible_arrangements *= 2 ** optional_adapters_count
    print(possible_arrangements)


if __name__ == "__main__":
    main(sys.argv[1:])