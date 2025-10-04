import argparse
import re

from collections import Counter


def get_guard_data(input_string):
    records = []
    for date, time, detail in re.findall(r"\[([\d\-]+) ([\d:]+)\] ([\d\w# ]+)", input_string):
        records.append((date, time, detail))
    records.sort()
    guards = {}
    cur_guard_id = ''
    asleep = 0
    for date, time, detail in records:
        if "shift" in detail:
            cur_guard_id = re.search(r"Guard #(\d+)", detail).groups()[0]
            asleep = 0
        elif "asleep" in detail:
            asleep = int(time.split(':')[-1])
        elif "wake" in detail:
            if cur_guard_id not in guards:
                guards[cur_guard_id] = []
            guards[cur_guard_id].extend(list(range(asleep, int(time.split(':')[-1]))))
    return guards


def part_1(input_string):
    guards = get_guard_data(input_string)
    max_sleep = max([len(s) for s in guards.values()])
    for guard in guards:
        if len(guards[guard]) == max_sleep:
            sleep_min_count = Counter(guards[guard])
            print(int(guard) * sleep_min_count.most_common(1)[0][0])
            break


def part_2(input_string):
    guards = get_guard_data(input_string)
    max_sleep_freq = max([Counter(guards[guard]).most_common(1)[0][1] for guard in guards])
    for guard in guards:
        sleep_min_count = Counter(guards[guard])
        most_sleep_freq = sleep_min_count.most_common(1)[0][1]
        if most_sleep_freq == max_sleep_freq:
            print(int(guard) * sleep_min_count.most_common(1)[0][0])
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_04.txt', 'r')
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
