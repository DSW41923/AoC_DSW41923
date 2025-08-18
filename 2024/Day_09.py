import argparse


def get_checksum(disk_map):
    checksum = 0
    for i in range(len(disk_map)):
        if disk_map[i] == '.':
            continue
        checksum += i * int(disk_map[i])
    return checksum


def part_1(input_string):
    dense_disk_map = list(input_string)
    disk_map_len = sum(map(int, dense_disk_map))
    disk_map = ['.' for _ in range(disk_map_len)]
    pos = 0
    file_num = 0
    for i in range(len(dense_disk_map)):
        if i % 2 == 0:
            for _ in range(int(dense_disk_map[i])):
                disk_map[pos] = str(file_num)
                pos += 1
            file_num += 1
        else:
            pos += int(dense_disk_map[i])
    start_pos = 0
    end_pos = disk_map_len-1
    while end_pos > start_pos:
        if disk_map[end_pos] != '.':
            for i in range(start_pos, end_pos):
                if disk_map[i] == '.':
                    start_pos = i
                    break
            disk_map[start_pos], disk_map[end_pos] = disk_map[end_pos], disk_map[start_pos]
        end_pos -= 1

    print(get_checksum(disk_map))


def part_2(input_string):
    dense_disk_map = list(input_string)
    disk_map_len = sum(map(int, dense_disk_map))
    disk_map = ['.' for _ in range(disk_map_len)]
    files = []
    spaces = []
    pos = 0
    file_num = 0
    for i in range(len(dense_disk_map)):
        if i % 2 == 0:
            file_size = int(dense_disk_map[i])
            files.append((str(file_num), pos, file_size))
            for _ in range(file_size):
                disk_map[pos] = str(file_num)
                pos += 1
            file_num += 1
        else:
            space_size = int(dense_disk_map[i])
            if space_size > 0:
                spaces.append((pos, space_size))
            pos += space_size

    files.sort(key=lambda f: int(f[0]), reverse=True)
    for file_id, file_pos, file_size in files:
        target_pos = file_pos
        for space_pos, space_size in spaces:
            if space_size >= file_size:
                target_pos = space_pos
                spaces.remove((space_pos, space_size))
                if space_size > file_size:
                    spaces.append((space_pos+file_size, space_size-file_size))
                    spaces.sort(key=lambda s: s[0])
                break
        if target_pos < file_pos:
            for i in range(file_size):
                disk_map[file_pos+i] = '.'
                disk_map[target_pos+i] = file_id

    print(get_checksum(disk_map))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_09.txt', 'r')
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
