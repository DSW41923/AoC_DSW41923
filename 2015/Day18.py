import copy


def get_adjacents(a, b, configuration):
    adjacents = []
    if a > 0:
        adjacents.append(configuration[b][a - 1])
    if a < len(configuration[0]) - 1:
        adjacents.append(configuration[b][a + 1])

    if b > 0:
        adjacents += configuration[b - 1][max(a - 1, 0):min(a + 2, len(configuration[0]))]
    if b < len(configuration) - 1:
        adjacents += configuration[b + 1][max(a - 1, 0):min(a + 2, len(configuration[0]))]

    return adjacents


file_input = open('inputs/2015/input-D18.txt', 'r')
light_strings = file_input.readlines()
file_input.close()
light_map = []
for x in light_strings:
    light_map.append(list(x.replace('\n', '')))

old_lightmap = copy.deepcopy(light_map)
new_lightmap = []
for _ in range(100):
    if len(new_lightmap) == 0:
        new_lightmap = copy.deepcopy(old_lightmap)
    else:
        old_lightmap = copy.deepcopy(new_lightmap)
    for y, y_lights in enumerate(old_lightmap):
        for x, light in enumerate(y_lights):
            adjacent_lights = get_adjacents(x, y, old_lightmap)
            if light == '#' and sum(s == '#' for s in adjacent_lights) not in [2, 3]:
                new_lightmap[y][x] = '.'
            elif light == '.' and sum(s == '#' for s in adjacent_lights) == 3:
                new_lightmap[y][x] = '#'

print(sum(list(map(lambda s: s.count('#'), new_lightmap))))

old_lightmap = copy.deepcopy(light_map)
new_lightmap = []
corner_lights = [(0, 0), (0, len(old_lightmap) - 1),
                 (len(old_lightmap[0]) - 1, 0), (len(old_lightmap[0]) - 1, len(old_lightmap) - 1)]
for x, y in corner_lights:
    old_lightmap[y][x] = '#'
for _ in range(100):
    if len(new_lightmap) == 0:
        new_lightmap = copy.deepcopy(old_lightmap)
    else:
        old_lightmap = copy.deepcopy(new_lightmap)
    for y, y_lights in enumerate(old_lightmap):
        for x, light in enumerate(y_lights):
            if (x, y) not in corner_lights:
                adjacent_lights = get_adjacents(x, y, old_lightmap)
                if light == '#' and sum(s == '#' for s in adjacent_lights) not in [2, 3]:
                    new_lightmap[y][x] = '.'
                elif light == '.' and sum(s == '#' for s in adjacent_lights) == 3:
                    new_lightmap[y][x] = '#'

print(sum(list(map(lambda s: s.count('#'), new_lightmap))))