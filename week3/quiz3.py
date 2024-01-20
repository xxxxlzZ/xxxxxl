import re
x = input()
# a = re.match('\d\d',x)
a = re.match('(^\d{15}$)|(^\d{17}([0-9]|X)$)', x)
print(a)