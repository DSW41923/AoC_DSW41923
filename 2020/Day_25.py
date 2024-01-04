import sys
import getopt
from math import gcd


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount


# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_25.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_25.py [-h | --help]')
            print('Advent of Code 2020 Day 25')
            sys.exit()

    file_input = open('inputs/2020/Input_25.txt', 'r')
    input_strings = file_input.readlines()
    file_input.close()
    pk1, pk2 = tuple(map(int, input_strings))
    n = 20201227
    s_n = 7
    phi_n = phi(n)
    loop_size_1, loop_size_2 = 0, 0
    trial_key = 1
    for p in range(1, phi_n+1):
        trial_key = (trial_key * s_n) % n
        if trial_key == pk1:
            loop_size_1 = p
            break
        if trial_key == pk2:
            loop_size_2 = p
            break

    def get_encryption_key(pk, loopsize):
        ek = 1
        for _ in range(loopsize):
            ek = (ek * pk) % 20201227
        return ek

    enc_key = 0
    if loop_size_1:
        enc_key = get_encryption_key(pk2, loop_size_1)
    if loop_size_2:
        enc_key = get_encryption_key(pk1, loop_size_2)
    print(enc_key)



if __name__ == "__main__":
    main(sys.argv[1:])