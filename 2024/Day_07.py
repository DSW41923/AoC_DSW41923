import argparse
import re


def part_1(input_string):
    result = 0
    for target, numbers in re.findall(r'(\d+): ([\d ]+)', input_string):
        target = int(target)
        numbers = list(map(int, numbers.split(' ')))
        for i in range(2**(len(numbers)-1)):
            trial = numbers[0]
            opertors = bin(i)[2:].zfill(len(numbers) - 1)
            for j, o in enumerate(opertors):
                if o == '0':
                    trial *= numbers[j+1]
                elif o == '1':
                    trial += numbers[j+1]
                if trial > target:
                    break
            if trial == target:
                result += target
                break
    print(result)


def part_2(input_string):
    result = 0
    for target, numbers in re.findall(r'(\d+): ([\d ]+)', input_string):
        target = int(target)
        numbers = list(map(int, numbers.split(' ')))
        for i in range(3**(len(numbers)-1)):
            trial = numbers[0]
            for j in range(len(numbers)-1):
                if (i%3) == 0:
                    trial *= numbers[j+1]
                elif (i%3) == 1:
                    trial += numbers[j+1]
                elif (i%3) == 2:
                    trial = int(str(trial)+str(numbers[j+1]))
                if trial > target:
                    break
                i = i//3
            if trial == target:
                result += target
                break
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_07.txt', 'r')
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
