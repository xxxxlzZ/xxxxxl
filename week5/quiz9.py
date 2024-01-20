import math
import random

inf = 0
for i in range(0, 10000):
    x = random.uniform(2, 3)
    y = random.uniform(0, 21)
    a = x * x + 4 * x * math.sin(x)
    if y <= a:
        inf = inf + 1
b = 21 *( inf/10000 )
print(b)