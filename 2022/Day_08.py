import argparse


def part_1(input_string):
    tree_map_strings = input_string.split('\n')
    tree_map = [list(map(int, list(tree_map_string))) for tree_map_string in tree_map_strings]
    visible_tree_count = 2 * (len(tree_map) + len(tree_map[0])) - 4
    for x in range(1, len(tree_map) - 1):
        for y in range(1, len(tree_map[x]) - 1):
            up_trees = [tree_map[i][y] for i in range(x)]
            down_trees = [tree_map[i][y] for i in range(x + 1, len(tree_map))]
            left_trees = [tree_map[x][j] for j in range(y)]
            right_trees = [tree_map[x][j] for j in range(y + 1, len(tree_map[x]))]
            if all(t < tree_map[x][y] for t in up_trees):
                visible_tree_count += 1
                continue
            if all(t < tree_map[x][y] for t in down_trees):
                visible_tree_count += 1
                continue
            if all(t < tree_map[x][y] for t in left_trees):
                visible_tree_count += 1
                continue
            if all(t < tree_map[x][y] for t in right_trees):
                visible_tree_count += 1
                continue
    print(visible_tree_count)


def part_2(input_string):
    tree_map_strings = input_string.split('\n')
    tree_map = [list(map(int, list(tree_map_string))) for tree_map_string in tree_map_strings]
    max_scenic_score = 0
    for x in range(1, len(tree_map) - 1):
        for y in range(1, len(tree_map[x]) - 1):
            scenic_score = 1
            up_trees = [tree_map[i][y] for i in range(x)]
            down_trees = [tree_map[i][y] for i in range(x + 1, len(tree_map))]
            left_trees = [tree_map[x][j] for j in range(y)]
            right_trees = [tree_map[x][j] for j in range(y + 1, len(tree_map[x]))]
            for t, tree in enumerate(reversed(up_trees)):
                if tree >= tree_map[x][y]:
                    scenic_score *= (t + 1)
                    break
                if t == len(up_trees) - 1:
                    scenic_score *= t + 1
            for t, tree in enumerate(down_trees):
                if tree >= tree_map[x][y]:
                    scenic_score *= (t + 1)
                    break
                if t == len(down_trees) - 1:
                    scenic_score *= t + 1
            for t, tree in enumerate(reversed(left_trees)):
                if tree >= tree_map[x][y]:
                    scenic_score *= (t + 1)
                    break
                if t == len(left_trees) - 1:
                    scenic_score *= t + 1
            for t, tree in enumerate(right_trees):
                if tree >= tree_map[x][y]:
                    scenic_score *= (t + 1)
                    break
                if t == len(right_trees) - 1:
                    scenic_score *= t + 1
            max_scenic_score = max(max_scenic_score, scenic_score)
    print(max_scenic_score)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2022/Input_08.txt', 'r')
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
