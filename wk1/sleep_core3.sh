#!/bin/bash
#BSUB -J sleepjob1
#BSUB -q hpc
#BSUB -W 2
#BSUB -n 64
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=500MB]" 
#BSUB -o sleeper_%J.out 
#BSUB -e sleeper_%J.err
#BSUB -R "select[model == XeonE5_2660v3]"


sleep 100