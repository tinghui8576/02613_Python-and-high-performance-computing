#!/bin/bash
#BSUB -J jacobi
#BSUB -q hpc
#BSUB -W 20
#BSUB -R "rusage[mem=4GB]"
#BSUB -n 16
#BSUB -R "span[hosts=1]"
#BSUB -o jacobi_%J.out
#BSUB -e jacobi_%J.err
#BSUB -R "select[model == XeonGold6226R]"

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python stimulate.py 20 1
python stimulate.py 20 2 
python stimulate.py 20 4
python stimulate.py 20 8
python stimulate.py 20 16
python stimulate.py 20 32 
python stimulate.py 20 64
python stimulate.py 20 128 
python stimulate.py 20 256
# kernprof -l stimulate.py 20
# python -m line_profiler "stimulate.py.lprof" 