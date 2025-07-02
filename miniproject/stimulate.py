from os.path import join
from time import perf_counter as time
import sys
import csv
import numpy as np
import multiprocessing as mp
LOAD_DIR = 'modified_swiss_dwellings/'
MAX_ITER = 20_000
ABS_TOL = 1e-4

def load_data(load_dir, bid):
    SIZE = 512
    u = np.zeros((SIZE + 2, SIZE + 2))
    u[1:-1, 1:-1] = np.load(join(load_dir, f"{bid}_domain.npy"))
    interior_mask = np.load(join(load_dir, f"{bid}_interior.npy"))
    return u, interior_mask

# @profile
def jacobi(u, interior_mask, max_iter, atol=1e-6):
    u = np.copy(u)

    for i in range(max_iter):
        # Compute average of left, right, up and down neighbors, see eq. (1)
        u_new = 0.25 * (u[1:-1, :-2] + u[1:-1, 2:] + u[:-2, 1:-1] + u[2:, 1:-1])
        u_new_interior = u_new[interior_mask]
        delta = np.abs(u[1:-1, 1:-1][interior_mask] - u_new_interior).max()
        u[1:-1, 1:-1][interior_mask] = u_new_interior

        if delta < atol:
            print(i)
            break
    return u

from numba import jit
@jit(nopython=True) 
def jacobi_jit(u, interior_mask, max_iter, atol=1e-6):
    u = np.copy(u)

    for i in range(max_iter):
        # Compute average of left, right, up and down neighbors, see eq. (1)
        u_new = 0.25 * (u[1:-1, :-2] + u[1:-1, 2:] + u[:-2, 1:-1] + u[2:, 1:-1])

        delta = 0.0
        for j in range(interior_mask.shape[0]):
            for k in range(interior_mask.shape[1]):
                if interior_mask[j,k] == True:
                    diff = abs(u[1:-1, 1:-1][j, k] - u_new[j, k])
                    u[1:-1, 1:-1][j,k] = u_new[j,k]
                    if diff > delta:
                        delta = diff

        if delta < atol:
            print(i)
            break
    return u


def paralize(bid):
    # Load floor plans
    u0, mask = load_data(LOAD_DIR, bid)
    # Run jacobi iterations for each floor plan
    # u = jacobi(u0, mask, MAX_ITER, ABS_TOL)
    u = jacobi_jit(u0, mask, MAX_ITER, ABS_TOL)
    return u0, mask, u

def muli_paralize(bids):
    return [paralize(bid) for bid in bids]

def summary_stats(u, interior_mask):
    u_interior = u[1:-1, 1:-1][interior_mask]
    mean_temp = u_interior.mean()
    std_temp = u_interior.std()
    pct_above_18 = np.sum(u_interior > 18) / u_interior.size * 100
    pct_below_15 = np.sum(u_interior < 15) / u_interior.size * 100
    return {
        'mean_temp': mean_temp,
        'std_temp': std_temp,
        'pct_above_18': pct_above_18,
        'pct_below_15': pct_below_15,
    }


if __name__ == '__main__':
    # Load data
    LOAD_DIR = '/dtu/projects/02613_2025/data/modified_swiss_dwellings/'
    with open(join(LOAD_DIR, 'building_ids.txt'), 'r') as f:
        building_ids = f.read().splitlines()
    print(len(building_ids))
    if len(sys.argv) < 2:
        N = 1
    else:
        N = int(sys.argv[1])
    building_ids = building_ids[:N]
    num_processes = int(sys.argv[2])

    start = time()
    with mp.Pool(processes=num_processes) as pool:
        # results = pool.map(paralize, building_ids)
        # chunk_size = max(1, len(building_ids) // (num_processes * 3))
        chunk_size = 1
        chunks = np.array_split(building_ids, len(building_ids) // chunk_size)
        results_async = [pool.apply_async(muli_paralize, args=(chunk,)) for chunk in chunks]
        results = [r.get() for r in results_async] 
    
    flat_results = [item for sublist in results for item in sublist]
    u0_list, mask_list, u_list = zip(*flat_results)

    all_u0   = np.stack(u0_list)
    all_interior_mask = np.stack(mask_list)
    all_u    = np.stack(u_list)

    runtime_sec = round(time() - start, 2)

    # Append to CSV file
    with open("runtime_log.csv", "a", newline='') as f:
        writer = csv.writer(f)
        
        # Optional: write header if file is empty
        if f.tell() == 0:
            writer.writerow(["runtime_seconds", "cores"])
        
        writer.writerow([runtime_sec, num_processes])

    # Print summary statistics in CSV format
    stat_keys = ['mean_temp', 'std_temp', 'pct_above_18', 'pct_below_15']
    print('building_id, ' + ', '.join(stat_keys))  # CSV header
    for bid, u, interior_mask in zip(building_ids, all_u, all_interior_mask):
        stats = summary_stats(u, interior_mask)
        print(f"{bid},", ", ".join(str(stats[k]) for k in stat_keys))