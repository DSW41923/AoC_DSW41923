import argparse


def part_1(input_string):
    lines = input_string.split('\n')
    score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in lines:
        chars = []
        for char in line:
            if char in ['(', '[', '{', '<']:
                chars.append(char)
                continue

            if char == ')' and chars[-1] == '(':
                chars.pop()
                continue

            if char == ']' and chars[-1] == '[':
                chars.pop()
                continue

            if char == '}' and chars[-1] == '{':
                chars.pop()
                continue

            if char == '>' and chars[-1] == '<':
                chars.pop()
                continue

            score += score_table[char]
            break

    print(score)


def part_2(input_string):
    lines = input_string.split('\n')
    scores = []
    for line in lines:
        chars = []
        is_corrupted = False
        for char in line:
            if char in ['(', '[', '{', '<']:
                chars.append(char)
                continue

            if char == ')' and chars[-1] == '(':
                chars.pop()
                continue

            if char == ']' and chars[-1] == '[':
                chars.pop()
                continue

            if char == '}' and chars[-1] == '{':
                chars.pop()
                continue

            if char == '>' and chars[-1] == '<':
                chars.pop()
                continue

            is_corrupted = True
            break

        if not is_corrupted:
            chars = ''.join(reversed(chars)).replace('(', '1').replace('[', '2').replace('{', '3').replace('<', '4')
            scores.append(int(chars, 5))

    scores.sort()
    print(scores[len(scores) // 2])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_10.txt', 'r')
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
