import sys
import getopt

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_03.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_03.py [-h | --help]')
            print('Advent of Code 2020 Day 03')
            sys.exit()

    file_input = open('Input_03.txt', 'r')
    map_strings = list(map(lambda s: s.replace('\n', ''), file_input.readlines()))
    file_input.close()
    def count_tree(map_data, right, down):
        map_x_maximum = len(map_data[0])
        tree_encounter_count = 0
        x, y = 0, 0
        while y < len(map_data):
            if map_data[y][x] == '#':
                tree_encounter_count += 1
            x = (x + right) % map_x_maximum
            y += down
        return tree_encounter_count
    first_result = count_tree(map_strings, 3, 1)
    print(first_result)
    second_result = first_result
    print(second_result * count_tree(map_strings, 1, 1)
          * count_tree(map_strings, 5, 1) * count_tree(map_strings, 7, 1)
          * count_tree(map_strings, 1, 2))


if __name__ == "__main__":
    main(sys.argv[1:])