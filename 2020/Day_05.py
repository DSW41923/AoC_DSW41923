import sys
import getopt

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_05.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_05.py [-h | --help]')
            print('Advent of Code 2020 Day 05')
            sys.exit()

    file_input = open('Input_05.txt', 'r')
    raw_data = file_input.readlines()
    boardingpass_data = []
    for data in raw_data:
        data = data.replace('\n', '').replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1')
        row_number = int(data[:5], 2)
        column_number = int(data[-3:], 2)
        seat_id = int(data, 2)
        boardingpass_data.append({
            'ID': seat_id,
            'row': row_number,
            'column': column_number
        })
    print(max(boardingpass_data, key=lambda a: a['ID'])['ID'])

    max_id = max(boardingpass_data, key=lambda a: a['ID'])['ID']
    min_id = min(boardingpass_data, key=lambda a: a['ID'])['ID']
    all_id = [b['ID'] for b in boardingpass_data]

    for x in range(max_id):
        if x >= min_id:
            if x not in all_id and (x - 1) in all_id and (x + 1) in all_id:
                print(x)


if __name__ == "__main__":
    main(sys.argv[1:])