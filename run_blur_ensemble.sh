#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1   
#SBATCH -c 20
#SBATCH --mem=62000
#SBATCH --output=slurm/
#SBATCH --error=slurm/
python3 main_blur_ensemble.py --c=configs/blur_model_ensemble_cluster.json