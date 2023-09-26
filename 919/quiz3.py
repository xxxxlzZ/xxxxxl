# 人 狼 羊 菜
a = [0, 0, 0, 0]
i = 1


def m(x, n):
    if x[n] == 0:
        x[n] = 1
    else:
        x[n] = 0

    n = n + 1
    if n > 3:
        n = 1
