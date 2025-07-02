import argparse

from pathlib import Path


DAY_FILE_CONTENT = '''import argparse


def part_1(input_string):
    pass


def part_2(input_string):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/{year}/Input_{day}.txt', 'r')
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
'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("year",
                        help="Specify initialization for which year.",
                        type=int)
    args = parser.parse_args()
    year = args.year
    print("Initializing for Adevent of Code Year {}".format(year))
    Path(str(year)).mkdir(exist_ok=True)
    Path( "./inputs/"+str(year)).mkdir(exist_ok=True)
    for day in range(1, 26):
        day_file_name = "./{}/Day_{}.py".format(year, str(day).zfill(2))
        input_file_name = "./inputs/{}/Input_{}.txt".format(year, str(day).zfill(2))
        with open(day_file_name, "w") as day_file, open(input_file_name, "w") as input_file:
            input_file.close()
            day_file.write(DAY_FILE_CONTENT.format(year=str(year),day=str(day).zfill(2)))
    print("Initialization for Adevent of Code Year {} Completed!".format(year))


if __name__ == "__main__":
    main()
