#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1   
#SBATCH -c 20
#SBATCH --mem=62000
#SBATCH -o model/logs/%j_outfile
#SBATCH -e model/logs/%j_errfile

python3 train.py --model=Blur --input_shape 250 250 1 --num_epochs=10 --batch_size=32
