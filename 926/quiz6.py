x = eval(input())

if x < 60:
    print('不合格')
elif 60 <= x < 75:
    print('合格')
elif 75 <= x < 90:
    print('良好')
else:
    print('优秀')