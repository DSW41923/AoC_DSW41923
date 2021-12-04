import argparse
import re


def part_1(input_string):
    valid_triangle_count = 0
    for a, b, c in re.findall(r'(\d+)\s+(\d+)\s+(\d+)', input_string):
        a, b, c = int(a), int(b), int(c)
        if (a + b > c) and (b + c > a) and (c + a > b):
            valid_triangle_count += 1
    print("{} of the listed triangles are possible.".format(valid_triangle_count))


def part_2(input_string):
    valid_triangle_count = 0
    for a, d, g, b, e, h, c, f, i in re.findall(r'\s+(\d+)\s+(\d+)\s+(\d+)\n'
                                                r'\s+(\d+)\s+(\d+)\s+(\d+)\n'
                                                r'\s+(\d+)\s+(\d+)\s+(\d+)', input_string):
        a, b, c, d, e, f, g, h, i = tuple(map(int, [a, b, c, d, e, f, g, h, i]))
        if (a + b > c) and (b + c > a) and (c + a > b):
            valid_triangle_count += 1
        if (d + e > f) and (e + f > d) and (f + d > e):
            valid_triangle_count += 1
        if (g + h > i) and (h + i > g) and (i + g > h):
            valid_triangle_count += 1
    print("Actually, {} of the listed triangles are possible.".format(valid_triangle_count))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_03.txt', 'r')
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
