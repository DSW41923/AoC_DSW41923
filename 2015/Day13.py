import itertools

input_string = open('../AoC_Inputs/2015/input-D13.txt', 'r')
happiness_descriptions = input_string.readlines()
input_string.close()
happiness_dict = {}
names = []
for x in happiness_descriptions:
    happiness_entry = x.split(' ')
    if happiness_entry[0] not in names:
        names.append(happiness_entry[0])
    names_involved = [happiness_entry[0], happiness_entry[-1].split('.')[0]]
    names_involved.sort()
    names_involved_string = str(tuple(names_involved))
    happiness_change = int(happiness_entry[3])
    if 'lose' in happiness_entry:
        happiness_change *= -1
    happiness_dict.update({names_involved_string: happiness_dict.get(names_involved_string, 0) + happiness_change})

all_possible_seating = list(itertools.permutations(names))
max_happiness_change = 0
for possible_seating in all_possible_seating:
    happiness_change = 0
    for i in range(len(possible_seating)):
        name_beside = [possible_seating[i], possible_seating[(i + 1) % len(possible_seating)]]
        name_beside.sort()
        name_beside_string = str(tuple(name_beside))
        happiness_change += happiness_dict[name_beside_string]
    if happiness_change > max_happiness_change:
        max_happiness_change = happiness_change
print(max_happiness_change)

names.append('DSW41923')
new_possible_seating = list(itertools.permutations(names))
max_happiness_change = 0
for possible_seating in new_possible_seating:
    happiness_change = 0
    for i in range(len(possible_seating)):
        name_beside = [possible_seating[i], possible_seating[(i + 1) % len(possible_seating)]]
        name_beside.sort()
        name_beside_string = str(tuple(name_beside))
        happiness_change += happiness_dict.get(name_beside_string, 0)
    if happiness_change > max_happiness_change:
        max_happiness_change = happiness_change
print(max_happiness_change)