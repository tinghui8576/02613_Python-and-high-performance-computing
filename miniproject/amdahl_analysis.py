# Example times
T_1 = 100
T_16 = 10

def amdahl_analysis(T_1, T_X, X):
    # T_1 is the time for 1 core
    # T_X is the time for X cores
    # X is the number of cores
    parralel_time_X = X*(T_1 - T_X) / (X - 1)
    print(f"Parralel time: {parralel_time_X:.2f}")
    serial_time =(X*T_X-T_1)/(X-1)
    print(f"Serial time: {serial_time:.2f}")

    print ("Checking if calculation is correct")
    time_for_1_cores = serial_time+parralel_time_X
    time_for_X_cores = serial_time+parralel_time_X/X
    print (f"Calculated for 1 core: {time_for_1_cores:.2f} vs real time {T_1:.2f}")
    print (f"Calculated for {X} cores: {time_for_X_cores:.2f} vs real time {T_X:.2f}")
    P = parralel_time_X/T_1
    S = 1-P
    print (f"Parallelizable fraction: {P:.2f}, Serial fraction: {S:.2f}")
    print (f"Max speedup: {1/S:.2f}")
    
amdahl_analysis(T_1, T_16, 16)