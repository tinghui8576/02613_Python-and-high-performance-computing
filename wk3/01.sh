#!/bin/bash
#BSUB -J duplicate
#BSUB -q hpc
#BSUB -W 2
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=100MB]" 
#BSUB -o duplicate_%J.out 
#BSUB -e duplicate_%J.err
#BSUB -R "select[model == XeonGold6226R]"

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python -u 01duplicate.py


