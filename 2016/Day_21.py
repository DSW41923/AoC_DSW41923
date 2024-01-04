import argparse
import re


def swap_char_in_str(string, char_0, char_1):
    return string.replace(char_0, '0').replace(char_1, '1').replace('0', char_1).replace('1', char_0)


def move_char_in_str_by_index(string, index_0, index_1):
    char_list = list(string)
    moving_char = char_list.pop(index_0)
    char_list.insert(index_1, moving_char)
    return ''.join(char_list)


def rotate_string(string, rotation):
    return string[rotation:] + string[:rotation]


def part_1(input_string):
    password = 'abcdefgh'
    operations = input_string.split('\n')
    for operation in operations:
        if matched := re.match(r'swap position (\d) with position (\d)', operation):
            pos_0, pos_1 = map(int, matched.groups())
            char_0, char_1 = password[pos_0], password[pos_1]
            password = swap_char_in_str(password, char_0, char_1)
            continue
        if matched := re.match(r'swap letter (\w) with letter (\w)', operation):
            char_0, char_1 = matched.groups()
            password = swap_char_in_str(password, char_0, char_1)
            continue
        if matched := re.match(r'rotate left (\d) steps?', operation):
            rotating_steps = int(matched.group(1))
            password = rotate_string(password, rotating_steps)
            continue
        if matched := re.match(r'rotate right (\d) steps?', operation):
            rotating_steps = -int(matched.group(1))
            password = rotate_string(password, rotating_steps)
            continue
        if matched := re.match(r'rotate based on position of letter (\w)', operation):
            char = matched.group(1)
            char_index = password.index(char)
            rotating_steps = -(char_index + 2) % 8 if char_index >= 4 else -(char_index + 1)
            password = rotate_string(password, rotating_steps)
            continue
        if matched := re.match(r'reverse positions (\d) through (\d)', operation):
            pos_0, pos_1 = map(int, matched.groups())
            reversed_part = password[pos_1:pos_0-1:-1] if pos_0 > 1 else password[pos_1::-1]
            password = password[:pos_0] + reversed_part + password[pos_1+1:]
            continue
        if matched := re.match(r'move position (\d) to position (\d)', operation):
            pos_0, pos_1 = map(int, matched.groups())
            password = move_char_in_str_by_index(password, pos_0, pos_1)
            continue

    print(password)


def part_2(input_string):
    password = 'fbgdceah'
    operations = input_string.split('\n')
    for operation in reversed(operations):
        if matched := re.match(r'swap position (\d) with position (\d)', operation):
            pos_0, pos_1 = map(int, matched.groups())
            char_0, char_1 = password[pos_0], password[pos_1]
            password = swap_char_in_str(password, char_0, char_1)
            continue
        if matched := re.match(r'swap letter (\w) with letter (\w)', operation):
            char_0, char_1 = matched.groups()
            password = swap_char_in_str(password, char_0, char_1)
            continue
        if matched := re.match(r'rotate left (\d) steps?', operation):
            rotating_steps = -int(matched.group(1))
            password = rotate_string(password, rotating_steps)
            continue
        if matched := re.match(r'rotate right (\d) steps?', operation):
            rotating_steps = int(matched.group(1))
            password = rotate_string(password, rotating_steps)
            continue
        if matched := re.match(r'rotate based on position of letter (\w)', operation):
            char = matched.group(1)
            char_index = password.index(char)
            char_index = 8 if char_index == 0 else char_index
            rotating_steps = (char_index + 1) // 2 if char_index % 2 == 1 else (char_index // 2 + 5) % 8
            password = rotate_string(password, rotating_steps)
            continue
        if matched := re.match(r'reverse positions (\d) through (\d)', operation):
            pos_0, pos_1 = map(int, matched.groups())
            reversed_part = password[pos_1:pos_0 - 1:-1] if pos_0 > 1 else password[pos_1::-1]
            password = password[:pos_0] + reversed_part + password[pos_1 + 1:]
            continue
        if matched := re.match(r'move position (\d) to position (\d)', operation):
            pos_0, pos_1 = map(int, matched.groups())
            password = move_char_in_str_by_index(password, pos_1, pos_0)
            continue

    print(password)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2016/Input_21.txt', 'r')
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
