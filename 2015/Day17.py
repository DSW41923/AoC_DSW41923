input_string = open('../inputs/2015/input-D17.txt', 'r')
container_data_string = input_string.readlines()
input_string.close()
container_data = list(map(int, container_data_string))
combination_count = 0
combinations = []
liter = 150
for x in range(2 ** len(container_data)):
    text_num = bin(x).replace('0b', '')
    while len(text_num) < len(container_data):
        text_num = '0' + text_num
    composition = list(map(int, list(text_num)))
    total = sum([a*b for a, b in zip(container_data, composition)])
    if total == 150:
        combination_count += 1
        combinations.append(text_num)
print(combination_count)

minimum_container_used = min(n.count('1') for n in combinations)
minimum_container_used_count = len([n for n in combinations if n.count('1') == minimum_container_used])
print(minimum_container_used_count)