import argparse
import functools
import re

from collections import Counter



def part_1(input_string):

    def compare(x, y):
        x_cards, y_cards = x[0], y[0]
        x_cards_count = Counter(x_cards)
        y_cards_count = Counter(y_cards)
        x_most_cards_count = x_cards_count.most_common(1)[0][1]
        y_most_cards_count = y_cards_count.most_common(1)[0][1]
        if x_most_cards_count != y_most_cards_count:
            return x_most_cards_count - y_most_cards_count
        if x_most_cards_count in [2, 3]: #  and y_most_cards_count in [2, 3]
            x_second_most_cards_count = x_cards_count.most_common(2)[-1][1]
            y_second_most_cards_count = y_cards_count.most_common(2)[-1][1]
            if x_second_most_cards_count != y_second_most_cards_count:
                return x_second_most_cards_count - y_second_most_cards_count
        labels = "23456789TJQKA"
        for x_card, y_card in zip(list(x_cards), list(y_cards)):
            if x_card != y_card:
                return labels.index(x_card) - labels.index(y_card)

    bids = list(map(lambda b: (b[0], int(b[1])),re.findall(r"([AKQJT98765432]{5}) (\d+)", input_string)))
    bids.sort(key=functools.cmp_to_key(compare))
    winnings = 0
    for i, bid in enumerate(bids):
        winnings += (i+1)*int(bid[1])
    print(winnings)


def part_2(input_string):

    def compare(x, y):
        x_cards, y_cards = x[0], y[0]
        x_cards_count = Counter(x_cards)
        x_most_cards = [x[0] for x in x_cards_count.most_common(1)]
        if 'J' in x_most_cards:
            if len(x_most_cards) == 1:
                x_cards_count = Counter(x_cards.replace("J", x_cards_count.most_common(2)[-1][0]))
            else:
                x_cards_count = Counter(x_cards.replace("J", [c for c in x_most_cards if c != 'J'][0]))
        else:
            x_most_cards = x_cards_count.most_common(1)[0][0]
            x_cards_count = Counter(x_cards.replace("J", x_most_cards))
        x_most_cards, x_most_cards_count = x_cards_count.most_common(1)[0]
        x_second_most_cards_count = x_cards_count.most_common(2)[-1][1]

        y_cards_count = Counter(y_cards)
        y_most_cards = [c[0] for c in y_cards_count.most_common(1)]
        if 'J' in y_most_cards:
            if len(y_most_cards) == 1:
                y_cards_count = Counter(y_cards.replace("J", y_cards_count.most_common(2)[-1][0]))
            else:
                y_cards_count = Counter(y_cards.replace("J", [c for c in y_most_cards if c != 'J'][0]))
        else:
            y_most_cards = y_cards_count.most_common(1)[0][0]
            y_cards_count = Counter(y_cards.replace("J", y_most_cards))
        y_most_cards, y_most_cards_count = y_cards_count.most_common(1)[0]
        y_second_most_cards_count = y_cards_count.most_common(2)[-1][1]

        if x_most_cards_count != y_most_cards_count:
            return x_most_cards_count - y_most_cards_count
        if x_most_cards_count in [2, 3]: #  and y_most_cards_count in [2, 3]
            if x_second_most_cards_count != y_second_most_cards_count:
                return x_second_most_cards_count - y_second_most_cards_count
        labels = "J23456789TQKA"
        for x_card, y_card in zip(list(x_cards), list(y_cards)):
            if x_card != y_card:
                return labels.index(x_card) - labels.index(y_card)

    bids = list(map(lambda b: (b[0], int(b[1])),re.findall(r"([AKQJT98765432]{5}) (\d+)", input_string)))
    bids.sort(key=functools.cmp_to_key(compare))
    winnings = 0
    for i, bid in enumerate(bids):
        winnings += (i+1)*int(bid[1])
    print(winnings)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_07.txt', 'r')
    input_string = file_input.read()
    file_input.close()

    if args.part == '1':
        part_1(input_string)
    elif args.part == '2':
        part_2(input_string)
    else:
        part_1(input_string)
        part_2(input_string)


if __name__ == "__main__":
    main()
