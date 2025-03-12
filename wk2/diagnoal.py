import sys
import numpy as np


def convert_string(s):
    if s.isdigit():
        return int(s)  # Convert to int if all characters are digits
    else:
        return float(s)

l = [convert_string(i) for i in sys.argv[1:]]
   
with open('output.npy', 'wb') as f:
    np.save(f, np.diag(l))
