house = 1
position_S = (0, 0)
position_R = (0, 0)
old_positions = [(0, 0)]
current = 'S'
string = open('inputs/2015/input-D3.txt', 'r')
input_string = string.read()
# input_string = '^v^v^v^v^v'
for x in input_string:
    if current == 'S':
        new_position_x = position_S[0]
        new_position_y = position_S[1]
        if x == '>':
            new_position_x += 1
        elif x == '<':
            new_position_x -= 1
        elif x == '^':
            new_position_y += 1
        elif x == 'v':
            new_position_y -= 1
        position_S = (new_position_x, new_position_y)
        # print(position_S, current)
        if position_S not in old_positions:
            house += 1
            old_positions.append(position_S)
        current = 'R'
    elif current == 'R':
        new_position_x = position_R[0]
        new_position_y = position_R[1]
        if x == '>':
            new_position_x += 1
        elif x == '<':
            new_position_x -= 1
        elif x == '^':
            new_position_y += 1
        elif x == 'v':
            new_position_y -= 1
        position_R = (new_position_x, new_position_y)
        # print(position_R, current)
        if position_R not in old_positions:
            house += 1
            old_positions.append(position_R)
        current = 'S'
print(house)
