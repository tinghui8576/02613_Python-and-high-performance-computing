import ctypes
import multiprocessing as mp
import sys
from time import perf_counter as time
import numpy as np
from PIL import Image
import math

def init(shared_arr_):
    global shared_arr
    shared_arr = shared_arr_


def tonumpyarray(mp_arr):
    return np.frombuffer(mp_arr, dtype='float32')


def reduce_step(args):
    b, e, s, elemshape = args
    arr = tonumpyarray(shared_arr).reshape((-1,) + elemshape)
    #print(arr)
    # Change the code below to compute a step of the reduction
    # ---------------------------8<---------------------------
    arr[b] = sum(arr[b:e:s])
    #arr[b:e:s] = 1.0 - arr[b:e:s]  # <-- Dummy op. Replace with correct


if __name__ == '__main__':
    n_processes = 1
    chunk = 2
    # import numpy as np
    # arr = np.arange(10)  # 0 to 9
    # arr = arr.astype('float32')
    # arr = arr[:, None, None, None]  # (10, 1, 1, 1)
    # np.save('dummydata.npy', arr)
    # Create shared array
    data = np.load(sys.argv[1])
    elemshape = data.shape[1:]
    shared_arr = mp.RawArray(ctypes.c_float, data.size)
    arr = tonumpyarray(shared_arr).reshape(data.shape)
    np.copyto(arr, data)
    del data

    # Run parallel sum
    t = time()
    pool = mp.Pool(n_processes, initializer=init, initargs=(shared_arr,))

    # Change the code below to compute a step of the reduction
    # ---------------------------8<---------------------------
    # pool.map(reduce_step,
    #          [(i, i + chunk, 1, elemshape) for i in range(0, len(arr), chunk)],
    #          chunksize=1)
 
    s = 1
    while True:
        pool.map(reduce_step,
                [(i, i + s*chunk, s, elemshape) for i in range(0, len(arr), s*chunk)],
                chunksize=1)
        if math.ceil(len(arr)/(s*chunk)) <= 1:
            break
        s *= 2
    # Write output
    print(time() - t)
    final_image = arr[0]
    # print(arr)
    final_image /= len(arr) # For mean
    Image.fromarray(
        (255 * final_image.astype(float)).astype('uint8')
    ).save('result.png')