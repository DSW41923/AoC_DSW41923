floor = 0
string = open('../inputs/2015/input-D1.txt', 'r')
input_string = string.read()
index = 0
for x in input_string:
    index += 1
    if x == '(':
        floor += 1
    elif x == ')':
        floor -= 1
    if floor == -1:
        print(index)
print(floor)
string.close()
