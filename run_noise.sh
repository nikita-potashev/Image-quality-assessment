#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1   
#SBATCH -c 20
#SBATCH --mem=62000
#SBATCH --output=slurm/%j_out
#SBATCH --error=slurm/%j_err
python3 main_noise.py --c configs/noise/noise_model1.json
python3 main_noise.py --c configs/noise/noise_model2.json
python3 main_noise.py --c configs/noise/noise_model3.json