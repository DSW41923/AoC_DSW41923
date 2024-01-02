import argparse
import re

from itertools import product


def settle_brick(settled_bricks, brick):
    b0x, b0y, b0z = brick[0]
    b1x, b1y, b1z = brick[1]

    next_z = min(b1z, b0z) - 1
    is_settled = False
    while next_z > 0 and not is_settled:
        bxy_spand = set(product(range(b0x, b1x+1), range(b0y, b1y+1)))
        for b0, b1 in settled_bricks:
            if max(b0[2], b1[2]) == next_z:
                xy_spand = set(product(range(b0[0], b1[0]+1), range(b0[1], b1[1]+1)))
                if len(bxy_spand & xy_spand):
                    is_settled = True
                    break
        if not is_settled:
            next_z -= 1
    settled_bricks.append(((b0x, b0y, next_z+1), (b1x, b1y, next_z+1+(b1z-b0z))))


def part_1(input_string):
    bricks = list(map(lambda b: (tuple(map(int, b[0].split(','))), tuple(map(int, b[1].split(',')))), re.findall(r"([\d,]+)~([\d,]+)", input_string)))
    bricks.sort(key=lambda b:min(b[0][2], b[1][2]))
    settled_bricks = [b for b in bricks if min(b[0][2], b[1][2]) == 1]
    unsettled_bricks = [b for b in bricks if min(b[0][2], b[1][2]) > 1]
    while unsettled_bricks:
        cur_brick = unsettled_bricks.pop(0)
        settle_brick(settled_bricks, cur_brick)
    result = 0
    for i in range(len(settled_bricks)):
        nex_bricks = settled_bricks[:i] + settled_bricks[i+1:]
        settled_height = max(settled_bricks[i][0][2], settled_bricks[i][1][2])
        new_settled_bricks = [b for b in nex_bricks if min(b[0][2], b[1][2]) <= settled_height]
        new_unsettled_bricks = [b for b in nex_bricks if min(b[0][2], b[1][2]) > settled_height]
        falling = False
        while new_unsettled_bricks:
            cur_brick = new_unsettled_bricks.pop(0)
            settle_brick(new_settled_bricks, cur_brick)
            if new_settled_bricks[-1] != cur_brick:
                falling = True
                break
        if not falling:
            result += 1
    print(result)


def part_2(input_string):
    bricks = list(map(lambda b: (tuple(map(int, b[0].split(','))), tuple(map(int, b[1].split(',')))), re.findall(r"([\d,]+)~([\d,]+)", input_string)))
    bricks.sort(key=lambda b:min(b[0][2], b[1][2]))
    settled_bricks = [b for b in bricks if min(b[0][2], b[1][2]) == 1]
    unsettled_bricks = [b for b in bricks if min(b[0][2], b[1][2]) > 1]
    while unsettled_bricks:
        cur_brick = unsettled_bricks.pop(0)
        settle_brick(settled_bricks, cur_brick)
    result = 0
    for i in range(len(settled_bricks)):
        nex_bricks = settled_bricks[:i] + settled_bricks[i+1:]
        settled_height = max(settled_bricks[i][0][2], settled_bricks[i][1][2])
        new_settled_bricks = [b for b in nex_bricks if min(b[0][2], b[1][2]) <= settled_height]
        new_unsettled_bricks = [b for b in nex_bricks if min(b[0][2], b[1][2]) > settled_height]
        while new_unsettled_bricks:
            cur_brick = new_unsettled_bricks.pop(0)
            settle_brick(new_settled_bricks, cur_brick)
            if new_settled_bricks[-1] != cur_brick:
                result += 1
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_22.txt', 'r')
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
