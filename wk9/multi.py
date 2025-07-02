import numpy as np
from numba import jit
from time import perf_counter as time

@jit(nopython=True) 
def matmul(A, B):
    C = np.zeros((A.shape[0],B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i,j] += A[i,k] * B[k,j]
    return C

@jit(nopython=True) 
def matmul_ikj(A, B):
    C = np.zeros((A.shape[0],B.shape[1]))
    for i in range(A.shape[0]):
        for k in range(A.shape[1]):    
            for j in range(B.shape[1]):
                C[i,j] += A[i,k] * B[k,j]
    return 

@jit(nopython=True) 
def matmul_kij(A, B):
    C = np.zeros((A.shape[0],B.shape[1]))
    for k in range(A.shape[1]):
        for i in range(A.shape[0]):
            for j in range(B.shape[1]):
                C[i,j] += A[i,k] * B[k,j]
    return C

def matmul_Slow(A, B):
    C = np.zeros((A.shape[0],B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i,j] += A[i,k] * B[k,j]
    return C

A = np.random.randint(1, 101, size=(200,200))
B = np.random.randint(1, 101, size=(200,200))

Start = time()
matmul_Slow(A,B)
print(time()-Start)
Start = time()
matmul(A,B)
Start = time()
matmul(A,B)
print(time()-Start)


Start = time()
matmul_ikj(A,B)
Start = time()
matmul_ikj(A,B)
print(time()-Start)

Start = time()
matmul_kij(A,B)
Start = time()
matmul_kij(A,B)
print(time()-Start)