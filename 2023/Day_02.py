import argparse
import re


def part_1(input_string):
    games = []
    for game_id, game_sets in re.findall(r"Game (\d+): ([\d;, redgrnblu]+)", input_string):
        game = {'id': int(game_id), 'blue': 0, 'red': 0, 'green': 0}
        for color in game.keys():
            if color != 'id':
                counts = list(map(int, re.findall(r"(\d+) "+color, game_sets)))
                game[color] = max(counts)
        games.append(game)
    result = 0
    for game in games:
        if game['red'] <= 12 and game['green'] <= 13 and game['blue'] <= 14:
            result += game['id']
    print(result)


def part_2(input_string):
    result = 0
    colors = ["blue", "red", "green"]
    for game_sets in re.findall(r"Game \d+: ([\d;, redgrnblu]+)", input_string):
        game_result = 1
        for color in colors:
            if color != 'id':
                counts = list(map(int, re.findall(r"(\d+) "+color, game_sets)))
                game_result *= max(counts)
        result += game_result
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_02.txt', 'r')
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
