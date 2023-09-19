l1 = [1, 2, 3, 4, 5]
a = len(l1)
b = int(a/2)
i = 0
# for i in range(0, b):
#     d = l1[i]
#     l1[i] = l1[a-i-1]
#     l1[a-i-1] = d
# print(l1)

while i < b:
    d = l1[i]
    l1[i] = l1[a-i-1]
    l1[a-i-1] = d
    i += 1


print(l1)