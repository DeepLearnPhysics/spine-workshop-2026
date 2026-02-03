#!/bin/bash

#SBATCH --account=m5252
#SBATCH --qos=shared
#SBATCH --constraint=gpu

#SBATCH --job-name=val_uresnet
#SBATCH --output=batch_outputs/output-val_uresnet.txt 
#SBATCH --error=batch_outputs/output-val_uresnet.txt

#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=6
#SBATCH --mem=16g
#SBATCH --time=0:10:00

srun -n 1 shifter --image deeplearnphysics/larcv2:ub2204-cu121-torch251-larndsim bash -c "python3 /global/cfs/cdirs/m5252/software/spine/bin/run.py -c /global/cfs/cdirs/m5252/dune/spine/train/example/uresnet_val.yaml"
