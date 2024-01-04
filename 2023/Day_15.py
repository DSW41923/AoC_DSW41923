import argparse
import re

def hash(string):
    result = 0
    for char in string:
        result += ord(char)
        result *= 17
        result %= 256
    return result


def part_1(input_string):
    steps = input_string.split(',')
    result = 0
    for step in steps:
        result += hash(step)
    print(result)


def part_2(input_string):
    steps = input_string.split(',')
    boxes = [[] for _ in range(256)]
    for step in steps:
        label, focal_length = re.split(r'[-=]', step)
        box_index = hash(label)
        labels_in_box = [l[0] for l in boxes[box_index]]
        if focal_length == '': # Operation character is -
            if label in labels_in_box:
                label_index = labels_in_box.index(label)
                del boxes[box_index][label_index]
        else:
            if label in labels_in_box:
                label_index = labels_in_box.index(label)
                boxes[box_index][label_index] = (label, int(focal_length))
            else:
                boxes[box_index].append((label, int(focal_length)))
    focusing_power = 0
    for b, box in enumerate(boxes):
        for l, lens in enumerate(box):
            focusing_power += (b+1)*(l+1)*lens[1]
    print(focusing_power)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_15.txt', 'r')
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
