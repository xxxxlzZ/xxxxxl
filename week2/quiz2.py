import time
start_time = time.time()
a = 0
for i in range(0, 100000):
    a = a + i
end_time = time.time()
time = end_time - start_time
print("%.12f" % time)