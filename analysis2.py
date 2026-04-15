import os
import time
from pathlib import Path
import numpy as np
from multiprocessing import Pool

# Folder that contains the .npy files
DATA_FOLDER = Path("/projappl/project_2018026/super_data")

# Workload value to reach about 60 seconds on this computer
# You can increase or decrease this number to adjust the running time
WORKLOAD = 115

def process_single_file(file_path):
    """
    This function processes one file and does intensive calculation.
    """
    # Load the data from the file
    data = np.load(file_path)
    
    # We do a lot of calculations to make the script take about 60 seconds
    count = 0
    while count < WORKLOAD:
        result = np.std(data)
        count = count + 1
        
    return result

def main():
    print("--- STARTING ANALYSIS2 ---")
    
    # 1. Collect all .npy files from the folder
    files = list(DATA_FOLDER.glob("*.npy"))
    print(f"Found {len(files)} files.")
    
    # 2. Start timing the analysis
    start_time = time.time()
    
    # 3. Use multiprocessing to run process_single_file for all files
    # The Pool will use all available processor cores automatically
    print("Processing files in parallel... (this should take about 1 minute)")
    with Pool() as pool:
        results = pool.map(process_single_file, files)
        
    # 4. Stop the timer and calculate the duration
    end_time = time.time()
    duration = end_time - start_time
    
    # 5. Show results to the user
    print("--- RESULTS ---")
    print(f"Files processed: {len(files)}")
    print(f"Total time used: {duration:.2f} seconds")
    print(f"Workload: {WORKLOAD}")
    
    # Just to show something was calculated, let's calculate the average of results
    if results:
        average_value = np.mean(results)
        print(f"Average of computed values: {average_value:.4f}")

# This part is needed on Windows for multiprocessing to work
if __name__ == "__main__":
    main()
