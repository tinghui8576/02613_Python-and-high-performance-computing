from numba import cuda
import numpy as np 
from time import perf_counter as time
@cuda.jit
def matmul_kernel(A, B, C):
    i,j = cuda.grid(2)

    C[i,j] = A[i,j] * B[i,j]

A = np.random.randint(1, 101, size=(200,200))
B = np.random.randint(1, 101, size=(200,200))

A_gpu = cuda.to_device(A)
B_gpu = cuda.to_device(B)
C_gpu = cuda.device_array_like(A)

Start = time()

tpb = 32, 32
bpg = (A.shape[0] // tpb[0],
A.shape[1] // tpb[1])
matmul_kernel[bpg, tpb](A_gpu, B_gpu, C_gpu)
cuda.synchronize()  # Ensure kernel finishes before timing ends
print("Time:", round(time() - Start, 4), "seconds")

C = C_gpu.copy_to_host()