import argparse

from Day_13 import IntCodeComputer


def part_1(input_string):
    computers = [{
        'machine': IntCodeComputer(input_string),
        'incoming_packets': []
    } for _ in range(50)]
    for i, computer in enumerate(computers):
        computer['machine'].add_input(i)
    while True:
        for i, computer in enumerate(computers):
            if not computer['incoming_packets']:
                computer['machine'].add_input(-1)
            else:
                for p in computer['incoming_packets']:
                    computer['machine'].add_input(p)
                computer['incoming_packets'] = []
            computer['machine'].run()
            outputs = computer['machine'].get_outputs()
            # print(i, computer, outputs)
            for j in range(0, len(outputs), 3):
                des, x, y = outputs[j:j+3]
                if des == 255:
                    print(y)
                    return
                computers[des]['incoming_packets'].extend([x, y])
            computer['machine'].clear_outputs()


def part_2(input_string):
    computers = [{
        'machine': IntCodeComputer(input_string),
        'incoming_packets': []
    } for _ in range(50)]
    nat = {
        'machine': IntCodeComputer(input_string),
        'incoming_packets': []
    }
    for i, computer in enumerate(computers):
        computer['machine'].add_input(i)
    idle_count = 0
    result = None
    while True:
        for i, computer in enumerate(computers):
            if not computer['incoming_packets']:
                computer['machine'].add_input(-1)
            else:
                for p in computer['incoming_packets']:
                    computer['machine'].add_input(p)
                computer['incoming_packets'] = []
            computer['machine'].run()
            outputs = computer['machine'].get_outputs()
            # print(i, computer, outputs)
            for j in range(0, len(outputs), 3):
                des, x, y = outputs[j:j+3]
                if des == 255:
                    nat['incoming_packets'] = [x, y]
                    continue
                computers[des]['incoming_packets'].extend([x, y])
            computer['machine'].clear_outputs()

        if all([len(c['incoming_packets']) == 0 for c in computers]):
            idle_count += 1
        else:
            idle_count = 0

        # print(idle_count, nat)
        if idle_count > 100:
            computers[0]['incoming_packets'].extend(nat['incoming_packets'])
            if result == nat['incoming_packets'][1]:
                print(result)
                break
            result = nat['incoming_packets'][1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_23.txt', 'r')
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
