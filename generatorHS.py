import random
import time
import heapS as hs

#Timing for sorted arrays
items = [i for i in range(1000)]

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)


items = [i for i in range(2000)]

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)

items = [i for i in range(4000)]

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)

items = [i for i in range(8000)]

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)

items = [i for i in range(16000)]

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)

items = [i for i in range(32000)]

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)

items = [i for i in range(100000)]

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)

items = [i for i in range(500000)]

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)


#Timing for unsorted arrays
random.seed(1)
items = random.sample(range(1000000),1000)

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)

items = random.sample(range(1000000),2000)

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)

items = random.sample(range(1000000),4000)

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)

items = random.sample(range(1000000),8000)

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)

items = random.sample(range(1000000),16000)

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)

items = random.sample(range(1000000),32000)

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)

items = random.sample(range(1000000),100000)

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)

items = random.sample(range(1000000),500000)

time_start = time.time()
print(hs.sort(items))
time_end = time.time()
print(time_end-time_start)
