#!/bin/bash
#BSUB -J bloc
#BSUB -q hpc
#BSUB -W 2
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=40GB]" 
#BSUB -o bloc_%J.out 
#BSUB -e bloc_%J.err
#BSUB -R "select[model == XeonGold6226R]"

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python -u 2_1.py 256
python -u 2_1.py 512
python -u 2_1.py 1024
