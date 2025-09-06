import argparse
import re


def get_claims_data(input_string):
    claims = []
    x_range, y_range = 0, 0
    for id, y, x, width, height in re.findall(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", input_string):
        y, x, width, height = tuple(map(int, (y, x, width, height)))
        if y+width > y_range:
            y_range = y+width
        if x+height > x_range:
            x_range = x+height
        claims.append((id, x, y, height, width))
    return claims, x_range, y_range


def get_filled_area(claims, x_range, y_range):
    area = [[0 for _ in range(y_range)] for _ in range(x_range)]
    for _, x, y, height, width in claims:
        for i in range(height):
            for j in range(width):
                area[x+i][y+j] += 1
    return area


def part_1(input_string):
    claims, x_range, y_range = get_claims_data(input_string)
    area = get_filled_area(claims, x_range, y_range)

    result = 0
    for r in area:
        result += len([c for c in r if c >= 2])
    print(result)


def part_2(input_string):
    claims, x_range, y_range = get_claims_data(input_string)
    area = get_filled_area(claims, x_range, y_range)
    for id, x, y, height, width in claims:
        overlapped = False
        for i in range(height):
            if any([area[x+i][y+j] != 1 for j in range(width)]):
                overlapped = True
                break
        if not overlapped:
            print(id)
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_03.txt', 'r')
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
