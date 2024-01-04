import sys
import getopt
import copy

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_11.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_11.py [-h | --help]')
            print('Advent of Code 2020 Day 11')
            sys.exit()

    file_input = open('inputs/2020/Input_11.txt', 'r')
    seat_strings = file_input.readlines()
    file_input.close()
    seat_map = []
    for x in seat_strings:
        seat_map.append(list(x.replace('\n', '')))

    old_seatmap = copy.deepcopy(seat_map)
    new_seatmap = []
    while new_seatmap != old_seatmap:
        if len(new_seatmap) == 0:
            new_seatmap = copy.deepcopy(old_seatmap)
        else:
            old_seatmap = copy.deepcopy(new_seatmap)
        for y, y_seats in enumerate(old_seatmap):
            for x, seat in enumerate(y_seats):
                if seat != '.':
                    def get_adjacent_seats(a, b, seats):
                        adj_seats = []
                        if a > 0:
                            adj_seats.append(seats[b][a-1])
                        if a < len(seats[0]) - 1:
                            adj_seats.append(seats[b][a+1])

                        if b > 0:
                            adj_seats += seats[b-1][max(a-1, 0):min(a+2, len(seats[0]))]
                        if b < len(seats) - 1:
                            adj_seats += seats[b+1][max(a-1, 0):min(a+2, len(seats[0]))]

                        return adj_seats

                    adjacent_seats = get_adjacent_seats(x, y, old_seatmap)
                    if sum(s == '#' for s in adjacent_seats) == 0 and seat == 'L':
                        new_seatmap[y][x] = '#'
                    elif sum(s == '#' for s in adjacent_seats) >= 4 and seat == '#':
                        new_seatmap[y][x] = 'L'

    print(sum(list(map(lambda s: s.count('#'), new_seatmap))))

    def get_visible_seats(a, b, seats):
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        vis_seats = []

        for d_x, d_y in directions:
            m, n = a, b
            while 0 <= m < len(seats[0]) and 0 <= n < len(seats):
                m, n = m + d_x, n + d_y
                try:
                    if seats[n][m] != '.' and 0 <= m < len(seats[0]) and 0 <= n < len(seats):
                        vis_seats.append((m, n))
                        break
                except IndexError:
                    continue

        return vis_seats

    visible_seatmap = copy.deepcopy(seat_map)
    for y in range(len(seat_map)):
        for x in range(len(seat_map[0])):
            if seat_map[y][x] == '.':
                visible_seatmap[y][x] = []
            else:
                visible_seatmap[y][x] = get_visible_seats(x, y, seat_map)

    old_seatmap = copy.deepcopy(seat_map)
    new_seatmap = []
    while new_seatmap != old_seatmap:
        if len(new_seatmap) == 0:
            new_seatmap = copy.deepcopy(old_seatmap)
        else:
            old_seatmap = copy.deepcopy(new_seatmap)
        for y, y_seats in enumerate(old_seatmap):
            for x, seat in enumerate(y_seats):
                if seat != '.':
                    visible_seats = [old_seatmap[y][x] for x, y in visible_seatmap[y][x]]
                    if sum(s == '#' for s in visible_seats) == 0 and seat == 'L':
                        new_seatmap[y][x] = '#'
                    elif sum(s == '#' for s in visible_seats) >= 5 and seat == '#':
                        new_seatmap[y][x] = 'L'

    print(sum(list(map(lambda s: s.count('#'), new_seatmap))))

if __name__ == "__main__":
    main(sys.argv[1:])