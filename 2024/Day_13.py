import argparse
import re


def part_1(input_string):
    result = 0
    for a_x, a_y, b_x, b_y, prize_x, prize_y in re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", input_string):
        a_x, a_y, b_x, b_y, prize_x, prize_y = tuple(map(int, [a_x, a_y, b_x, b_y, prize_x, prize_y]))
        # Solve
        # a_x*a+b_x*b=prize_x
        # a_y*a+b_y*b=prize_y
        delta = a_x*b_y-b_x*a_y
        if delta != 0:
            a = (prize_x*b_y-b_x*prize_y)/delta
            b = (a_x*prize_y-prize_x*a_y)/delta
            if int(a) == a and int(b) == b:
                assert a <= 100 and b <= 100
                result += int(3*a+b)
    print(result)



def part_2(input_string):
    result = 0
    for a_x, a_y, b_x, b_y, prize_x, prize_y in re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", input_string):
        a_x, a_y, b_x, b_y, prize_x, prize_y = tuple(map(int, [a_x, a_y, b_x, b_y, prize_x, prize_y]))
        # Solve
        # a_x*a+b_x*b=prize_x
        # a_y*a+b_y*b=prize_y
        prize_x += 10000000000000
        prize_y += 10000000000000
        delta = a_x*b_y-b_x*a_y
        if delta != 0:
            a = (prize_x*b_y-b_x*prize_y)/delta
            b = (a_x*prize_y-prize_x*a_y)/delta
            if int(a) == a and int(b) == b:
                result += int(3*a+b)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_13.txt', 'r')
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
