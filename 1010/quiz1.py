a = int(input(""))
b = int(a/2)
c = 0
for i in range(2,b):
    if a % i == 0:
        c = 1
        print("not a prime number")
        break
if c == 0:
    print("prime number")