import sys
import numpy as np
from time import perf_counter
def distance_matrix(p1, p2):
    p1, p2 = np.radians(p1), np.radians(p2)
    cosprod = np.cos(p1[:, 0][:, None]) * np.cos(p2[:, 0])

    dsin2_x = np.sin(0.5 *(p1[:, 0][:, None] - p2[:, 0])) ** 2
    dsin2_y = np.sin(0.5 *(p1[:, 1][:, None] - p2[:, 1])) ** 2

    
    a = dsin2_x + cosprod * dsin2_y
    a = np.clip(a, 0.0, 1.0)
    D = 2 * np.arcsin(np.sqrt(a))

    # cosprod_1 = np.cos(p1[:, 0])
    # cosprod_2 = np.cos(p2[:, 0])
    # D = np.empty((len(p1), len(p2)))
    # for i in range(len(p1)):
    #     dsin2_x = np.sin(0.5 *(p1[i, 0] - p2[:, 0])) ** 2
    #     dsin2_y = np.sin(0.5 *(p1[i, 1] - p2[:, 1])) ** 2
       
    #     cosprod = cosprod_1[i] * cosprod_2
    #     a = dsin2_x + cosprod * dsin2_y 
        
    #     D[i, :] = 2 * np.arcsin(np.sqrt(a))
    # print(D)
    D *= 6371  # Earth radius in km
    return D


def load_points(fname):
    data = np.loadtxt(fname, delimiter=',', skiprows=1, usecols=(1, 2))
    return data


def distance_stats(D):
    # Extract upper triangular part to avoid duplicate entries
    assert D.shape[0] == D.shape[1], 'D must be square'
    idx = np.triu_indices(D.shape[0], k=1)
    distances = D[idx]
    return {
        'mean': float(distances.mean()),
        'std': float(distances.std()),
        'max': float(distances.max()),
        'min': float(distances.min()),
    }

Size_arr = np.logspace(1, 4.5, num=10)
for i in Size_arr:
    points = np.random.randint(20, 256, size=(int(i), 2), dtype=np.uint8)
    
    #print(mat.shape)


    # fname = sys.argv[1]
    # points = load_points(fname)
    Start = perf_counter()
    D = distance_matrix(points, points)
    stats = distance_stats(D)
    Stop = perf_counter()

    elapsed_time = Stop - Start

    # Calculate MFLOPS
    Mflops = elapsed_time 
    print(i, Mflops)
    #print(stats)
