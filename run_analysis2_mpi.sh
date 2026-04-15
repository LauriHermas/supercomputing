#!/bin/bash
#SBATCH --account=project_2018026
#SBATCH --job-name=mpi_analysis
#SBATCH --output=mpi_log.txt
#SBATCH --time=00:05:00
#SBATCH --ntasks=40
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --partition=small

# Load the project's default python environment that includes mpi4py and numpy
module load python-data

# Run the MPI script with srun
srun python analysis2_mpi.py
