import argparse

from copy import deepcopy


def part_1(input_string):
    histories = [list(map(int, line.split(' '))) for line in input_string.split('\n')]
    result = 0
    for history in histories:
        histories_of_history= [history]
        while not all([h == 0 for h in histories_of_history[-1]]):
            new_h = []
            for i in range(len(histories_of_history[-1])-1):
                new_h.append(histories_of_history[-1][i+1]-histories_of_history[-1][i])
            histories_of_history.append(new_h)
        result += sum([h[-1] for h in histories_of_history])
    print(result)


def part_2(input_string):
    histories = [list(map(int, line.split(' '))) for line in input_string.split('\n')]
    result = 0
    for history in histories:
        histories_of_history= [history]
        while not all([h == 0 for h in histories_of_history[-1]]):
            new_h = []
            for i in range(len(histories_of_history[-1])-1):
                new_h.append(histories_of_history[-1][i+1]-histories_of_history[-1][i])
            histories_of_history.append(new_h)
        result += sum([h[0]*(-1)**i for i, h in enumerate(histories_of_history)])
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_09.txt', 'r')
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
