input_string = open('inputs/2015/input-D5.txt', 'r')
input_string = input_string.readlines()
total_nice = 0
another_nice = 0
for x in input_string:
    if ('ab' in x) or ('cd' in x) or ('pq' in x) or ('xy' in x):
        continue
    else:
        vowel_check = 0
        double_check = 0
        for i in range(len(x) - 1):
            if x[i] == x[i + 1]:
                double_check = 1
            if x[i] in ['a', 'e', 'i', 'o', 'u']:
                vowel_check += 1
        if double_check == 1 and vowel_check >= 3:
            total_nice += 1
print(total_nice)
for x in input_string:
    pattern = []
    twin_check = 0
    duo_check = 0
    for i in range(len(x) - 1):
        if i != len(x) - 2:
            if x[i] == x[i + 2]:
                duo_check = 1
        if x[i:i+2] in pattern[:-1]:
            twin_check = 1
        else:
            pattern.append(x[i:i+2])
    if duo_check == 1 and twin_check == 1:
        print(x)
        another_nice += 1
print(another_nice)
