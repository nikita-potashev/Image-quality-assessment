#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1   
#SBATCH -c 20
#SBATCH --mem=62000
#SBATCH -o logs/%j_blurout
#SBATCH -e logs/%j_blurerr

python3 train.py --model=Blur --input_shape 500 500 1 --num_epochs=10 --batch_size=32 --train_mode=cluster --metric=accuracy --last_act=softmax --loss=categorical_crossentropy
