import re
import copy

file_input = open('../AoC_Inputs/2015/input-D19.txt', 'r')
input_strings = file_input.readlines()
file_input.close()
replacements = []
for x in input_strings:
    if '=>' in x:
        replacements.append(tuple(x.replace('\n', '').split(' => ')))

medicine_molecule = input_strings[-1].replace('\n', '')
medicine_molecule_list = re.findall(r'[A-Z][a-z]?', medicine_molecule)
new_molecules = []
for index, element in enumerate(medicine_molecule_list):
    for instruction in replacements:
        if instruction[0] == element:
            new_molecule_elements = copy.deepcopy(medicine_molecule_list)
            new_molecule_elements[index] = instruction[1]
            new_molecules.append(''.join(new_molecule_elements))
print(len(list(set(new_molecules))))

# Use replacement analysis to directly get the result
target_molecule = 'e'
print(len(medicine_molecule_list) - medicine_molecule.count('Rn') - medicine_molecule.count('Ar')
      - 2 * medicine_molecule.count('Y') - len(target_molecule))
