import argparse


def part_1(input_string):
    paired_assignments = input_string.split('\n')
    fully_contained_pair_count = 0
    for assignment in paired_assignments:
        pair_1, pair_2 = list(map(lambda x: tuple(map(int, x.split('-'))), assignment.split(',')))
        if (pair_1[0] >= pair_2[0] and pair_1[1] <= pair_2[1]) or (pair_2[0] >= pair_1[0] and pair_2[1] <= pair_1[1]):
            fully_contained_pair_count += 1
    print(fully_contained_pair_count)


def part_2(input_string):
    paired_assignments = input_string.split('\n')
    overlapped_pair_count = 0
    for assignment in paired_assignments:
        pair_1, pair_2 = list(map(lambda x: tuple(map(int, x.split('-'))), assignment.split(',')))
        if (pair_1[0] <= pair_2[0] <= pair_1[1]) or \
            (pair_1[0] <= pair_2[1] <= pair_1[1]) or \
            (pair_2[0] <= pair_1[0] <= pair_2[1]) or \
            (pair_2[0] <= pair_1[1] <= pair_2[1]):
            overlapped_pair_count += 1
    print(overlapped_pair_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_04.txt', 'r')
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
