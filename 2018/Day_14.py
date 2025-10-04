import argparse


def part_1(input_string):
    recipes_number = int(input_string)
    recipes = [3, 7]
    cur_0, cur_1 = 0, 1
    while len(recipes) < (recipes_number+10):
        new_recipes = recipes[cur_0] + recipes[cur_1]
        recipes.extend(list(map(int, list(str(new_recipes)))))
        cur_0 += (1+recipes[cur_0])
        cur_0 %= len(recipes)
        cur_1 += (1+recipes[cur_1])
        cur_1 %= len(recipes)
    print(''.join(list(map(str, recipes[recipes_number:recipes_number+10]))))


def part_2(input_string):
    recipes = "37"
    cur_0, cur_1 = 0, 1
    while input_string not in [recipes[-len(input_string)-1:-1], recipes[-len(input_string):]]:
        cur_0_recipe, cur_1_recipe = int(recipes[cur_0]), int(recipes[cur_1])
        new_recipes = cur_0_recipe + cur_1_recipe
        recipes += str(new_recipes)
        cur_0 += (1+cur_0_recipe)
        cur_0 %= len(recipes)
        cur_1 += (1+cur_1_recipe)
        cur_1 %= len(recipes)
    print(recipes.index(input_string))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_14.txt', 'r')
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
