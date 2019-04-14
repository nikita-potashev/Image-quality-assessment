#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1   
#SBATCH -c 20
#SBATCH --mem=62000
#SBATCH --output=slurm/%j_n
#SBATCH --error=slurm/%j_ne

python3 main_noise.py --c configs/noise/noise_model2.json
