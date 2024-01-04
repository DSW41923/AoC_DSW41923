import argparse
import re


def parse_monkey_data(input_string):
    monkeys = {}
    for monkey_id, items, operation, test, true_des, false_des in re.findall(r'Monkey (\d+):\n[\w ]+items: ([\d ,]+)\n +Operation: new = ([old *+\-\d]+)\n +Test:[\w ]+by (\d+)\n[\w ]+true:[\w ]+(\d+)\n[\w ]+false:[\w ]+(\d+)', input_string):
        monkeys.update({
            monkey_id: {
            'items': list(map(int, items.split(', '))),
            'operation': operation,
            'test': 'new%' + test,
            'true_des': true_des,
            'false_des': false_des,
            'inspection_count': 0}})
    return monkeys


def part_1(input_string):
    monkeys = parse_monkey_data(input_string)
    for _ in range(20):
        for i in range(len(monkeys)):
            inspecting = str(i)
            for j in range(len(monkeys[inspecting]['items'])):
                old = monkeys[inspecting]['items'][j]
                new = eval(monkeys[inspecting]['operation'])
                monkeys[inspecting]['inspection_count'] += 1 
                new //= 3
                if eval(monkeys[inspecting]['test']):
                    monkeys[monkeys[inspecting]['false_des']]['items'].append(new)
                    continue
                monkeys[monkeys[inspecting]['true_des']]['items'].append(new)
            monkeys[inspecting]['items'] = []
    inspection_counts = sorted([m['inspection_count'] for m in monkeys.values()], reverse=True)
    print(inspection_counts[0] * inspection_counts[1])


def part_2(input_string):
    monkeys = parse_monkey_data(input_string)
    ultimate_test = 1
    for test in [m['test'] for m in monkeys.values()]:
        ultimate_test *= int(test.split('%')[-1])
    for _ in range(10000):
        for i in range(len(monkeys)):
            inspecting = str(i)
            for j in range(len(monkeys[inspecting]['items'])):
                old = monkeys[inspecting]['items'][j]
                new = eval(monkeys[inspecting]['operation'])
                monkeys[inspecting]['inspection_count'] += 1 
                new %= ultimate_test
                if eval(monkeys[inspecting]['test']):
                    monkeys[monkeys[inspecting]['false_des']]['items'].append(new)
                    continue
                monkeys[monkeys[inspecting]['true_des']]['items'].append(new)
            monkeys[inspecting]['items'] = []
    inspection_counts = sorted([m['inspection_count'] for m in monkeys.values()], reverse=True)
    print(inspection_counts[0] * inspection_counts[1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2022/Input_11.txt', 'r')
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

