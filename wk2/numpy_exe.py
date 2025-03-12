
import sys
import numpy as np

lists = np.array(sys.argv[1:])

def magnitude(lists):
    return np.linalg.norm(lists)

print(magnitude(lists))