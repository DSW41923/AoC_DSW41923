import argparse
import re


def union_intervals(intervals, new_interval):
    new_a, new_b = new_interval
    for i, (a, b) in enumerate(intervals):
        if not (b < new_a - 1 or a > new_b + 1):
            new_a = min(new_a, a)
            new_b = max(new_b, b)
            intervals[i] = new_a, new_b
            return

    intervals.append(new_interval)


def get_blocked_ip(blocked_ip_data):
    blocked_ip_intervals = []

    for lower_bound, upper_bound in re.findall(r'(\d+)-(\d+)', blocked_ip_data):
        union_intervals(blocked_ip_intervals, (int(lower_bound), int(upper_bound)))

    merged_blocked_ip_intervals = []
    for lower_bound, upper_bound in blocked_ip_intervals:
        union_intervals(merged_blocked_ip_intervals, (int(lower_bound), int(upper_bound)))

    merged_blocked_ip_intervals.sort(key=lambda x: x[0])

    return merged_blocked_ip_intervals


def part_1(input_string):
    blocked_ip_intervals = get_blocked_ip(input_string)
    for i in range(2**32):
        next_ip = False
        for lo, up in blocked_ip_intervals:
            if lo <= i <= up:
                next_ip = True
                break

        if not next_ip:
            print(i)
            return


def part_2(input_string):
    blocked_ip_intervals = get_blocked_ip(input_string)
    allowed_ip_counts = 2**32
    for lo, up in blocked_ip_intervals:
        allowed_ip_counts -= (up-lo+1)
    print(allowed_ip_counts)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2016/Input_20.txt', 'r')
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
