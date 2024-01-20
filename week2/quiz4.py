# 希尔排序
a = list(input().split(" "))
l1 = len(a)
gap = int(l1/2)

while gap >= 0.5:
    # print(gap)
    for i in range(gap, l1):
        j = i
        x = i
        temp = a[i]
        while j - gap >= 0 and int(a[j]) < int(a[j - gap]):
            # print(a[j], a[j-gap])
            a[j] = a[j - gap]
            # print(a[j], a[j - gap])
            j = j - gap
        if x != j:
            a[j] = temp
        # print(a)
    gap = int(gap/2)
print(a)
