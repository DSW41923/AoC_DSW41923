import argparse

from Day_13 import IntCodeComputer
from math import inf


def in_beam(x, y, program):
    computer = IntCodeComputer(program)
    computer.add_input(x)
    computer.add_input(y)
    computer.run()
    outputs = computer.get_outputs()
    return outputs[-1] == 1

def get_in_beam_count(x_base, x_range, y_base, y_range, program):
    affected = []
    for i in range(x_range):
        for j in range(y_range):
            if in_beam(x_base+i, y_base+j, program):
                affected.append((x_base+i, y_base+j))
    return affected


def part_1(input_string):
    print(len(get_in_beam_count(0, 50, 0, 50, input_string)))


def part_2(input_string):
    x = y = 0
    result = inf
    while result > 100000000:
        width = 0
        while in_beam(x+width, y, input_string):
            width += 1
        if width >= 100:
            # print(x, y, width)
            for i in range(width-100, -1, -1):
                affected = get_in_beam_count(x+i, 1, y, 100, input_string)
                # print(x+i, y, len(affected))
                if len(affected) >= 100:
                    result = min(result, 10000*(x+i)+y)
                else:
                    break
            if result > 100000000:
                x += (width-99)
                y += 1
        else:
            # print(x, y, width)
            y += 1
            while not in_beam(x, y, input_string):
                moved = False
                for i in range(5):
                    if in_beam(x+i, y, input_string):
                        x += i
                        moved = True
                        break
                if not moved:
                    y += 1
            while in_beam(x-1, y, input_string):
                x -= 1
        # height = 0
        # while in_beam(x, y+height, input_string):
        #     height += 1
        # if height >= 100:
        #     print(x, y, height)
        #     for i in range(height-100, -1, -1):
        #         affected = get_in_beam_count(x, 100, y+i, 1, input_string)
        #         print(x, y+i, len(affected))
        #         if len(affected) >= 100:
        #             result = min(result, 10000*x+y+i)
        #         else:
        #             break
        #     if result > 100000000:
        #         y += (height-99)
        # else:
        #     print(x, y, height)
        #     x += 1
        #     while not in_beam(x, y, input_string):
        #         moved = False
        #         for i in range(10):
        #             if in_beam(x, y+i, input_string):
        #                 y += i
        #                 moved = True
        #                 break
        #         if not moved:
        #             x += 1
        #     while in_beam(x, y-1, input_string):
        #         y -= 1
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_19.txt', 'r')
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
