#!/bin/bash
min=100
x=`python get_pulse.py`
y=`echo "$x" | sort -n | awk '{a[NR]=$0}END{if(NR%2==1)print a[int(NR/2)+1];else print(a[NR/2-1]+a[NR/2])/2}'`
if [[ 1 -eq "$(echo "${y} < ${min}" | bc)" ]]
then
	echo "Signs of 'Trachycardia' Possible"
else
	echo "Healthy Life Owner Identified"
fi