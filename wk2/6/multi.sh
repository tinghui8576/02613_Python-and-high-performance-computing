#!/bin/bash
#BSUB -J multimatrix
#BSUB -q hpc
#BSUB -W 2
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=100MB]" 
#BSUB -o multi_%J.out 
#BSUB -e multi_%J.err
#BSUB -R "select[model == XeonE5_2660v3]"

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python -u multi_numpy.py input.npy 10

