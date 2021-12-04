import argparse
import re


def get_boards(board_data):
    boards = []
    new_board = []
    for row_data in board_data:
        if row_data == '':
            if new_board:
                boards.append(new_board)
                new_board = []
            continue

        new_board.append(re.split(r'\s+', row_data.lstrip()))

    return boards


def is_winning_board(board):
    for i, row in enumerate(board):
        if all([n == '' for n in row]):
            return True
    for j in range(len(board[0])):
        if all([n == '' for n in [board[i][j] for i in range(len(board))]]):
            return True

    return False


def get_score(board, number):
    unmarked_sum = 0
    for r in board:
        unmarked_sum += sum([int(n) for n in r if n.isdigit()])
    return unmarked_sum * int(number)


def part_1(input_string):
    input_string_row = input_string.split('\n')
    calling_numbers = input_string_row[0].split(',')
    boards = get_boards(input_string_row[1:])
    for number in calling_numbers:
        for board in boards:
            for i, row in enumerate(board):
                for j, num in enumerate(row):
                    if num == number:
                        board[i][j] = ''

        for board in boards:
            if is_winning_board(board):
                print(get_score(board, number))
                return


def part_2(input_string):
    input_string_row = input_string.split('\n')
    calling_numbers = input_string_row[0].split(',')
    boards = get_boards(input_string_row[1:])
    for number in calling_numbers:
        for board in boards:
            for i, row in enumerate(board):
                for j, num in enumerate(row):
                    if num == number:
                        board[i][j] = ''

        won_boards = []
        for board in boards:
            if is_winning_board(board):
                if len(boards) == 1:
                    print(get_score(board, number))
                    return

                won_boards.append(board)

        boards = [board for board in boards if board not in won_boards]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_04.txt', 'r')
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
