input_string = open('../AoC_Inputs/2015/input-D2.txt', 'r')
input_string = input_string.readlines()
total_area = 0
total_length = 0
for x in input_string:
    lengths = x.split('x')
    l = int(lengths[0])
    m = int(lengths[1])
    n = int(lengths[2])
    M = max(l, m, n)
    area = ((l+m+n) ** 2 - l ** 2 - m ** 2 - n ** 2) + ((l*m*n)/M)
    length = (2*(l+m+n) - 2*M) + (l*m*n)
    total_area += area
    total_length += length
print(total_area)
print(total_length)
