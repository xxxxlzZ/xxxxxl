x = float(input(""))
a = int(x)
b = x-a
print(a)
print(b)
c = bin(a)
i = 0.5
print(c, end='')
print('.', end='')
while abs(b) > 0.00000001:
    if b >= i:
        print(1, end='')
        b = b - i
        i = i/2
    else:
        print(0, end='')
        i = i/2

