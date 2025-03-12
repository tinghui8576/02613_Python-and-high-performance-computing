#!/bin/bash
#BSUB -J PI
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=1GB]"
#BSUB -n 4
#BSUB -R "span[hosts=1]"
#BSUB -o Pi_serial_%J.out
#BSUB -e Pi_serial_%J.err
#BSUB -R "select[model == XeonGold6226R]"

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

time python chunk_pi.py 1
time python chunk_pi.py 2
time python chunk_pi.py 4
time python chunk_pi.py 6
time python chunk_pi.py 8
time python chunk_pi.py 10
time python chunk_pi.py 12
time python chunk_pi.py 14
time python chunk_pi.py 16