import argparse


def get_lanternfish_count(timer, count_history, day):
    if day == 0:
        count_history[timer][0] = 1
        return count_history[timer][day]

    if timer == 0:
        if count_history[6][day - 1] == 0:
            count_history[6][day - 1] = get_lanternfish_count(6, count_history, day - 1)

        if count_history[8][day - 1] == 0:
            count_history[8][day - 1] = get_lanternfish_count(8, count_history, day - 1)

        count_history[0][day] = count_history[6][day - 1] + count_history[8][day - 1]
        return count_history[0][day]

    if count_history[timer - 1][day - 1] == 0:
        count_history[timer - 1][day - 1] = get_lanternfish_count(timer - 1, count_history, day - 1)
    count_history[timer][day] = count_history[timer - 1][day - 1]
    return count_history[timer][day]


def part_1(input_string):
    lanternfish_timers = list(map(int, input_string.split(',')))
    day = 0
    while day < 80:
        day += 1
        new_lanterfish_count = len([t for t in lanternfish_timers if t == 0])
        for i in range(len(lanternfish_timers)):
            if lanternfish_timers[i] == 0:
                lanternfish_timers[i] = 6
                continue
            lanternfish_timers[i] -= 1
        lanternfish_timers.extend([8 for _ in range(new_lanterfish_count)])

    print(len(lanternfish_timers))


def part_2(input_string):
    lanternfish_timers = list(map(int, input_string.split(',')))
    timers_count = [lanternfish_timers.count(i) for i in range(7)]
    days = 256
    lanternfish_count = 0
    lanternfish_count_history = [[0 for _ in range(days+1)] for _ in range(9)]
    for i, t in enumerate(timers_count):
        lanternfish_count += get_lanternfish_count(i, lanternfish_count_history, days) * t

    print(lanternfish_count)


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
