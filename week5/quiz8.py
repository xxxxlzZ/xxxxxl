import random

inf = 0
for i in range(0, 10000):
    x = random.uniform(0, 1)
    y = random.uniform(0,1)
    if (x * x + y * y) <= 1:
        inf = inf + 1
pai = inf * 4 /(10000)
print(pai)
#
# def pi(n):
#     sum = 0.0
#     for i in range(n):
#         sign = (-1) ** i
#         term = 1 / (i * 2 +1)
#         sum  += sign * term
#     return 4.0 * sum
#
# n = 10000
# print(pi(n))

# import math
# pi = math.pi
# print(pi)