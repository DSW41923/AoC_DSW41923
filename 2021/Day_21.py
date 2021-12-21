import argparse


def part_1(player_1_start, player_2_start):
    player_1_pos = player_1_start - 1
    player_2_pos = player_2_start - 1
    player_1_score, player_2_score = 0, 0
    die_times = 0
    while True:
        player_movement = sum([(d % 100) + 1 for d in range(die_times, die_times+3)])
        die_times += 3

        if die_times % 2 == 1:
            player_1_pos = (player_1_pos + player_movement) % 10
            player_1_score += (player_1_pos + 1)
            if player_1_score >= 1000:
                print(player_2_score * die_times)
                break

        if die_times % 2 == 0:
            player_2_pos = (player_2_pos + player_movement) % 10
            player_2_score += (player_2_pos + 1)
            if player_2_score >= 1000:
                print(player_1_score * die_times)
                break


def part_2(player_1_start, player_2_start):
    playing_games = [{
        'player_1': {'pos': player_1_start - 1, 'score': 0},
        'player_2': {'pos': player_2_start - 1, 'score': 0},
        'round': 0,
        'count': 1
    }]
    die_result_count = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    player_1_winning_count, player_2_winning_count = 0, 0
    while playing_games:
        new_playing_games = []
        for game in playing_games:
            for player_movement in [3, 4, 5, 6, 7, 8, 9]:
                round_count = game['round'] + 1
                new_playing_game = {
                    'round': round_count,
                    'count': game['count'] * die_result_count[player_movement]
                }

                if round_count % 2 == 1:
                    player_1_pos = (game['player_1']['pos'] + player_movement) % 10
                    player_1_score = (game['player_1']['score'] + player_1_pos + 1)
                    if player_1_score >= 21:
                        player_1_winning_count += new_playing_game['count']
                        continue
                    new_playing_game.update({
                        'player_1': {'pos': player_1_pos, 'score': player_1_score},
                        'player_2': game['player_2']
                    })

                if round_count % 2 == 0:
                    player_2_pos = (game['player_2']['pos'] + player_movement) % 10
                    player_2_score = (game['player_2']['score'] + player_2_pos + 1)
                    if player_2_score >= 21:
                        player_2_winning_count += new_playing_game['count']
                        continue
                    new_playing_game.update({
                        'player_1': game['player_1'],
                        'player_2': {'pos': player_2_pos, 'score': player_2_score},
                    })

                new_playing_games.append(new_playing_game)

        playing_games = new_playing_games

    print(max(player_1_winning_count, player_2_winning_count))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    player_1_start, player_2_start = 4, 6

    if args.part == '1':
        part_1(player_1_start, player_2_start)
    elif args.part == '2':
        part_2(player_1_start, player_2_start)
    else:
        part_1(player_1_start, player_2_start)
        part_2(player_1_start, player_2_start)


if __name__ == "__main__":
    main()
