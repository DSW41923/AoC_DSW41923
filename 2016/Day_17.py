import argparse

from Day_14 import simple_md5_hash


DIRECTIONS = ['U', 'D', 'L', 'R']


def get_path(passcode, part):
    paths = [{'room': (0, 0), 'passcode_path': passcode}]
    longest_path = ''
    while paths:
        new_paths = []
        for path in paths:
            door_data = simple_md5_hash(path['passcode_path'])[:4]
            available_directions = []
            for i, char in enumerate(door_data):
                if int(char, 16) > 10:
                    available_directions.append(DIRECTIONS[i])
            for direction in available_directions:

                if direction == 'U':
                    if path['room'][1] - 1 >= 0:
                        new_paths.append({
                            'room': (path['room'][0], path['room'][1] - 1),
                            'passcode_path': path['passcode_path'] + direction})
                    continue

                if direction == 'D':
                    if path['room'][1] + 1 <= 3:
                        new_paths.append({
                            'room': (path['room'][0], path['room'][1] + 1),
                            'passcode_path': path['passcode_path'] + direction})
                    continue

                if direction == 'L':
                    if path['room'][0] - 1 >= 0:
                        new_paths.append({
                            'room': (path['room'][0] - 1, path['room'][1]),
                            'passcode_path': path['passcode_path'] + direction})
                    continue

                if direction == 'R':
                    if path['room'][0] + 1 <= 3:
                        new_paths.append({
                            'room': (path['room'][0] + 1, path['room'][1]),
                            'passcode_path': path['passcode_path'] + direction})
                    continue

        paths = new_paths

        for path in new_paths:
            if path['room'] == (3, 3):
                if part == 1:
                    return path['passcode_path'][len(passcode):]

                if part == 2:
                    paths.remove(path)
                    if len(path['passcode_path']) - len(passcode) > len(longest_path):
                        longest_path = path['passcode_path'][len(passcode):]

    return longest_path


def part_1(passcode):
    print(get_path(passcode, part=1))


def part_2(passcode):
    print(len(get_path(passcode, part=2)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    passcode = 'lpvhkcbi'

    if args.part == '1':
        part_1(passcode)
    elif args.part == '2':
        part_2(passcode)
    else:
        part_1(passcode)
        part_2(passcode)


if __name__ == "__main__":
    main()
