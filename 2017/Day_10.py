import argparse


def part_1(input_string):
    numbers = list(range(256))
    cur = 0
    skip = 0
    for length in list(map(int, input_string.split(','))):
        numbers = list(reversed(numbers[:length])) + numbers[length:]
        cur = (cur + length + skip) % 256
        numbers = numbers[(length + skip) % 256:] + numbers[:(length + skip) % 256]
        skip += 1
    print(numbers[-cur] * numbers[-cur + 1])


def part_2(input_string):
    lengths = list(map(ord, input_string)) + [17, 31, 73, 47, 23]
    numbers = list(range(256))
    cur = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
            numbers = list(reversed(numbers[:length])) + numbers[length:]
            cur = (cur + length + skip) % 256
            numbers = numbers[(length + skip) % 256:] + numbers[:(length + skip) % 256]
            skip += 1
    numbers = numbers[-cur:] + numbers[:-cur]
    output = [0 for _ in range(16)]
    for i in range(256):
        output[i // 16] ^= numbers[i]
    print(''.join(list(map(lambda o: "{:02x}".format(o), output))))


def knot_hash(msg):
    lengths = list(map(ord, msg)) + [17, 31, 73, 47, 23]
    numbers = list(range(256))
    cur = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
            numbers = list(reversed(numbers[:length])) + numbers[length:]
            cur = (cur + length + skip) % 256
            numbers = numbers[(length + skip) % 256:] + numbers[:(length + skip) % 256]
            skip += 1
    numbers = numbers[-cur:] + numbers[:-cur]
    output = [0 for _ in range(16)]
    for i in range(256):
        output[i // 16] ^= numbers[i]
    return ''.join(list(map(lambda o: "{:02x}".format(o), output)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_10.txt', 'r')
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
