import re


def parse(string):
    result = re.findall(r'\d+', string)
    start = (int(result[0]), int(result[1]))
    end = (int(result[2]) + 1, int(result[3]) + 1)
    return start, end


input_string = open('inputs/2015/input-D6.txt', 'r')
input_string = input_string.readlines()
lights = []
on_count = 0
for x in range(1000):
    lights.append([False] * 1000)
for line in input_string:
    start, end = parse(line)
    for x in range(start[0], end[0]):
        for y in range(start[1], end[1]):
            if line.startswith('turn on'):
                lights[x][y] = True
            elif line.startswith('turn off'):
                lights[x][y] = False
            elif line.startswith('toggle'):
                lights[x][y] = not lights[x][y]
            else:
                print('Wrong!')
for x in range(1000):
    for y in range(1000):
        if lights[x][y]:
            on_count += 1
        else:
            pass
print('on = ' + str(on_count))

lights_bright = []
bright_count = 0
for x in range(1000):
    lights_bright.append([0] * 1000)
for line in input_string:
    start, end = parse(line)
    for x in range(start[0], end[0]):
        for y in range(start[1], end[1]):
            if line.startswith('turn on'):
                lights_bright[x][y] += 1
            elif line.startswith('turn off'):
                lights_bright[x][y] -= 1
                if lights_bright[x][y] < 0:
                    lights_bright[x][y] = 0
            elif line.startswith('toggle'):
                lights_bright[x][y] += 2
            else:
                print('Wrong!')
for x in range(1000):
    for y in range(1000):
        bright_count += lights_bright[x][y]
print('bright = ' + str(bright_count))
