from multiprocessing.pool import ThreadPool
import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
import sys

if __name__ == "__main__":
    path = sys.argv[1]
    N = int(sys.argv[2])
    n = int(sys.argv[3])
    width = N
    height = N

    mandelbrot_array = np.memmap('mandelbrot.raw', dtype='int32', mode='r', shape=(height, width))
    # print(mandelbrot_set.shape)
    # Save set as image
    # mandelbrot_set = mandelbrot_set.reshape((height, width))
    #plot_mandelbrot(mandelbrot_set)
