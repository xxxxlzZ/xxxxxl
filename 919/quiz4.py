a = input("")
x = int(a)
mid = int(x/2)
b = mid*mid
left = 0
right = x
while round(b, 6) != x:
    if b > x:
        right = mid
        mid = (left + mid)/2
        b = mid*mid
    else:
        left = mid
        mid = (mid + right)/2
        b = mid*mid
print("%.6f" % mid)