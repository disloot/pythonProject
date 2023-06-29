import random
import time
import numpy as np

a = [random.random() for _ in range(10000000)]
t1 = time.time()
sum1 = sum(a)
t2 = time.time()

b = np.array(a)
t4 = time.time()
sum3 = np.sum(b)
t5 = time.time()
print(t2 - t1, t5 - t4)
