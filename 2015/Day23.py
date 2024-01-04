file_input = open('inputs/2015/input-D23.txt', 'r')
input_strings = file_input.readlines()
file_input.close()
instructions = []
for x in input_strings:
    if x.startswith('j'):
        instructions.append(tuple(x.replace('\n', '').replace(',', '').split(' ')))
    else:
        instructions.append(tuple(x.replace('\n', '').split(' ')))

part1_register = {'a': 0, 'b': 0}
def program(register):
    index = 0
    while index < len(instructions):
        instruction = instructions[index]
        if instruction[0] == 'hlf':
            register[instruction[1]] //= 2
            index += 1
        elif instruction[0] == 'tpl':
            register[instruction[1]] *= 3
            index += 1
        elif instruction[0] == 'inc':
            register[instruction[1]] += 1
            index += 1
        elif instruction[0] == 'jmp':
            index += int(instruction[-1])
        elif instruction[0] == 'jie':
            if register[instruction[1]] % 2 == 0:
                index += int(instruction[-1])
            else:
                index += 1
        elif instruction[0] == 'jio':
            if register[instruction[1]] == 1:
                index += int(instruction[-1])
            else:
                index += 1
program(part1_register)
print(part1_register)
part2_register = {'a': 1, 'b': 0}
program(part2_register)
print(part2_register)

