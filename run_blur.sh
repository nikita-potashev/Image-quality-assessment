#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1   
#SBATCH -c 20
#SBATCH --mem=62000

python3 main_blur.py --c configs/blur_model_cluster.json