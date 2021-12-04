import argparse
import re


def lit_rect(screen, width, height):
    for h in range(height):
        for w in range(width):
            screen[h][w] = '*'


def right_shift(pixels, shift_num):
    return pixels[-shift_num:] + pixels[:-shift_num]


def rotate_row(screen, row_num, rotate_num):
    rotate_target = screen[row_num]
    screen[row_num] = right_shift(rotate_target, rotate_num)


def rotate_column(screen, column_num, rotate_num):
    rotate_target = []
    for row_pixels in screen:
        rotate_target.append(row_pixels[column_num])
    rotate_result = right_shift(rotate_target, rotate_num)
    for row_num, row_pixels in enumerate(screen):
        row_pixels[column_num] = rotate_result[row_num]


def get_final_screen(instructions):
    screen = [['.'] * 50 for _ in range(6)]
    for instruction in instructions:
        if instruction.startswith('rect'):
            width, height = re.findall(r'(\d+)x(\d+)', instruction)[0]
            lit_rect(screen, int(width), int(height))
        elif instruction.startswith('rotate row'):
            row_num, rotate_num = re.findall(r'y=(\d+) by (\d+)', instruction)[0]
            rotate_row(screen, int(row_num), int(rotate_num))
        elif instruction.startswith('rotate column'):
            column_num, rotate_num = re.findall(r'x=(\d+) by (\d+)', instruction)[0]
            rotate_column(screen, int(column_num), int(rotate_num))
    return screen


def part_1(instructions):
    screen = get_final_screen(instructions)
    lit_pixel_count = sum(s.count('*') for s in screen)
    print("{} pixels should be lit.".format(lit_pixel_count))


def part_2(instructions):
    screen = get_final_screen(instructions)
    print('\n'.join([''.join(row) for row in screen]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_08.txt', 'r')
    instructions = file_input.readlines()
    file_input.close()

    if args.part == '1':
        part_1(instructions)
    elif args.part == '2':
        part_2(instructions)
    else:
        part_1(instructions)
        part_2(instructions)


if __name__ == "__main__":
    main()
