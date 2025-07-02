#!/bin/bash
#BSUB -J kernel
#BSUB -q c02613
#BSUB -n 4
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=4GB]"
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -W 1
#BSUB -o gpu_%J.out
#BSUB -e gpu_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python kernel.py