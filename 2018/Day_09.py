import argparse
import re

from collections import deque


def part_1(input_string):
    players, marbles = tuple(map(int, re.findall(r"(\d+)", input_string)))
    player_scores = [0 for _ in range(players)]
    cur = None
    marble_status = []
    for i in range(marbles+1):
        if not marble_status:
            marble_status.append(i)
            cur = 0
            continue

        if len(marble_status) == 1:
            marble_status.append(i)
            cur = 1
            continue

        if (i % 23) == 0:
            player_scores[i % players] += i
            cur -= 7
            cur %= len(marble_status)
            player_scores[i % players] += marble_status.pop(cur)
            continue
        
        cur += 2
        if cur > len(marble_status):
            cur %= len(marble_status)
        marble_status.insert(cur, i)
    print(max(player_scores))


def part_2(input_string):
    players, marbles = tuple(map(int, re.findall(r"(\d+)", input_string)))
    marbles *= 100
    player_scores = [0 for _ in range(players)]
    marble_status = deque([0])
    for i in range(1, marbles+1):
        if i % 23 == 0:
            marble_status.rotate(7)
            player_scores[i % players] += (i + marble_status.pop())
            marble_status.rotate(-1)
        else:
            marble_status.rotate(-1)
            marble_status.append(i)

    print(max(player_scores))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_09.txt', 'r')
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
