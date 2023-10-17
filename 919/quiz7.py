c = int(input(""))
g = c/3
while abs(g*g*g - c) > 0.000000001:
    g = g - (g*g*g - c)/(3*g*g)
print("%.12f" % g)