l1 = input().split(" ")
a = int(l1[0])
b = int(l1[1])
c = a/2
d = b/2
if c > b:
    e = d
else:
    e = c
x = 1
e = int(e + 1)
for i in range(1, e):
    if a % i == 0 and b % i == 0:
        x = i
print(x)