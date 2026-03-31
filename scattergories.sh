#!/bin/bash
seed=${1:-$(shuf -i 1-9999 -n 1)}
questions=$(cat questions.txt | tr '\t' '\n' | grep -v '^$' | awk -v seed=$seed 'BEGIN{srand(seed)} {a[NR]=$0} END{for(i=1;i<=12;i++){j=int(rand()*NR)+1; print a[j]; a[j]=a[NR-i+1]}}')
echo "Scattergories Game (Seed: $seed)"
echo "----------------"
echo "$questions" | nl -s ". "

