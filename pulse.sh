#!/bin/sh
x=`python get_pulse.py`
echo "$x" | sort -n|awk '{a[NR]=$0}END{if(NR%2==1)print a[int(NR/2)+1];else print(a[NR/2-1]+a[NR/2])/2}'