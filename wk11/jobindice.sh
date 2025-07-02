#!/bin/bash
#BSUB -J Jindice
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=1GB]"
#BSUB -n 1
#BSUB -w ended(21241475)
#BSUB -R "span[hosts=1]"
#BSUB -o Jindice_%J.out
#BSUB -e Jindice_%J.err
#BSUB -R "select[model == XeonGold6226R]"

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613