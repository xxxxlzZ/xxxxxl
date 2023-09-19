str1 = input("")
for i in range(0, len(str1)):
    if i+1 <= len(str1)-1:
        if str1[i] == str1[i+1]:
            d = 1
            break
        else:
            d = 0
if d == 1:
    print("yes")
else:
    print("no")