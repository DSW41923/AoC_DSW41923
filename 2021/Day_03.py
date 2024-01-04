import argparse


def part_1(input_string):
    report_bits = input_string.split('\n')
    rate_bits_length = len(report_bits[0])
    one_count = [0 for _ in range(rate_bits_length)]
    for bits in report_bits:
        for i, bit in enumerate(bits):
            if bit == '1':
                one_count[i] += 1

    gamma_rate = int(''.join([str(int(c > len(report_bits) / 2)) for c in one_count]), 2)
    epsilon_rate = int('1' * rate_bits_length, 2) ^ gamma_rate
    print(gamma_rate * epsilon_rate)


def part_2(input_string):
    report_bits = input_string.split('\n')
    O2_rating_candidates = report_bits
    CO2_rating_candidates = report_bits
    determining_bit = 0
    while len(O2_rating_candidates) > 1 or len(CO2_rating_candidates) > 1:
        if len(O2_rating_candidates) > 1:
            O2_one_count = 0
            for bits in O2_rating_candidates:
                if bits[determining_bit] == '1':
                    O2_one_count += 1

            if O2_one_count >= len(O2_rating_candidates) / 2:
                O2_rating_candidates = [bits for bits in O2_rating_candidates if bits[determining_bit] == '1']

            if O2_one_count < len(O2_rating_candidates) / 2:
                O2_rating_candidates = [bits for bits in O2_rating_candidates if bits[determining_bit] == '0']

        if len(CO2_rating_candidates) > 1:
            CO2_one_count = 0
            for bits in CO2_rating_candidates:
                if bits[determining_bit] == '1':
                    CO2_one_count += 1

            if CO2_one_count >= len(CO2_rating_candidates) / 2:
                CO2_rating_candidates = [bits for bits in CO2_rating_candidates if bits[determining_bit] == '0']

            if CO2_one_count < len(CO2_rating_candidates) / 2:
                CO2_rating_candidates = [bits for bits in CO2_rating_candidates if bits[determining_bit] == '1']

        determining_bit += 1

    O2_rating = int(O2_rating_candidates[0], 2)
    CO2_rating = int(CO2_rating_candidates[0], 2)
    print(O2_rating * CO2_rating)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2021/Input_03.txt', 'r')
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
