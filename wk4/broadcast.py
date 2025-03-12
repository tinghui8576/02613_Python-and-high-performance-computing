import numpy as np
def Standardize_rows(data, mean, std):
    return (data - mean)/ std

data = np.array([[1, 2, 3],[4, 5,6]])
mean = np.array([0.5, 1, 3])
std = np.array([1, 2,3])

# print(Standardize_rows(data, mean, std))

def outer(vec1, vec2):
    vec1 = vec1[:, None]
    return vec1*vec2
    #print(vec1.dot(vec2))

vec1 = np.array([1, 2])
vec2 = np.array([3, 4, 5])
#print(outer(vec1, vec2))

def distmat_1d(vec1, vec2):
    vec1 = vec1[:, None]
    return np.abs(vec1 -vec2 )

vec1 = np.array([1, 2])
vec2 = np.array([3, 0.5, 1])
distmat_1d(vec1, vec2)