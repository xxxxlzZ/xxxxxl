a = input("")
x = int(a)
b = int(x/3)
n = x % 3
result = []
output = 1
if n == 1:
    for i in range(1, b):
        result.append(3)
    result.append(2)
    result.append(2)
elif n == 0:
    for i in range(1,b+1):
        result.append(3)
else:
    for i in range(1, b+1):
        result.append(3)
    result.append(2)
print(result)
