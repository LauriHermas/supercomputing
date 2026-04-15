#!/bin/bash
#SBATCH --account=project_2018026
#SBATCH --job-name=local_analysis
#SBATCH --output=local_log.txt
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=40
#SBATCH --mem=40G
#SBATCH --partition=small

# Load the project's default python environment
module load python-data

# Run the multiprocessing script (it will automatically use the 40 CPUs)
python analysis2.py
