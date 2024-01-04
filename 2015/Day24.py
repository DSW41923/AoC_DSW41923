import math
import itertools


def min_package_knapsack(weights, target, package_num):
    if sum(weights[:package_num]) > target:
        return []
    elif sum(weights[:package_num]) == target:
        return [tuple(weights)]
    else:
        result = []
        for combination in itertools.combinations(weights, package_num):
            if sum(combination) == target:
                new_weight = [w for w in weights if w not in combination]
                group_num = sum(new_weight) // target
                if get_min_package_combinations(new_weight, target, group_num, package_num):
                    result.append(combination)
        return result

def get_min_package_combinations(weights, target, group_num, min_package_num=0):
    if group_num <= 0 or len(weights) == 0 or min_package_num > len(weights):
        return []
    elif group_num == 1:
        if sum(weights) == target and min_package_num <= len(weights):
            return [tuple(weights)]
        else:
            return []
    else:
        for i in range(min_package_num, len(weights)):
            result = min_package_knapsack(weights, target, i)
            if result:
                return result


file_input = open('../inputs/2015/input-D24.txt', 'r')
input_strings = file_input.readlines()
file_input.close()
packages = list(map(int, input_strings))
three_group_target = sum(packages) // 3
three_group_combinations = get_min_package_combinations(packages, three_group_target, 3)
quantum_entanglement = list(map(math.prod, three_group_combinations))
print(min(quantum_entanglement))
four_group_target = sum(packages) // 4
four_group_combinations = get_min_package_combinations(packages, four_group_target, 4)
quantum_entanglement = list(map(math.prod, four_group_combinations))
print(min(quantum_entanglement))
