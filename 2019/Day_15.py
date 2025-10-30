import argparse


from Day_13 import IntCodeComputer


def part_1(input_string):
    computer = IntCodeComputer(input_string)
    facing_options = [0, 1j, -1j, -1, 1]
    fronts = [(0, 0, computer)]
    traversed = [0]
    while True:
        new_fronts = []
        for pos, steps, computer in fronts:
            for i in range(1, 5):
                new_pos = pos+facing_options[i]
                if new_pos not in traversed:
                    traversed.append(new_pos)
                    new_steps = steps + 1
                    new_computer = computer.copy()
                    new_computer.add_input(i)
                    new_computer.run()
                    outputs = new_computer.get_outputs()
                    if outputs[-1] == 2:
                        print(new_steps)
                        return
                    elif outputs[-1] == 1:
                        new_fronts.append((new_pos, new_steps, new_computer))
        fronts = new_fronts


def part_2(input_string):
    computer = IntCodeComputer(input_string)
    facing_options = [0, 1j, -1j, -1, 1]
    fronts = [(0, 0, computer)]
    traversed = [0]
    spaces = [0]
    oxygen = None
    while fronts:
        new_fronts = []
        for pos, steps, computer in fronts:
            for i in range(1, 5):
                new_pos = pos+facing_options[i]
                if new_pos not in traversed:
                    traversed.append(new_pos)
                    new_steps = steps + 1
                    new_computer = computer.copy()
                    new_computer.add_input(i)
                    new_computer.run()
                    outputs = new_computer.get_outputs()
                    if outputs[-1] == 2:
                        oxygen = new_pos
                    elif outputs[-1] == 1:
                        spaces.append(new_pos)
                        new_fronts.append((new_pos, new_steps, new_computer))
        fronts = new_fronts
    fronts = [oxygen]
    spreaded = [oxygen]
    time = 0
    while fronts:
        new_fronts = []
        for pos in fronts:
            for i in range(1, 5):
                new_pos = pos+facing_options[i]
                if new_pos in spaces and new_pos not in spreaded:
                    spreaded.append(new_pos)
                    new_fronts.append(new_pos)
        fronts = new_fronts
        if not fronts:
            break
        time += 1
    print(time)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_15.txt', 'r')
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
