import numpy as np
import sys
from time import perf_counter

a = np.load(sys.argv[1])
t = sys.argv[2]
t1_start = perf_counter() 
with open('output.npy', 'wb') as f:
    np.save(f, np.linalg.matrix_power(a, int(t)+1))

t1_stop = perf_counter()

print(t1_stop - t1_start)