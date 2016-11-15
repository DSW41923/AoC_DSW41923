input_string = open('input-D8.txt', 'r')
input_string = input_string.readlines()
count = 0
count_another = 0
for x in input_string:
    s = x.replace('\n', '')
    print(len(s), len(eval(s)), s)
    count += len(s) - len(eval(s))
    count_another += 2
    for i in range(0, len(s)):
        if s[i] == '\"' or s[i] == '\\':
            count_another += 1
print(count, count_another)
