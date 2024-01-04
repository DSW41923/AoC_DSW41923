import sys
import getopt
import re

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_22.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_22.py [-h | --help]')
            print('Advent of Code 2020 Day 22')
            sys.exit()

    file_input = open('inputs/2020/Input_22.txt', 'r')
    input_strings = file_input.read()
    file_input.close()
    player1_deck_base = []
    player2_deck_base = []

    for player_id, player_deck in re.findall(r'Player (\d):\n([\d\n]+)', input_strings):
        player_deck = list(map(int, [c for c in player_deck.split('\n') if c]))
        if player_id == '1':
            player1_deck_base = player_deck
        elif player_id == '2':
            player2_deck_base = player_deck

    player1_deck, player2_deck = player1_deck_base[:], player2_deck_base[:]
    while all([player1_deck, player2_deck]):
        player1_play = player1_deck[0]
        player2_play = player2_deck[0]
        player1_deck.remove(player1_play)
        player2_deck.remove(player2_play)
        if player1_play > player2_play:
            player1_deck.extend([player1_play, player2_play])
        elif player2_play > player1_play:
            player2_deck.extend([player2_play, player1_play])
        else:
            print("Unexpected happened!")
            sys.exit()

    def calculate_score(deck1, deck2):
        score = 0
        for i in range(max(len(deck1), len(deck2)), 0, -1):
            if deck1:
                score += i * deck1[-i]

            if deck2:
                score += i * deck2[-i]
        return score

    print(calculate_score(player1_deck, player2_deck))

    def recursive_combat(deck1, deck2, configurations):
        while all([deck1, deck2]):
            if (deck1, deck2) in configurations:
                return '1'
            else:
                configurations.append((deck1[:], deck2[:]))
            player1_played = deck1[0]
            player2_played = deck2[0]
            deck1.remove(player1_played)
            deck2.remove(player2_played)

            if len(deck1) >= player1_played and len(deck2) >= player2_played:
                winner = recursive_combat(deck1[:player1_played], deck2[:player2_played], [])
            else:
                winner = '1' if player1_played > player2_played else '2'

            if winner == '1':
                deck1.extend([player1_played, player2_played])
            elif winner == '2':
                deck2.extend([player2_played, player1_played])
            else:
                print("Unexpected happened!")
                sys.exit()
        if deck1:
            return '1'
        if deck2:
            return '2'

    new_player1_deck, new_player2_deck = player1_deck_base[:], player2_deck_base[:]
    recursive_combat(new_player1_deck, new_player2_deck, [])
    print(calculate_score(new_player1_deck, new_player2_deck))


if __name__ == "__main__":
    main(sys.argv[1:])