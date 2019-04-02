#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1   
#SBATCH -c 20
#SBATCH --mem=62000
#SBATCH -o logs/%j__noiseout
#SBATCH -e logs/%j_noiseerr

python3 train.py --model=Noise --input_shape 500 500 1 --num_epochs=10 --batch_size=32 --train_mode=cluster --metric=accuracy
