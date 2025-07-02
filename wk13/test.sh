#!/bin/bash
#BSUB -J Jindice
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=1GB]"
#BSUB -n 8
#BSUB -w ended(21241475)
#BSUB -R "span[hosts=1]"
#BSUB -o Jindice_%J.out
#BSUB -e Jindice_%J.err
#BSUB -R "select[model == XeonGold6226R]"

NUM_THREADS=8 
OMP_NUM_THREADS=$NUM_THREADS 
MPI_NUM_THREADS=$NUM_THREADS 
MKL_NUM_THREADS=$NUM_THREADS 
OPENBLAS_NUM_THREADS=$NUM_THREADS

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python mm.py