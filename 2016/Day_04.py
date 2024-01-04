import argparse
import string
import re


def get_real_rooms(input_string):
    real_rooms = []
    for encrypted_room_name, sector_id, checksum in re.findall(r'([a-z\-]+)-(\d+)\[([a-z]+)]',
                                                               input_string):
        char_count = {}
        for c in encrypted_room_name:
            if c != '-':
                if char_count.get(c):
                    char_count[c] += 1
                else:
                    char_count[c] = 1
        top_five = [v[0] for v in sorted(char_count.items(), key=lambda kv: (-kv[1], kv[0]))][:5]
        if ''.join(top_five) == checksum:
            real_rooms.append({'room_name': encrypted_room_name,
                               'sector_id': int(sector_id),
                               'checksum': checksum})
    return real_rooms


def part_1(real_rooms):
    sector_id_sum = 0
    for room in real_rooms:
        sector_id_sum += room['sector_id']
    print("The sum of the sector IDs of the real rooms is {}".format(sector_id_sum))


def part_2(real_rooms):
    characters = string.ascii_lowercase
    for room in real_rooms:
        encrypted_name = room['room_name']
        key = room['sector_id'] % 26
        actual_name = ''
        for c in encrypted_name:
            if c == '-':
                actual_name += ' '
            else:
                actual_name += characters[(characters.index(c) + key) % 26]
        if 'pole' in actual_name.lower():
            print("Room name: {}\nSector_ID: {}".format(actual_name, room['sector_id']))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('../inputs/2016/Input_04.txt', 'r')
    input_string = file_input.read()
    file_input.close()

    real_rooms = get_real_rooms(input_string)

    if args.part == '1':
        part_1(real_rooms)
    elif args.part == '2':
        part_2(real_rooms)
    else:
        part_1(real_rooms)
        part_2(real_rooms)


if __name__ == "__main__":
    main()
