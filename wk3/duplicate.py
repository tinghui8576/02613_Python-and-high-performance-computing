import numpy as np
from time import perf_counter
import csv

# Define the size of the array using logspace
Size_arr = np.logspace(1, 4.5, num=10)

def run_exp(SIZE, idx):
    Start = perf_counter()
    # Perform the operations multiple times for accuracy
    for i in range(1, 1000):
        mat = np.random.randint(0, 256, size=(int(SIZE), int(SIZE)), dtype=np.uint8)

        if idx == "col":
            # Perform some operations
            double_column = 2 * mat[:, 0]
        else:
            double_row = 2 * mat[0, :]
    
    # Stop the timer
    Stop = perf_counter()
    elapsed_time = Stop - Start

    # Calculate MFLOPS
    Mflops = mat.nbytes / (elapsed_time / 1000 * 1e6)

    return Mflops

# Open a CSV file to write the results
with open("content.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    
    # Write the header row
    writer.writerow(["SIZE", "row", "col"])

# Iterate over the different sizes
for SIZE in Size_arr:    
    # Write the SIZE and MFLOPS to the CSV file
    #writer.writerow([SIZE, run_exp(SIZE, "row"), run_exp(SIZE,"col")])
    
    Start = perf_counter()
    # Perform the operations multiple times for accuracy
    for i in range(1, 1000):
        mat = np.random.randint(0, 256, size=(int(SIZE), int(SIZE)), dtype=np.uint8)
        double_row = 2 * mat[0, :]
    
    # Stop the timer
    Stop = perf_counter()
    elapsed_time = Stop - Start

    # Calculate MFLOPS
    Mflops_row = int(SIZE) / (elapsed_time / 1000 * 1e6)
    Start = perf_counter()
    # Perform the operations multiple times for accuracy
    for i in range(1, 1000):
        mat = np.random.randint(0, 256, size=(int(SIZE), int(SIZE)), dtype=np.uint8)
        double_col = 2 * mat[:, 0]
    
    # Stop the timer
    Stop = perf_counter()
    elapsed_time = Stop - Start

    # Calculate MFLOPS
    Mflops_col = int(SIZE) / (elapsed_time / 1000 * 1e6)
    print(SIZE, ", ", Mflops_row, ", ", Mflops_col)
print("Results saved to content.csv")

