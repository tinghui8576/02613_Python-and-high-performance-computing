#!/bin/bash
#BSUB -J sleepjob1
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=100MB]" 
#BSUB -o sleeper_%J.out 
#BSUB -e sleeper_%J.err
sleep 60