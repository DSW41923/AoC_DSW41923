import re

input_string = open('inputs/2015/input-D16.txt', 'r')
aunt_data_string = input_string.read()
input_string.close()
ideal_aunt_data = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}
aunt_data = []
for aunt_number, aunt_property in re.findall(r'(Sue \d+): ([\w: \d,]+)', aunt_data_string):
    new_aunt_data = {'name': aunt_number}
    ideal_aunt_score = 0
    for property_name, number in re.findall(r'(\w+): (\d+)', aunt_property):
        new_aunt_data.update({
            property_name: int(number)
        })
        if new_aunt_data[property_name] == ideal_aunt_data[property_name]:
            ideal_aunt_score += 1
    new_aunt_data.update({
        'score': ideal_aunt_score
    })
    aunt_data.append(new_aunt_data)
print(max(aunt_data, key= lambda a: a['score']))

for aunt in aunt_data:
    ideal_aunt_score = 0
    for property_name in aunt.keys():
        if property_name not in ['score', 'name']:
            ideal_property_amount = ideal_aunt_data[property_name]
            if property_name in ['cats', 'trees'] and ideal_property_amount < aunt[property_name]:
                ideal_aunt_score += 1
            elif property_name in ['pomeranians', 'goldfish'] and ideal_property_amount > aunt[property_name]:
                ideal_aunt_score += 1
            elif aunt[property_name] == ideal_property_amount:
                ideal_aunt_score += 1
            else:
                ideal_aunt_score = -100
    aunt.update({
        'new_score': ideal_aunt_score
    })
print(max(aunt_data, key= lambda a: a['new_score']))