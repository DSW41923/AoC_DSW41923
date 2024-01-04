import argparse
import copy


def part_1(input_string):
    state = list(map(list, input_string.splitlines()))
    steps = 0
    while True:
        steps += 1
        print(steps, end='\r')
        step_1_state = copy.deepcopy(state)
        moved_cucumber = []
        for r, row in enumerate(step_1_state):
            for sc, sea_cucumber in enumerate(row):
                dest_sc = (sc + 1) % len(step_1_state[0])
                if sea_cucumber == '>' and state[r][dest_sc] == '.' and (r, sc) not in moved_cucumber:
                    step_1_state[r][sc] = '.'
                    step_1_state[r][dest_sc] = '>'
                    moved_cucumber.append((r, dest_sc))

        new_state = copy.deepcopy(step_1_state)
        for r, row in enumerate(new_state):
            for sc, sea_cucumber in enumerate(row):
                dest_r = (r + 1) % len(new_state)
                if sea_cucumber == 'v' and step_1_state[dest_r][sc] == '.' and (r, sc) not in moved_cucumber:
                    new_state[r][sc] = '.'
                    new_state[dest_r][sc] = 'v'
                    moved_cucumber.append((dest_r, sc))

        if len(moved_cucumber) == 0:
            print(steps)
            break

        state = new_state


def part_2():
    print("Merry Christmas!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2021/Input_25.txt', 'r')
    input_string = file_input.read()
    file_input.close()

    if args.part == '1':
        part_1(input_string)
    elif args.part == '2':
        part_2()
    else:
        part_1(input_string)
        part_2()


if __name__ == "__main__":
    main()
