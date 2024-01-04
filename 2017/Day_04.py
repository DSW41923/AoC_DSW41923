import argparse
import string


def part_1(input_string):
    passphrases = input_string.split('\n')
    result = 0
    for passphrase in passphrases:
        words = passphrase.split(' ')
        if len(set(words)) == len(words):
            result += 1
    print(result)


def part_2(input_string):
    passphrases = input_string.split('\n')
    result = 0
    for passphrase in passphrases:
        words = passphrase.split(' ')
        encoded_words = []
        for word in words:
            encoded_word = ""
            for char in string.ascii_lowercase:
                encoded_word += char + str(word.count(char))
            if encoded_word not in encoded_words:
                encoded_words.append(encoded_word)
        if len(encoded_words) == len(words):
            result += 1
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2017/Input_04.txt', 'r')
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
