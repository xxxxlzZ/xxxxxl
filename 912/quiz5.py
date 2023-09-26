l1 = input().split(" ")

for i in range(len(l1)):
    for j in range(i, len(l1)):
        if l1[i] > l1[j]:
            d = l1[i]
            l1[i] = l1[j]
            l1[j] = d

print(l1)
print(1/2)