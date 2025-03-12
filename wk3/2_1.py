import os
import blosc
import numpy as np
import sys
from time import perf_counter

def write_numpy(arr, file_name):
    np.save(f"{file_name}.npy", arr)
    os.sync()


def write_blosc(arr, file_name, cname="zstd"):
    b_arr = blosc.pack_array(arr, cname=cname)
    with open(f"{file_name}.bl", "wb") as w:
        w.write(b_arr)
    os.sync()


def read_numpy(file_name):
    return np.load(f"{file_name}.npy")


def read_blosc(file_name):
    with open(f"{file_name}.bl", "rb") as r:
        b_arr = r.read()
    return blosc.unpack_array(b_arr)


def test(arr, name ):
    Write_Start = perf_counter()
    write_numpy(arr, name )
    Write_Stop = perf_counter()
    write_blosc(arr, name )
    Writeb_Stop = perf_counter()
    read_numpy(name )
    Read_Stop = perf_counter()
    read_blosc(name )
    Readb_Stop = perf_counter()
    print(Write_Stop-Write_Start, Writeb_Stop-Write_Stop,Read_Stop - Writeb_Stop, Readb_Stop-Read_Stop )

SIZE = sys.argv[1]

mat = np.zeros((int(SIZE), int(SIZE), int(SIZE)), dtype=np.uint8)
name = "Zero"
print(name)
test(mat, name)

tiled_mat = np.tile(
                np.arange(256, dtype='uint8'),
                (int(SIZE) // 256) * int(SIZE) * int(SIZE),
                ).reshape(int(SIZE),int(SIZE), int(SIZE))

name = "Tiled"
print(name )
test(tiled_mat, name )

name = "Rand"
rand_mat = np.random.randint(0, 256, size=(int(SIZE), int(SIZE), int(SIZE)), dtype=np.uint8)
print(name )
test(rand_mat, name )



    