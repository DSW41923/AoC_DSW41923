input_string = '33100000'
present = int(input_string)
# def factorize(n):
#     factors = []
#     while n > 1:
#         for i in range(2, n+1):
#             if n % i == 0:
#                 n = int(n / i)
#                 factors.append(i)
#     return factors
#
# def get_present_received(num):
#     all_factors = factorize(num)
#     distinct_factors = list(set(all_factors))
#     factor_sum = 1
#     for factor in distinct_factors:
#         factor_sum *= ((factor ** (all_factors.count(factor) + 1) - 1) / (factor - 1))
#     return int(factor_sum) * 10
#
# # test
# for j in range(1, 10):
#     print(get_present_received(j))
#
# possible_numbers = []
# k = int(present ** 0.5)
# while True:
#     present_received = get_present_received(k)
#     print(k, present_received)
#     if present_received >= present:
#         possible_numbers.append(k)
#         break
#
#     if present_received < present / 10:
#         k *= 10
#     else:
#         k += 1
#
# print(min(possible_numbers))
# Factorizing isn't wrong but take too much time!

all_present_received = [0] * int(present / 10)
for i in range(1, int(present / 10)):
    for j in range(i, int(present / 10), i):
        all_present_received[j] += i * 10
print(all_present_received.index(([p for p in all_present_received if p >= present])[0]))

new_present_received = [0] * int(present / 2)
for i in range(1, len(new_present_received)):
    for j in range(i, (50 * i) + 1, i):
        if j < len(new_present_received):
            new_present_received[j] += i * 11
        else:
            break
print(new_present_received.index(([p for p in new_present_received if p >= present])[0]))