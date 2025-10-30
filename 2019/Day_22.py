import argparse


def power_mod(a, n, p):
    e = 1
    for i in bin(n)[2:]:
        e *= e
        if i == '1':
            e *= a
        e %= p
    return e


def b_inverse_modulo_a(a, b):
    mod_base = a
    x = 0
    y = 1
    while b != 0:
        a, b, x, y = b, a % b, y, x-y*int(a/b)
    while x < 0:
        x += mod_base
    if x == 1:
        return "No inverse!"
    else:
        return x
    

def part_1(input_string):
    card_num = 10007
    target = 2019
    shuffle_process = input_string.split('\n')
    # deck = list(range(card_num))
    # for technique in shuffle_process:
    #     if technique == "deal into new stack":
    #         deck.reverse()
    #     elif technique.startswith("deal"):
    #         increment = int(technique.split(' ')[-1])
    #         new_deck = [-1 for _ in range(card_num)]
    #         for i, card in enumerate(deck):
    #             new_deck[(i*increment)%card_num] = card
    #         deck = new_deck
    #     elif technique.startswith("cut"):
    #         cut = int(technique.split(' ')[-1])
    #         deck = deck[cut:] + deck[:cut]
    # print(deck.index(target))

    for technique in shuffle_process:
        if technique == "deal into new stack":
            target = card_num - target - 1
        elif technique.startswith("deal"):
            increment = int(technique.split(' ')[-1])
            target = (target*increment)%card_num
        elif technique.startswith("cut"):
            cut = int(technique.split(' ')[-1])
            target -= cut
            target %= card_num
    print(target)


def part_2(input_string):
    # card_num = 10007
    card_num = 119315717514047
    shuffle_process = input_string.split('\n')

    a, b = 1, 0
    for technique in shuffle_process[::-1]:
        if technique == "deal into new stack":
            a *= -1
            b *= -1
            b -= 1
        elif technique.startswith("deal"):
            increment = int(technique.split(' ')[-1])
            inv = b_inverse_modulo_a(card_num, increment)
            a *= inv
            b *= inv
        elif technique.startswith("cut"):
            cut = int(technique.split(' ')[-1])
            b += cut
        a %= card_num
        b %= card_num

    '''
    y0 = ax+b
    y1 = a(ax+b)+b = a**2x+ab+b = (a**2)x + (a+1)*b
    y2 = a((a**2)x + (a+1)*b)+b = a**3x+a**2*b+ab+b = (a**3)x + (a**2+a+1)*b
    yn = (a**n)x + (a**(n-1)+...+a**2+a+1)*b = (a**n)x + (a**n-1)/(a-1)*b
    '''
    round_num = 101741582076661
    result = 2020
    # print(a,b)
    e = power_mod(a, round_num, card_num)
    # print(b_inverse_modulo_a(card_num, e))
    b *= (e-1)*b_inverse_modulo_a(card_num, a-1)
    b %= card_num
    # print(e, b)
    result *= e
    result %= card_num
    result += b
    result %= card_num
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_22.txt', 'r')
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
