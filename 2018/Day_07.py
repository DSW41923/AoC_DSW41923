import argparse
import re

from string import ascii_uppercase


def get_steps_data(input_string):
    steps_order = {}
    all_steps = set()
    for step_a, step_b in re.findall(r"Step (\w) must be finished before step (\w) can begin.", input_string):
        if step_b not in steps_order:
            steps_order[step_b] = []
        steps_order[step_b].append(step_a)
        all_steps.add(step_a)
        all_steps.add(step_b)
    return steps_order, all_steps


def part_1(input_string):
    steps_order, all_steps = get_steps_data(input_string)

    traversed = []
    next_steps = []
    while all_steps:
        if not traversed:
            for step in all_steps:
                if step not in steps_order:
                    next_steps.append(step)
        for step, pre in steps_order.items():
            if all([s in traversed for s in pre]) and step not in traversed:
                next_steps.append(step)
        next_steps = list(set(next_steps))
        next_steps.sort()
        next_step = next_steps[0]
        all_steps.remove(next_step)
        traversed.append(next_step)
        next_steps = next_steps[1:]

    print(''.join(traversed))


def part_2(input_string):
    steps_order, all_steps = get_steps_data(input_string)

    traversed = []
    workers = [('', 0) for _ in range(5)]
    next_steps = []
    seconds = 0
    while all_steps:
        if any([worker[1] != 0 for worker in workers]):
            for i in range(5):
                if workers[i][1] > 1:
                    workers[i] = (workers[i][0], workers[i][1]-1)
                elif workers[i][1] == 1:
                    traversed.append(workers[i][0])
                    workers[i] = ('', 0)

        if any([worker[1] == 0 for worker in workers]):
            if not traversed:
                if all([worker[0] == '' for worker in workers]):
                    for step in all_steps:
                        if step not in steps_order:
                            next_steps.append(step)
            for step, pre in steps_order.items():
                if all([s in traversed for s in pre]) and step not in traversed and step not in [worker[0] for worker in workers]:
                    next_steps.append(step)
            next_steps = list(set(next_steps))
            for next_step in next_steps:
                for i in range(5):
                    if workers[i][0] == '':
                        workers[i] = (next_step, 61+ascii_uppercase.index(next_step))
                        all_steps.remove(next_step)
                        break
            for worker in workers:
                if worker[0] in next_steps:
                    next_steps.remove(worker[0])

        seconds += 1

    print(seconds+max([worker[1] for worker in workers])-1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_07.txt', 'r')
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
