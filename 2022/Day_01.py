import argparse


def part_1(input_string):
    ungrouped_weights = input_string.split('\n')
    max_total_weight = 0
    current_total_weight = 0
    for w in ungrouped_weights:
        if w != '':
            try:
                current_total_weight += int(w)
            except ValueError:
                raise
        elif w == '':
            if current_total_weight > max_total_weight:
                max_total_weight = current_total_weight
            current_total_weight = 0
        else:
            raise
    print(max_total_weight)


def part_2(input_string):
    ungrouped_weights = input_string.split('\n')
    grouped_weights = []
    current_total_weight = 0
    for w in ungrouped_weights:
        if w != '':
            try:
                current_total_weight += int(w)
            except ValueError:
                raise
        elif w == '':
            grouped_weights.append(current_total_weight)
            current_total_weight = 0
        else:
            raise
    print(sum(sorted(grouped_weights, reverse=True)[:3]))



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2022/Input_01.txt', 'r')
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

