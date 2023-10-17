a = input().split(" ")
b = a.copy()
length = len(a)
for i in range(1, length):
    j = i - 1
    m = i
    while a[m] > a[j]:
        temp = a[m]
        a[m] = a[j]
        a[j] = temp
        m = m - 1
        if j - 1 >= 0:
            j = j-1
print(a)
for i in range(0, length-1):
    for j in range(0, length-1):
        if b[j] < b[j+1]:
            temp = b[j]
            b[j] = b[j+1]
            b[j+1] = temp
print(b)
