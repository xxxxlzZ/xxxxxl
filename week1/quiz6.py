import random

# 生成四个随机整数
w = random.randint(1, 100)
x = random.randint(1, 100)
y = random.randint(1, 100)
z = random.randint(1, 100)

# 使用条件语句进行排序
if w < x:
    w, x = x, w
if x < y:
    x, y = y, x
if y < z:
    y, z = z, y
if w < x:
    w, x = x, w

# 打印排序后的结果
print(f"从大到小排序后的结果为：{w}, {x}, {y}, {z}")