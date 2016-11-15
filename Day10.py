input_string = '1113222113'
count_1 = 0
count_2 = 0
count_3 = 0
for x in range(0, 50):
    result = ""
    for x in input_string:
        if x == '1':
            if count_1 == 0:
                if count_2 > 0:
                    result += str(count_2) + '2'
                    count_2 = 0
                elif count_3 > 0:
                    result += str(count_3) + '3'
                    count_3 = 0
            count_1 += 1
        if x == '2':
            if count_2 == 0:
                if count_1 > 0:
                    result += str(count_1) + '1'
                    count_1 = 0
                elif count_3 > 0:
                    result += str(count_3) + '3'
                    count_3 = 0
            count_2 += 1
        if x == '3':
            if count_3 == 0:
                if count_2 > 0:
                    result += str(count_2) + '2'
                    count_2 = 0
                elif count_1 > 0:
                    result += str(count_1) + '1'
                    count_1 = 0
            count_3 += 1
    if count_1 > 0:
        result += str(count_1) + '1'
        count_1 = 0
    elif count_2 > 0:
        result += str(count_2) + '2'
        count_2 = 0
    elif count_3 > 0:
        result += str(count_3) + '3'
        count_3 = 0
    input_string = result
print(len(result))
