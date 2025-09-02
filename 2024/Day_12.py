import argparse

from itertools import product


def get_adjacent(x, x_range, y, y_range):
    adjacent = []
    if x > 0:
        adjacent.append((x-1,y))
    if x < x_range-1:
        adjacent.append((x+1,y))
    if y > 0:
        adjacent.append((x,y-1))
    if y < y_range-1:
        adjacent.append((x,y+1))
    return adjacent


def get_map_data(input_string):
    garden_map = list(map(list, input_string.split('\n')))
    x_range = len(garden_map)
    y_range = len(garden_map[0])
    ungrouped_regions = {}
    for x in range(x_range):
        for y in range(y_range):
            if garden_map[x][y] in ungrouped_regions:
                ungrouped_regions[garden_map[x][y]] += [(x, y)]
            else:
                ungrouped_regions[garden_map[x][y]] = [(x, y)]

    regions = {}
    for plant in ungrouped_regions:
        regions[plant] = []
        while ungrouped_regions[plant]:
            new_region = [ungrouped_regions[plant].pop(0)]
            found_adjacent = True
            while found_adjacent:
                found_adjacent = False
                for o, n in product(ungrouped_regions[plant], new_region):
                    if (o[0]-n[0])**2+(o[1]-n[1])**2 == 1:
                        new_region += [o]
                        ungrouped_regions[plant].remove(o)
                        found_adjacent = True
                        break
            regions[plant].append(new_region)
    return garden_map, x_range, y_range, regions


def part_1(input_string):
    garden_map, x_range, y_range, regions = get_map_data(input_string)
    result = 0
    for plant in regions:
        for region in regions[plant]:
            perimeter = 0
            for x, y in region:
                adjacent = get_adjacent(x, x_range, y, y_range)
                perimeter += (4-len(adjacent))+len([(a,b) for a,b in adjacent if garden_map[a][b] != plant])
            result += perimeter * len(region)
    print(result)


def part_2(input_string):
    garden_map, x_range, y_range, regions = get_map_data(input_string)
    result = 0
    for plant in regions:
        for region in regions[plant]:
            corner_count = 0
            for x, y in region:
                adjacent = get_adjacent(x, x_range, y, y_range)
                adj_same_plant = [(a,b) for a,b in adjacent if garden_map[a][b] == plant]
                adj_same_plant_count = len(adj_same_plant)
                diagonal = []
                if x > 0:
                    if y > 0:
                        diagonal.append((x-1,y-1))
                    if y < y_range-1:
                        diagonal.append((x-1,y+1))
                if x < x_range-1:
                    if y > 0:
                        diagonal.append((x+1,y-1))
                    if y < y_range-1:
                        diagonal.append((x+1,y+1))
                diagonal_same_plant = [(a,b) for a,b in diagonal if garden_map[a][b] == plant]
                diagonal_same_plant_count = len(diagonal_same_plant)
                if adj_same_plant_count == 4:
                    corner_count += (4-diagonal_same_plant_count)
                elif adj_same_plant_count == 3:
                    # OOO
                    # AXB
                    # OTO
                    t, a, b = adj_same_plant[0], adj_same_plant[1], adj_same_plant[2]
                    if t[0] == adj_same_plant[1][0] or t[1] == adj_same_plant[1][1]:
                        t, a, b = adj_same_plant[2], adj_same_plant[1], adj_same_plant[0]
                    elif t[0] == adj_same_plant[2][0] or t[1] == adj_same_plant[2][1]:
                        t, a, b = adj_same_plant[1], adj_same_plant[2], adj_same_plant[0]

                    if diagonal_same_plant_count == 0:
                        corner_count += 2
                    elif diagonal_same_plant_count == 1:
                        if (t[0], a[1]) in diagonal and garden_map[t[0]][a[1]] == plant:
                            corner_count += 1
                        elif (t[0], b[1]) in diagonal and garden_map[t[0]][b[1]] == plant:
                            corner_count += 1
                        elif (a[0], t[1]) in diagonal and garden_map[a[0]][t[1]] == plant:
                            corner_count += 1
                        elif (b[0], t[1]) in diagonal and garden_map[b[0]][t[1]] == plant:
                            corner_count += 1
                        else:
                            corner_count += 2
                    elif diagonal_same_plant_count == 2:
                        if (set([(t[0], a[1]), (t[0], b[1])]) == set(diagonal_same_plant)) or \
                            (set([(a[0], t[1]), (b[0], t[1])]) == set(diagonal_same_plant)):
                            continue
                        if ((t[0], a[1]) in diagonal and garden_map[t[0]][a[1]] == plant) or \
                           ((t[0], b[1]) in diagonal and garden_map[t[0]][b[1]] == plant) or \
                           ((a[0], t[1]) in diagonal and garden_map[a[0]][t[1]] == plant) or \
                           ((b[0], t[1]) in diagonal and garden_map[b[0]][t[1]] == plant):
                            corner_count += 1
                        else:
                            corner_count += 2
                    elif diagonal_same_plant_count == 3:
                        if ((t[0], a[1]) in diagonal_same_plant and (t[0], b[1]) in diagonal_same_plant) or \
                            ((a[0], t[1]) in diagonal_same_plant and (b[0], t[1]) in diagonal_same_plant):
                            continue
                        else:
                            corner_count += 1
                    elif diagonal_same_plant_count == 4:
                        continue
                elif adj_same_plant_count == 2:
                    if 0 < x < x_range-1 and (garden_map[x-1][y] == plant and garden_map[x+1][y] == plant):
                        continue
                    elif 0 < y < y_range-1 and (garden_map[x][y-1] == plant and garden_map[x][y+1] == plant):
                        continue
                    else:
                        critical_diagonal = (adj_same_plant[0][0], adj_same_plant[1][1])
                        if critical_diagonal == (x,y):
                            critical_diagonal = (adj_same_plant[0][1], adj_same_plant[1][0])
                        if garden_map[critical_diagonal[0]][critical_diagonal[1]] == plant:
                            corner_count += 1
                        else:
                            corner_count += 2
                elif adj_same_plant_count == 1:
                    corner_count += 2
                elif adj_same_plant_count == 0:
                    corner_count += 4
                else:
                    continue
            result += corner_count * len(region)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_12.txt', 'r')
    input_string = file_input.read()
    file_input.close()

    if args.part == '1':
        part_1(input_string)
    elif args.part == '2':
        part_2(input_string)
    else:
        part_1(input_string)
        part_2(input_string)


if __name__ == "__main__":
    main()
