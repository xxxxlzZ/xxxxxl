a = input().split(" ")
j = len(a)
b = a.copy()
for i in range(0, j):
    c = 1
    d = 1
    if i == 0:
        
        c = 1
    else:
        for x in range(0, i):
            c = c * int(a[x])
#            print(a[x])
    if i + 1 == j:
        d = 1
    else:
        for y in range(i+1, j):
            d = d * int(a[y])
#            print(a[y])
#    print(c, d)
    b[i] = c * d
print(b)