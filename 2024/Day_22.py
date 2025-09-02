import argparse


def part_1(input_string):
    secret_numbers = list(map(int, input_string.split('\n')))
    result = 0
    for num in secret_numbers:
        for _ in range(2000):
            tmp = num << 6
            num ^= tmp
            num %= 16777216
            tmp = num >> 5
            num ^= tmp
            num %= 16777216
            tmp = num << 11
            num ^= tmp
            num %= 16777216
        result += num
    print(result)


def part_2(input_string):
    secret_numbers = list(map(int, input_string.split('\n')))
    prices_per_buyer = []
    for num in secret_numbers:
        prices = []
        for _ in range(2000):
            tmp = num << 6
            num ^= tmp
            num %= 16777216
            tmp = num >> 5
            num ^= tmp
            num %= 16777216
            tmp = num << 11
            num ^= tmp
            num %= 16777216
            prices.append(num%10)
        prices_per_buyer.append(prices)
    price_change_per_buyer = []
    all_price_change_sequences = set()
    for p in prices_per_buyer:
        price_change = []
        price_change_buyer = {}
        for i in range(1, len(p)):
            price_change.append(p[i]-p[i-1])
            if i >= 4:
                pc_seq = tuple(price_change)
                if pc_seq not in price_change_buyer:
                    price_change_buyer[pc_seq] = p[i]
                price_change.pop(0)
        for pc in price_change_buyer:
            all_price_change_sequences.add(pc)
        price_change_per_buyer.append(price_change_buyer)
    result = 0
    for pc in all_price_change_sequences:
        pc_result = 0
        for pcpb in price_change_per_buyer:
            if pc in pcpb:
                pc_result += pcpb[pc]
        result = max(pc_result, result)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_22.txt', 'r')
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
