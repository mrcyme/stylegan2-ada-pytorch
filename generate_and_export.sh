#!/bin/bash
PKL_DIRECTORY=
PKL_LIST=
OUTDIR=
MODEL=oneline

conda activate StyleGan
i=1
for pkl in $PKL_LIST
do
  python generate.py --outdir=${OUTDIR}/${pkl} --filename="image" --trunc=0.9 --seeds=0-1024 --network=${PKL_DIRECTORY}/network-snapshot-00${pkl}.pkl
  python export_to_space.py --directory=${OUTDIR}/${pkl} --bucket=tattoos --destination=${MODEL}/i
  rm -r ${OUTDIR}/${pkl}
  i=$i+1
done
