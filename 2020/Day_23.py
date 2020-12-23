import sys
import getopt

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_23.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_23.py [-h | --help]')
            print('Advent of Code 2020 Day 23')
            sys.exit()

    input_string = '137826495'
    cups = list(map(int, list(input_string)))
    moves = 100

    def crab_cups(cup_labels, move_count):
        min_cup_label, max_cup_label = min(cup_labels), max(cup_labels)
        current_cup_index = 0
        while move_count > 0:
            current_cup = cup_labels[current_cup_index]
            relocating_cups = [cup_labels[(current_cup_index + 1) % len(cup_labels)],
                               cup_labels[(current_cup_index + 2) % len(cup_labels)],
                               cup_labels[(current_cup_index + 3) % len(cup_labels)]]
            for cup in relocating_cups:
                cup_labels.remove(cup)
            destination_cup = current_cup - 1 if current_cup - 1 >= min_cup_label else max_cup_label
            while destination_cup in relocating_cups:
                destination_cup -= 1
                if destination_cup < min_cup_label:
                    destination_cup = max_cup_label
            destination_cup_index = cup_labels.index(destination_cup)
            cup_labels = cup_labels[:destination_cup_index + 1] + \
                         relocating_cups + cup_labels[destination_cup_index + 1:]
            current_cup_index = (cup_labels.index(current_cup) + 1) % len(cup_labels)
            move_count -= 1
        return cup_labels

    cups = crab_cups(cups, moves)
    cups = list(map(str, cups))
    cup_one_index = cups.index('1')
    print(''.join(cups[cup_one_index + 1:] + cups[:cup_one_index]))

    new_cups = list(map(int, list(input_string))) + list(range(10, 1000001))
    new_moves = 10000000
    min_cup_label, max_cup_label = min(new_cups), max(new_cups)
    current_cup = new_cups[0]
    cup_label_dict = {}
    for index in range(len(new_cups)):
        cup_label_dict.update({new_cups[index]: new_cups[(index + 1) % len(new_cups)]})
    while new_moves:
        relocating_cup1 = cup_label_dict[current_cup]
        relocating_cup2 = cup_label_dict[relocating_cup1]
        relocating_cup3 = cup_label_dict[relocating_cup2]
        cup_label_dict.update({current_cup: cup_label_dict[relocating_cup3]})
        dest_cup = current_cup - 1 if current_cup - 1 >= min_cup_label else max_cup_label
        while dest_cup in [relocating_cup1, relocating_cup2, relocating_cup3]:
            dest_cup -= 1
            if dest_cup < min_cup_label:
                dest_cup = max_cup_label
        cup_label_dict.update({relocating_cup3: cup_label_dict[dest_cup]})
        cup_label_dict.update({dest_cup: relocating_cup1})
        current_cup = cup_label_dict[current_cup]
        new_moves -= 1
    print(cup_label_dict[1] * cup_label_dict[cup_label_dict[1]])


if __name__ == "__main__":
    main(sys.argv[1:])