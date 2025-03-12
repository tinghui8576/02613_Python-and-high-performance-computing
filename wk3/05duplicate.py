import numpy as np
from time import perf_counter
import csv

# Define the size of the array using logspace
Size_arr = np.logspace(2, 8, num=10)

# Iterate over the different sizes
for SIZE in Size_arr:    
    # Write the SIZE and MFLOPS to the CSV file
    #writer.writerow([SIZE, run_exp(SIZE, "row"), run_exp(SIZE,"col")])
    Start = perf_counter()
    # Perform the operations multiple times for accuracy
    for i in range(1, 100):
        #mat = np.random.randint(0, 256, size=(int(SIZE), int(SIZE)), dtype=np.uint8)
        # mat = np.random.randint(0, 256, size=(1, int(SIZE)), dtype=np.uint8)
        mat = np.random.rand(1, int(SIZE))
        double_row = 2 * mat[:]
    
    # Stop the timer
    Stop = perf_counter()
    elapsed_time = Stop - Start
    total_operations = int(SIZE)
    # Calculate MFLOPS
    Mflops =( total_operations*100) / (elapsed_time * 1e6)
    print(SIZE, ", ",Mflops)


