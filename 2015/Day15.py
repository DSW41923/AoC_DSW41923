import re
import itertools

input_string = open('../AoC_Inputs/2015/input-D15.txt', 'r')
ingredient_data_string = input_string.read()
input_string.close()
ingredient_data = []
for ingredient, capacity, durability, flavor, texture, calories in \
        re.findall(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)',
                   ingredient_data_string):
    ingredient_data.append({
        'name': ingredient,
        'capacity': int(capacity),
        'durability': int(durability),
        'flavor': int(flavor),
        'texture': int(texture),
        'calories': int(calories)})

def get_property_score(data, teaspoon_count, cookie_property):
    property_score = 0
    for d, t in zip(data, teaspoon_count):
        property_score += t * d.get(cookie_property)
    if property_score < 0:
        return 0
    return property_score

focus_properties = ['capacity', 'durability', 'flavor', 'texture']
total_teaspoons = 100
all_possible_teaspoons = list(itertools.combinations(
    range(total_teaspoons + len(focus_properties) - 1), len(focus_properties) - 1))
max_score = 0
for teaspoons in all_possible_teaspoons:
    teaspoons = [0] + list(teaspoons) + [total_teaspoons + len(focus_properties) - 1]
    teaspoons_per_ingredient = [teaspoons[1] - teaspoons[0]] + \
                               [teaspoons[i] - teaspoons[i - 1] - 1 for i in range(2, len(teaspoons))]
    total_score = 1
    for focus_property in focus_properties:
        total_score *= get_property_score(ingredient_data, teaspoons_per_ingredient, focus_property)
    if total_score > max_score:
        max_score = total_score
print(max_score)

new_max_score = 0
for teaspoons in all_possible_teaspoons:
    teaspoons = [0] + list(teaspoons) + [total_teaspoons + len(focus_properties) - 1]
    teaspoons_per_ingredient = [teaspoons[1] - teaspoons[0]]
    teaspoons_per_ingredient.extend([teaspoons[i] - teaspoons[i - 1] - 1 for i in range(2, len(teaspoons))])
    total_score = 1
    for focus_property in focus_properties:
        total_score *= get_property_score(ingredient_data, teaspoons_per_ingredient, focus_property)
    calories = get_property_score(ingredient_data, teaspoons_per_ingredient, 'calories')
    if total_score > new_max_score and calories == 500:
        new_max_score = total_score
print(new_max_score)