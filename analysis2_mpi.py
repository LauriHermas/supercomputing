import os
import time
from pathlib import Path
import numpy as np
from mpi4py import MPI

# Initialize MPI communication
comm = MPI.COMM_WORLD
rank = comm.Get_rank()   # The ID of the current process (0, 1, 2...)
size = comm.Get_size()   # Total number of processes

# Folder that contains the .npy files (Supercomputer path)
# We use expandvars so we can switch between Scratch and TMPDIR easily
DATA_FOLDER = Path(os.path.expandvars("$DATA_PATH"))

# Fallback in case DATA_PATH is not set
if not os.getenv("DATA_PATH"):
    DATA_FOLDER = Path("/scratch/project_2018026/laurisfolder/super_data")

# Workload value (matches your local analysis2.py)
WORKLOAD = 115

def process_single_file(file_path):
    """
    Standard processing function, same as in analysis2.py
    """
    data = np.load(file_path)
    count = 0
    while count < WORKLOAD:
        result = np.std(data)
        count = count + 1
    return result

def main():
    # Only rank 0 handles the file listing initially
    if rank == 0:
        print(f"--- STARTING MPI ANALYSIS WITH {size} PROCESSES ---")
        all_files = list(DATA_FOLDER.glob("*.npy"))
        print(f"Found {len(all_files)} files total.")
    else:
        all_files = None

    # Step 1: Send the list of files to all processes
    all_files = comm.bcast(all_files, root=0)

    # Step 2: Each process takes its own share of files
    # (Rank 0 takes file 0, Rank 1 takes file 1, etc.)
    my_files = all_files[rank::size]
    
    # Step 3: Start timing on Rank 0
    if rank == 0:
        start_time = time.time()

    # Step 4: Each process works on its subset of files
    my_results = []
    for f in my_files:
        res = process_single_file(f)
        my_results.append(res)

    # Step 5: Gather all results back to Rank 0
    all_results = comm.gather(my_results, root=0)

    # Step 6: Rank 0 prints the final results
    if rank == 0:
        end_time = time.time()
        duration = end_time - start_time
        
        # Flatten the list of lists into one single list
        flat_results = []
        for sublist in all_results:
            for item in sublist:
                flat_results.append(item)
        
        print("--- MPI RESULTS ---")
        print(f"Total files processed: {len(flat_results)}")
        print(f"Total time used: {duration:.2f} seconds")
        print(f"Average of results: {np.mean(flat_results):.4f}")

if __name__ == "__main__":
    main()
