#!/bin/bash
#SBATCH --account=project_2018026
#SBATCH --job-name=mpi_analysis
#SBATCH --output=mpi_log.txt
#SBATCH --time=00:05:00
#SBATCH --ntasks=40
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --partition=small

# Clear existing modules and load the specific Intel environment
module purge
module load intel-oneapi-compilers-classic/2021.6.0
module load intel-oneapi-mpi/2021.6.0
module load python-data

# Run the MPI script with srun using python3
srun python3 analysis2_mpi.py
