import argparse

from functools import lru_cache


def count_stones_v1(stones, blinks):
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                stone_str = str(stone)
                l, r = int(stone_str[:len(stone_str) // 2]), int(stone_str[len(stone_str) // 2:])
                new_stones += [l, r]
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)



@lru_cache(maxsize=None)
def count_stones_v2(stones, blinks):
    if blinks == 0:
        return 1

    result = 0
    for stone in stones:
        if stone == 0:
            result += count_stones_v2((1,), blinks-1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            l, r = int(stone_str[:len(stone_str) // 2]), int(stone_str[len(stone_str) // 2:])
            result += count_stones_v2((l,), blinks-1)
            result += count_stones_v2((r,), blinks-1)
        else:
            result += count_stones_v2((stone * 2024,), blinks-1)
    return result


def part_1(input_string):
    stones = list(map(int, input_string.split(' ')))
    print(count_stones_v1(stones, 25))


def part_2(input_string):
    stones = tuple(map(int, input_string.split(' ')))
    print(count_stones_v2(stones, 75))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_11.txt', 'r')
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
