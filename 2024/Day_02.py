import argparse


def is_report_safe(report):
    asc = False
    if report[0] < report[1]:
        asc = True
    elif report[0] == report[1]:
        return False
    for i in range(len(report)-1):
        if not (1 <= abs(report[i] - report[i+1]) <= 3):
            return False

        if asc and report[i] > report[i+1]:
            return False

        if (not asc) and report[i] < report[i+1]:
            return False
    return True
        # if i == len(report)-2:
        #     safe_report_count += 1

def part_1(input_string):
    safe_report_count = 0
    for report_str in input_string.split('\n'):
        report = list(map(int, report_str.split(' ')))
        asc = False
        if report[0] < report[1]:
            asc = True
        elif report[0] == report[1]:
            continue
        for i in range(len(report)-1):
            if not (1 <= abs(report[i] - report[i+1]) <= 3):
                break

            if asc and report[i] > report[i+1]:
                break

            if (not asc) and report[i] < report[i+1]:
                break

            if i == len(report)-2:
                safe_report_count += 1
    print(safe_report_count)
    # print(len([report for report in list(map(lambda l: list(map(int, l.split(' '))), input_string.split('\n'))) if is_report_safe(report)]))


def part_2(input_string):
    safe_report_count = 0
    potential_safe_reports = []
    for report_str in input_string.split('\n'):
        report = list(map(int, report_str.split(' ')))
        if is_report_safe(report):
            safe_report_count += 1
        else:
            potential_safe_reports.append(report)
    
    for report in potential_safe_reports:
        for i in range(len(report)):
            new_report = [report[j] for j in range(len(report)) if j != i]
            if is_report_safe(new_report):
                safe_report_count += 1
                break
    print(safe_report_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_02.txt', 'r')
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
