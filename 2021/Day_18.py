import argparse
import itertools

LEFT_ORDER = [59, 28,
              57, 27, 55, 26, 12,
              53, 25, 51, 24, 11,
              49, 23, 47, 22, 10, 4,
              45, 21, 43, 20, 9,
              41, 19, 39, 18, 8, 3,
              37, 17, 35, 16, 7,
              33, 15, 31, 14, 6, 2, 0]
RIGHT_ORDER = [32, 15,
               34, 16, 36, 17, 7,
               38, 18, 40, 19, 8,
               42, 20, 44, 21, 9, 3,
               46, 22, 48, 23, 10,
               50, 24, 52, 25, 11, 4,
               54, 26, 56, 27, 12,
               58, 28, 60, 29, 13, 5, 1]
SPLITTING_ORDER = [14, 15, 6, 16, 17, 7, 2, 18, 19, 8, 20, 21, 9, 3, 0,
                   22, 23, 10, 24, 25, 11, 4, 26, 27, 12, 28, 29, 13, 5, 1]


def reduce_snailfish_number(snailfish_number):
    while not all(n == '' for n in snailfish_number[30:]) \
            or any(n > 9 for n in snailfish_number if n not in ['', '^']):
        # Explode, apply on lowest layer pairs
        for j in range(32):
            exploding_element = snailfish_number[30 + j]
            snailfish_number[30 + j] = ''

            if j in [0, 31]:
                continue

            if type(exploding_element) is int:
                if j % 2 == 0:
                    for k in LEFT_ORDER[LEFT_ORDER.index(30 + j - 1):]:
                        if type(snailfish_number[k]) is int:
                            snailfish_number[k] += exploding_element
                            break

                if j % 2 == 1:
                    for k in RIGHT_ORDER[RIGHT_ORDER.index(30 + j + 1):]:
                        if type(snailfish_number[k]) is int:
                            snailfish_number[k] += exploding_element
                            break

                if snailfish_number[14 + j // 2] == '^':
                    snailfish_number[14 + j // 2] = 0

        # Splitting one time
        splitted = False
        for i in SPLITTING_ORDER:
            if type(snailfish_number[i]) is int:
                if snailfish_number[i] >= 10:
                    splitting_element = snailfish_number[i]
                    snailfish_number[2 * i + 2] = splitting_element // 2
                    snailfish_number[2 * i + 3] = splitting_element // 2 + 1 \
                        if splitting_element % 2 == 1 else splitting_element // 2
                    snailfish_number[i] = '^'
                    splitted = True

            if splitted:
                break

    return snailfish_number


def snailfish_number_add(snailfish_number_0, snailfish_number_1):
    if all(n == '' for n in snailfish_number_0):
        return snailfish_number_1
    if all(n == '' for n in snailfish_number_1):
        return snailfish_number_0

    snailfish_sum: list = ['' for _ in range(62)]
    snailfish_sum[0] = '^'
    snailfish_sum[1] = '^'
    j = 1
    for i in range(30):
        snailfish_sum[i + 2 ** j] = snailfish_number_0[i]
        snailfish_sum[i + 2 ** (j + 1)] = snailfish_number_1[i]
        if i in [1, 5, 13]:
            j += 1

    snailfish_sum = reduce_snailfish_number(snailfish_sum)

    return snailfish_sum[:30]


def print_snailfish_number(snailfish_number):
    print(snailfish_number[:2])
    print(snailfish_number[2:6])
    print(snailfish_number[6:14])
    if len(snailfish_number) == 30:
        print(snailfish_number[14:])
        return
    print(snailfish_number[14:30])
    print(snailfish_number[30:])
    return


def evaluate_magnitude(snailfish_number):
    if snailfish_number[0] == '^':
        left = snailfish_number[2:4]
        if len(snailfish_number) > 6:
            left += snailfish_number[6:10]
        if len(snailfish_number) > 14:
            left += snailfish_number[14:22]
        snailfish_number[0] = evaluate_magnitude(left)

    if snailfish_number[1] == '^':
        right = snailfish_number[4:6]
        if len(snailfish_number) > 6:
            right += snailfish_number[10:14]
        if len(snailfish_number) > 14:
            right += snailfish_number[22:]
        snailfish_number[1] = evaluate_magnitude(right)

    return 3 * snailfish_number[0] + 2 * snailfish_number[1]


def parse_snailfish_number(snailfish_number_string):
    i, j = 0, 0
    new_snailfish_number: list = ['' for _ in range(30)]
    for char in snailfish_number_string:
        if char == ',':
            j += 1
            continue

        if char == '[':
            if (i, j) != (0, 0):
                new_snailfish_number[2 ** i - 2 + j] = '^'
            i += 1
            j *= 2
            continue

        if char == ']':
            i -= 1
            j = j // 2
            continue

        if char.isdigit():
            new_snailfish_number[2 ** i - 2 + j] = int(char)
            continue

        raise

    return new_snailfish_number


def part_1(input_string):
    snailfish_sum: list = ['' for _ in range(30)]
    for snailfish_number_string in input_string.split('\n'):
        new_snailfish_number = parse_snailfish_number(snailfish_number_string)
        snailfish_sum = snailfish_number_add(snailfish_sum, new_snailfish_number)
    print(evaluate_magnitude(snailfish_sum))


def part_2(input_string):
    snailfish_numbers = []
    for snailfish_number_string in input_string.split('\n'):
        new_snailfish_number = parse_snailfish_number(snailfish_number_string)
        snailfish_numbers.append(new_snailfish_number)

    max_two_snailfish_sum = 0
    for snailfish_number_0, snailfish_number_1 in itertools.combinations(snailfish_numbers, 2):
        snailfish_sum = snailfish_number_add(snailfish_number_0, snailfish_number_1)
        max_two_snailfish_sum = max(max_two_snailfish_sum, evaluate_magnitude(snailfish_sum))

    print(max_two_snailfish_sum)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2021/Input_18.txt', 'r')
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
