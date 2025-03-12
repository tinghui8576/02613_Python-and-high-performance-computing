from multiprocessing.pool import ThreadPool
import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
import sys
def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2.0:
            return i
    return 100

def sum_multiple(points):
    return [mandelbrot_escape_time(point) for point in points]

def generate_mandelbrot_set(points, num_processes):
    # chunk_size = 1
    # print(chunk_size)
    # chunks = [points[i:i+chunk_size] for i in range(0,len(points), chunk_size)]
    # print(len(chunks))
    chunk_size = len(points)//num_processes
    print(chunk_size)
    chunks = [points[i:i+chunk_size] for i in range(0,len(points), chunk_size)]
    print(len(chunks))
    if len(chunks) > num_processes:
        chunks[-2] = np.concatenate((chunks[-2], chunks[-1]))  # Merge the last chunk into the second last
        chunks = chunks[:-1]  # Remove the last empty chunk if it exists
    print(len(chunks))
    pool = multiprocessing.Pool(num_processes)
    results_async = [pool.apply_async(sum_multiple, (chunks[i],))
                    for i in range(num_processes)]
    escape_times = [r.get() for r in results_async]
    escape_times = np.array([item for sublist in escape_times for item in sublist]).flatten()

    return escape_times

def generate_mandelbrot_set_chunks(points, num_processes):
    chunk_size = 1
    chunks = [points[i:i+chunk_size] for i in range(0,len(points), chunk_size)]
    while len(chunks) > num_processes:
        chunks[-2] = np.concatenate((chunks[-2], chunks[-1]))  # Merge the last chunk into the second last
        chunks = chunks[:-1]  # Remove the last empty chunk if it exists
    pool = multiprocessing.Pool(num_processes)
    results_async = [pool.apply_async(sum_multiple, (chunks[i],))
                                      for i in range(num_processes)]
    escape_times = [r.get() for r in results_async] 
    escape_times = np.array([item for sublist in escape_times for item in sublist]).flatten()
    
    return escape_times

def plot_mandelbrot(escape_times):
    plt.imshow(escape_times, cmap='hot', extent=(-2, 2, -2, 2))
    plt.axis('off')
    plt.savefig('mandelbrot.png', bbox_inches='tight', pad_inches=0)

if __name__ == "__main__":
    width = 17
    height = 1
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    num_proc = int(sys.argv[1])

    # Precompute points
    x_values = np.linspace(xmin, xmax, width)
    y_values = np.linspace(ymin, ymax, height)
    points = np.array([complex(x, y) for x in x_values for y in y_values])

    # Compute set
    mandelbrot_set = generate_mandelbrot_set_chunks(points, num_proc)
    print(mandelbrot_set.shape)
    # Save set as image
    mandelbrot_set = mandelbrot_set.reshape((height, width))
    #plot_mandelbrot(mandelbrot_set)
