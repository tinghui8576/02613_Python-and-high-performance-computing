from numba import cuda
import numpy as np 
from time import perf_counter as time
@cuda.jit
def add_kernel(x, y, out):
    i = cuda.grid(1)
    if i < len(x):
        out[i] = x[i] + y[i]


x = np.random.rand(1000000)
y = np.random.rand(1000000)
out = np.empty_like(x)
tpb = 512 # Threads per block
bpg = len(x) // tpb # Blocks per grid
add_kernel[bpg, tpb](x, y, out)
Start = time()
for _ in range(100):
    add_kernel[bpg, tpb](x, y, out)
cuda.synchronize()
print(time()-Start)


x = np.random.rand(1000000)
y = np.random.rand(1000000)
with cuda.pinned(x) and cuda.pinned(y):
    d_x = cuda.to_device(x)
    d_y = cuda.to_device(y)
    out = cuda.device_array_like(d_x)

    tpb = 512 # Threads per block
    bpg = len(d_x) // tpb # Blocks per grid
    add_kernel[bpg, tpb](d_x, d_y, out)
    Start = time()
    for _ in range(100):
        add_kernel[bpg, tpb](d_x, d_y, out)
    cuda.synchronize()
    print(time()-Start)