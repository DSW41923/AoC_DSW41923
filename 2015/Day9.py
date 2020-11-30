import itertools


def getDistance(route, start, end):
    if start == end:
        result = 0
    else:
        try:
            result = route[(start, end)]
        except:
            result = route[(end, start)]

    return result


input_string = open('input-D9.txt', 'r')
input_string = input_string.readlines()
route = {}
locations = []
for x in input_string:
    line = x.split(' ')
    start = line[0]
    end = line[2]
    distance = int(line[-1])
    route[(start, end)] = distance
    if start not in locations:
        locations.append(start)
    if end not in locations:
        locations.append(end)
min_distance = float("inf")
max_distance = 0
nums = range(0, 8)
possible_routes = list(itertools.permutations(nums, 8))
for r in possible_routes:
    current_distance = 0
    for i in range(0, 7):
        current_distance += getDistance(route, locations[r[i]], locations[r[i + 1]])
        if current_distance > min_distance:
            i = 7
    if current_distance < min_distance:
        min_distance = current_distance
    if current_distance > max_distance:
        max_distance = current_distance
print(min_distance, max_distance)
