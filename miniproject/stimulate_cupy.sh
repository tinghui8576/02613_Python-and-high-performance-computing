#!/bin/bash
#BSUB -J jacobi
#BSUB -q c02613
#BSUB -n 4
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=4GB]"
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -W 20
#BSUB -o jacobi_%J.out
#BSUB -e jacobi_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

# python stimulate_cupy.py 20 

nsys profile -o jacobi_profile python stimulate_cupy.py 20 
nsys stats jacobi_profile.nsys-rep 