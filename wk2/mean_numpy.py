import numpy as np
import sys

a = np.load(sys.argv[1])

with open('cols.npy', 'wb') as f:
    np.save(f, np.mean(a, axis=0))
with open('rows.npy', 'wb') as f:
    np.save(f, np.mean(a, axis=1))
