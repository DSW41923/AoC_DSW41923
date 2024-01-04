import argparse
import string


def part_1(input_string):
    dance_moves = input_string.split(',')
    programs = list(string.ascii_lowercase[:16])
    for dance_move in dance_moves:
        if dance_move.startswith('s'):
            spin_size = int(dance_move[1:])
            programs = programs[-spin_size:] + programs[:-spin_size]
            continue

        if dance_move.startswith('x'):
            pos_A, pos_B = list(map(int, dance_move[1:].split('/')))
            programs[pos_A], programs[pos_B] = programs[pos_B], programs[pos_A]
            continue

        if dance_move.startswith('p'):
            program_A, program_B = dance_move[1:].split('/')
            pos_A = programs.index(program_A)
            pos_B = programs.index(program_B)
            programs[pos_A], programs[pos_B] = programs[pos_B], programs[pos_A]
            continue
    print(''.join(programs))


def part_2(input_string):
    dance_moves = input_string.split(',')
    programs = list(string.ascii_lowercase[:16])
    dance_time = 1000000000
    programs_history = []
    for i in range(dance_time):        
        programs_state = ''.join(programs)
        if programs_state in programs_history:
            history_index = programs_history.index(programs_state)
            print(programs_history[history_index + dance_time % (i - history_index)])
            break

        for dance_move in dance_moves:
            if dance_move.startswith('s'):
                spin_size = int(dance_move[1:])
                programs = programs[-spin_size:] + programs[:-spin_size]
                continue

            if dance_move.startswith('x'):
                pos_A, pos_B = list(map(int, dance_move[1:].split('/')))
                programs[pos_A], programs[pos_B] = programs[pos_B], programs[pos_A]
                continue

            if dance_move.startswith('p'):
                program_A, program_B = dance_move[1:].split('/')
                pos_A = programs.index(program_A)
                pos_B = programs.index(program_B)
                programs[pos_A], programs[pos_B] = programs[pos_B], programs[pos_A]
                continue
        programs_history.append(programs_state)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2017/Input_16.txt', 'r')
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
