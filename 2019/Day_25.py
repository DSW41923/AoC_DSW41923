import argparse

from Day_13 import IntCodeComputer


def part_1(input_string):
    computer = IntCodeComputer(input_string)
    computer.run()
    outputs = computer.get_outputs()
    for o in outputs:
        print(chr(o), end='')
    outputs = computer.clear_outputs()
    
    while True:
        '''
        easter egg
        space heater
        sand
        mug
        '''
        action = input("Choose one action: 0) Exit 1) Move 2) Take 3) Drop 4) Inventory ")
        if action not in ["0", "1", "2", "3", "4"]:
            continue
        action = int(action)
        command = ""
        if action == 0:
            break
        if action == 1:
            direction = input("Choose direction from NEWS: ")
            direction = direction.lower()
            if direction in ['n', "north"]:
                command = "north\n"
            elif direction in ['e', "east"]:
                command = "east\n"
            elif direction in ['w', "west"]:
                command = "west\n"
            elif direction in ['s', "south"]:
                command = "south\n"
            else:
                print("Invalid direction!!")
                continue
        elif action == 2:
            item = input("Choose one item to take: ")
            command = "take " + item + "\n"
        elif action == 3:
            item = input("Choose one item to drop: ")
            command = "drop " + item + "\n"
        elif action == 4:
            command = "inv\n"

        for i in command:
            computer.add_input(ord(i))

        computer.run()
        outputs = computer.get_outputs()
        for o in outputs:
            if o <= 255:
                print(chr(o), end='')
            else:
                print(o)
        outputs = computer.clear_outputs()


def part_2(input_string):
    print("Merry Christmas!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_25.txt', 'r')
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
