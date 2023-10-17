c = int(input(""))
# g = c/2
# g = c/4
g = c
while abs(g*g - c) > 0.000000001:
    g = (g + c/g)/2
print(g)