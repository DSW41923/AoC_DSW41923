import argparse

from itertools import product


def get_z(w):
    z = w[0] * (26 ** 2) + w[1] * 26 + 12 * 26 + w[2] + 14

    if w[3] - 2 != w[4]:
        z = z * 26 + w[4] + 3

    z = z * 26 + w[5] + 15

    if w[6] - 4 != w[7]:
        z = z * 26 + w[7] + 12

    if w[8] - 8 != w[9]:
        z = z * 26 + w[9] + 12

    x_parameter = {10: 9, 11: 7, 12: 4, 13: 6}
    y_parameter = {10: 3, 11: 10, 12: 14, 13: 12}
    for i in range(10, 14):
        x = z % 26
        z //= 26
        if x - x_parameter[i] != w[i]:
            z = z * 26 + w[i] + y_parameter[i]

    return z


def part_1(input_string):
    instructions = input_string.split('\n')
    print("{} instructions to run...?!".format(len(instructions) * 9 ** 14))
    num = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
    pair_34 = ['97', '86', '75', '64', '53', '42', '31']
    pair_67 = ['95', '84', '73', '62', '51']
    pair_89 = ['91']
    candidate_numbers = map(lambda n: ''.join(n),
                            product(num, ['1'], num, pair_34, num, pair_67, pair_89, num, num, ['9'], num))
    for model_number_string in candidate_numbers:
        w = list(map(int, list(model_number_string)))
        z = get_z(w)
        if z == 0:
            print()
            print("Found! {}".format(int(model_number_string)))
            break
        else:
            print("Trying number {}, result is {}".format(int(model_number_string), z), end='\r')


def part_2(input_string):
    instructions = input_string.split('\n')
    print("Still {} instructions to run...?!".format(len(instructions) * 9 ** 14))
    print("Reverse engineered in part 1. Let's do more in part 2!")
    pair_0d = [('7', '1'), ('8', '2'), ('9', '3')]
    pair_1c = [('1', '9')]
    pair_2b = [('1', '8'), ('2', '9')]
    pair_5a = [('1', '7'), ('2', '8'), ('3', '9')]
    pair_34 = ['31', '42', '53', '64', '75', '86', '97']
    pair_67 = ['51', '62', '73', '84', '95']
    pair_89 = ['91']
    candidate_templates = list(product(pair_0d, pair_1c, pair_2b, pair_5a))
    candidate_numbers = map(lambda n: ''.join([n[0][0][0], n[0][1][0], n[0][2][0], n[1], n[0][3][0], n[2],
                                               n[3], n[0][3][1], n[0][2][1], n[0][1][1], n[0][0][1]]),
                            product(candidate_templates, pair_34, pair_67, pair_89))

    for model_number_string in candidate_numbers:
        w = list(map(int, list(model_number_string)))
        z = get_z(w)
        if z == 0:
            print(int(model_number_string))
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_24.txt', 'r')
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
