import sys
import getopt
import re

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_21.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_21.py [-h | --help]')
            print('Advent of Code 2020 Day 21')
            sys.exit()

    file_input = open('inputs/2020/Input_21.txt', 'r')
    input_strings = file_input.read()
    file_input.close()
    allergen_in_foods = {}
    all_allergens = []
    all_ingredients = []
    for ingredients, allergens_contained in re.findall(r'([\w ]+) \(contains ([\w, ]+)\)', input_strings):
        ingredients = ingredients.split(' ')
        all_ingredients.extend(ingredients)
        all_allergens.extend(allergens_contained.split(', '))
        allergen_in_foods.update({allergens_contained: allergen_in_foods.get(allergens_contained, []) + ingredients})

    all_allergens = list(set(all_allergens))
    all_ingredients = list(set(all_ingredients))

    allergen_in_ingredient = {}
    for allergen in all_allergens:
        allergen_ingredients = []
        for allergen_contained, ingredients in allergen_in_foods.items():
            allergens = allergen_contained.split(', ')
            if allergen in allergens:
                if not allergen_ingredients:
                    allergen_ingredients = ingredients
                else:
                    allergen_ingredients = list(set(allergen_ingredients) & set(ingredients))
        allergen_in_ingredient.update({
            allergen: allergen_ingredients
        })

    ingredients_with_allergen = list(set(' '.join([' '.join(a) for a in allergen_in_ingredient.values()]).split(' ')))

    all_ingredients_appearance = ' '.join([' '.join(a) for a in allergen_in_foods.values()]).split(' ')
    no_allergen_ingredients_appear_count = 0
    for ingredient in all_ingredients:
        if ingredient not in ingredients_with_allergen:
            no_allergen_ingredients_appear_count += all_ingredients_appearance.count(ingredient)
    print(no_allergen_ingredients_appear_count)

    allergen_ingredient_name = {}
    while any(len(n) > 0 for n in allergen_in_ingredient.values()):
        for allergen, possible_ingredients in allergen_in_ingredient.items():
            if len(possible_ingredients) == 1:
                allergen_ingredient_name.update({allergen: possible_ingredients[0]})
                break

        for ingrdients in allergen_ingredient_name.values():
            for allergen in all_allergens:
                if ingrdients in allergen_in_ingredient[allergen]:
                    allergen_in_ingredient[allergen].remove(ingrdients)

    all_allergens.sort()
    canonical_dangerous_ingredient_list = ','.join(allergen_ingredient_name[allergen] for allergen in all_allergens)
    print(canonical_dangerous_ingredient_list)


if __name__ == "__main__":
    main(sys.argv[1:])