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

time python mandelbrot.py 1
time python mandelbrot.py 2
time python mandelbrot.py 3
time python mandelbrot.py 4
time python mandelbrot.py 5
time python mandelbrot.py 6
time python mandelbrot.py 7
time python mandelbrot.py 8
time python mandelbrot.py 9
time python mandelbrot.py 10
time python mandelbrot.py 11
time python mandelbrot.py 12
time python mandelbrot.py 13
time python mandelbrot.py 14
time python mandelbrot.py 15
time python mandelbrot.py 16