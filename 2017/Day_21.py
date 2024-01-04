import argparse
import re


def split_by_length(iter, length):
    return [iter[i:i + length] for i in range(0, len(iter), length)]


def part_1(input_string):
    rules = {}
    for before, after in re.findall(r'([./#]+) => ([./#]+)', input_string):
        all_possible_before = [before]
        before = before.split('/')
        for i in range(7):
            before = [''.join([d[-i] for d in before]) for i in range(1, len(before[0]) + 1)]
            all_possible_before.append('/'.join(before))
            if i == 2:
                before.reverse()
        for b in set(all_possible_before):
            rules.update({
                b: after
            })
    pattern = ['.#.', '..#', '###']
    iterations = 5
    for i in range(iterations):
        new_pattern = []
        if len(pattern) % 2 == 0:
            pattern = list(map(lambda p: split_by_length(p, 2), pattern))
            for j in range(0, len(pattern), 2):
                new_grids = []
                for r1, r2 in zip(pattern[j], pattern[j + 1]):
                    new_grids.append(rules['{}/{}'.format(r1, r2)].split('/'))
                for j in range(len(new_grids[0])):
                    new_pattern.append(''.join([new_grid[j] for new_grid in new_grids]))
        elif len(pattern) % 3 == 0:
            pattern = list(map(lambda p: split_by_length(p, 3), pattern))
            for j in range(0, len(pattern), 3):
                new_grids = []
                for r1, r2, r3 in zip(pattern[j], pattern[j + 1], pattern[j + 2]):
                    new_grids.append(rules['{}/{}/{}'.format(r1, r2, r3)].split('/'))
                for j in range(len(new_grids[0])):
                    new_pattern.append(''.join([new_grid[j] for new_grid in new_grids]))
        pattern = new_pattern
    print(sum(list(map(lambda p: p.count('#'), pattern))))


def part_2(input_string):
    rules = {}
    for before, after in re.findall(r'([./#]+) => ([./#]+)', input_string):
        all_possible_before = [before]
        before = before.split('/')
        for i in range(7):
            before = [''.join([d[-i] for d in before]) for i in range(1, len(before[0]) + 1)]
            all_possible_before.append('/'.join(before))
            if i == 2:
                before.reverse()
        for b in set(all_possible_before):
            rules.update({
                b: after
            })
    pattern = ['.#.', '..#', '###']
    iterations = 18
    for i in range(iterations):
        new_pattern = []
        if len(pattern) % 2 == 0:
            pattern = list(map(lambda p: split_by_length(p, 2), pattern))
            for j in range(0, len(pattern), 2):
                new_grids = []
                for r1, r2 in zip(pattern[j], pattern[j + 1]):
                    new_grids.append(rules['{}/{}'.format(r1, r2)].split('/'))
                for j in range(len(new_grids[0])):
                    new_pattern.append(''.join([new_grid[j] for new_grid in new_grids]))
        elif len(pattern) % 3 == 0:
            pattern = list(map(lambda p: split_by_length(p, 3), pattern))
            for j in range(0, len(pattern), 3):
                new_grids = []
                for r1, r2, r3 in zip(pattern[j], pattern[j + 1], pattern[j + 2]):
                    new_grids.append(rules['{}/{}/{}'.format(r1, r2, r3)].split('/'))
                for j in range(len(new_grids[0])):
                    new_pattern.append(''.join([new_grid[j] for new_grid in new_grids]))
        pattern = new_pattern
    print(sum(list(map(lambda p: p.count('#'), pattern))))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2017/Input_21.txt', 'r')
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
