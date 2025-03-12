#!/bin/bash
#BSUB -J Hsine
#BSUB -q hpc
#BSUB -W 2
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=1GB]"
#BSUB -o hsine_%J.out
#BSUB -e hsine_%J.err
#BSUB -R "select[model == XeonGold6226R]"

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python -m cProfile -o haversine.prof Haversine.py locations.csv