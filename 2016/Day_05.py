import argparse
import hashlib


def part_1(door_id):
    index = 0
    password = ''
    while len(password) < 8:
        trial_string = door_id + str(index)
        m = hashlib.md5()
        m.update(trial_string.encode())
        hash_result = m.hexdigest()
        if hash_result.startswith('00000'):
            password += hash_result[5]
        index += 1
    print(password)


def part_2(door_id):
    index = 0
    password = [''] * 8
    while any([p == '' for p in password]):
        trial_string = door_id + str(index)
        m = hashlib.md5()
        m.update(trial_string.encode())
        hash_result = m.hexdigest()
        if hash_result.startswith('00000'):
            position = hash_result[5]
            pwd_char = hash_result[6]
            try:
                if password[int(position)] == '':
                    password[int(position)] = pwd_char
            except IndexError:
                pass
            except ValueError:
                pass
        index += 1
    print(''.join(password))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    door_id = 'ojvtpuvg'

    if args.part == '1':
        part_1(door_id)
    elif args.part == '2':
        part_2(door_id)
    else:
        part_1(door_id)
        part_2(door_id)


if __name__ == "__main__":
    main()
