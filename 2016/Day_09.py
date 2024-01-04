import argparse
import re


def compute_decompressed_sequence_length(sequence):
    length = 0
    current_position = 0
    while current_position < len(sequence):
        if marker := re.match(r'\((\d+)x(\d+)\)', sequence[current_position:]):
            start_repeating_position = current_position + len(marker.group(0))
            repeating_length, repeating_times = int(marker.group(1)), int(marker.group(2))
            repeating_characters = sequence[start_repeating_position:start_repeating_position + repeating_length]
            if re.match(r'\((\d+)x(\d+)\)', repeating_characters):
                length += compute_decompressed_sequence_length(repeating_characters) * repeating_times
            else:
                length += repeating_length * repeating_times
            current_position = start_repeating_position + repeating_length
        else:
            length += 1
            current_position += 1
    return length


def part_1(compressed_sequence):
    decompressed_sequence = ''
    current_position = 0
    while current_position < len(compressed_sequence):
        if marker := re.match(r'\((\d+)x(\d+)\)', compressed_sequence[current_position:]):
            start_repeating_position = current_position + len(marker.group(0))
            repeating_length, repeating_times = int(marker.group(1)), int(marker.group(2))
            repeating_characters = compressed_sequence[start_repeating_position:
                                                       start_repeating_position + repeating_length]

            decompressed_sequence += repeating_characters * repeating_times
            current_position = start_repeating_position + repeating_length
        else:
            decompressed_sequence += compressed_sequence[current_position]
            current_position += 1
    print("The decompressed length of the file is {}".format(len(decompressed_sequence)))


def part_2(compressed_sequence):
    decompressed_sequence_length = compute_decompressed_sequence_length(compressed_sequence)
    print("The actual decompressed length of the file is {}".format(decompressed_sequence_length))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('../inputs/2016/Input_09.txt', 'r')
    compressed_sequence = file_input.read()
    file_input.close()

    if args.part == '1':
        part_1(compressed_sequence)
    elif args.part == '2':
        part_2(compressed_sequence)
    else:
        part_1(compressed_sequence)
        part_2(compressed_sequence)


if __name__ == "__main__":
    main()
