import argparse
import re


def part_1(input_string):
    scanners = []
    for layer, scanning_range in re.findall(r'(\d+): (\d+)', input_string):
        while len(scanners) < int(layer):
            scanners.append(0)
        scanners.append(int(scanning_range))
    severity  = 0
    for t in range(len(scanners)):
        if scanners[t] == 0:
            continue
        scanner_pos = t % (2 * scanners[t] - 2)
        if scanner_pos == 0:
            severity += t * scanners[t]
    print(severity)


def part_2(input_string):
    scanners = []
    for layer, scanning_range in re.findall(r'(\d+): (\d+)', input_string):
        while len(scanners) < int(layer):
            scanners.append(0)
        scanners.append(int(scanning_range))
    time = 0
    caught = True
    while caught:
        caught = False
        time += 1
        for t in range(len(scanners)):
            if scanners[t] == 0:
                continue
            scanner_pos = (time + t) % (2 * scanners[t] - 2)
            if scanner_pos == 0:
                caught = True
                break
    print(time)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_13.txt', 'r')
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
