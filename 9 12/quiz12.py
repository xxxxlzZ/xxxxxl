a = input("")
x = int(a)
mid = int(x/2)
b = mid*mid*mid
left = 0
right = a
while b != x:
    if b > x:
        right = mid
        mid = (left + mid)/2
        b = mid*mid*mid
    else:
        left = mid
        mid = (mid + right)/2
        b = mid*mid*mid
print("%.6f" % mid)