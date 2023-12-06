import argparse
import re


def part_1(input_string):
    times, distances = input_string.split('\n')
    times = list(map(int, re.findall(r"(\d+)", times)))
    distances = list(map(int, re.findall(r"(\d+)", distances)))
    races = list(zip(times, distances))
    result = 1
    for time, distance in races:
        time_min, time_max = 0, 0
        while time_min == time_max == 0:
            for t in range(1, time):
                if distance <= t * (time - t):
                    time_min = t
                    time_max = time - t
                    break
            if time_min == time_max:
                distance += 1
        result *= (time_max - time_min + 1)
    print(result)


def part_2(input_string):
    time, distance = tuple(map(lambda x: int(''.join(re.findall(r"(\d+)", x))), input_string.split('\n')))
    result = 1
    time_min, time_max = 0, 0
    while time_min == time_max == 0:
        for t in range(1, time):
            if distance <= t * (time - t):
                time_min = t
                time_max = time - t
                break
        if time_min == time_max:
            distance += 1
    result *= (time_max - time_min + 1)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_06.txt', 'r')
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
