import argparse
from operator import itemgetter


def part_1(messages):
    msg_len = min(list(map(len, messages)))
    correct_message = ''
    for i in range(msg_len):
        ith_character = [m[i] for m in messages]
        char_count = {}
        for c in ith_character:
            if char_count.get(c):
                char_count[c] += 1
            else:
                char_count[c] = 1
        top_character = max(char_count.items(), key=itemgetter(1))[0]
        correct_message += top_character
    print(correct_message)


def part_2(messages):
    msg_len = min(list(map(len, messages)))
    correct_message = ''
    for i in range(msg_len):
        ith_character = [m[i] for m in messages]
        char_count = {}
        for c in ith_character:
            if char_count.get(c):
                char_count[c] += 1
            else:
                char_count[c] = 1
        top_character = min(char_count.items(), key=itemgetter(1))[0]
        correct_message += top_character
    print(correct_message)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_06.txt', 'r')
    messages = file_input.readlines()
    file_input.close()

    if args.part == '1':
        part_1(messages)
    elif args.part == '2':
        part_2(messages)
    else:
        part_1(messages)
        part_2(messages)


if __name__ == "__main__":
    main()
