a = input().split(" ")
length = len(a)
for i in range(1, length):
    j = i - 1
    m = i
    while a[m] < a[j]:
        temp = a[m]
        a[m] = a[j]
        a[j] = temp
        m = m - 1
        if j - 1 >= 0:
            j = j-1
print(a)
