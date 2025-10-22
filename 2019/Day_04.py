import argparse


def part_1(input_string):
    range_min, range_max = tuple(map(int, input_string.split('-')))
    doubles = [str(a)*2 for a in range(10)]
    result = 0
    for num in range(range_min, range_max+1):
        if any([d in str(num) for d in doubles]):
            num_list = list(map(int, list(str(num))))
            if any([num_list[i] > num_list[i+1] for i in range(5)]):
                continue
            result += 1
    print(result)


def part_2(input_string):
    range_min, range_max = tuple(map(int, input_string.split('-')))
    results = set()
    for num in range(range_min, range_max+1):
        for d in range(10):
            if str(d)*2 in str(num):
                if str(d)*3 in str(num):
                    continue
                num_list = list(map(int, list(str(num))))
                if any([num_list[i] > num_list[i+1] for i in range(5)]):
                    continue
                results.add(num)
    print(len(results))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_04.txt', 'r')
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
