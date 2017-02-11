#!/bin/bash
min=100
x=`python get_pulse.py`
y=`echo "$x" | sort -n | awk '{a[NR]=$0}END{if(NR%2==1)print a[int(NR/2)+1];else print(a[NR/2-1]+a[NR/2])/2}'`
if [[ 1 -eq "$(echo "${y} > ${min}" | bc)" ]]
then
	# echo "Signs of 'Trachycardia' Possible"
	z=`python questionnaire.py`
	i=1
	a=()
	for var in $z; do
		a[i]=$var
		i=$i+1
	done

	if [[ $a[0] -eq 1 ]]
	then
		python first.py
	else
		if [[ $a[1] -eq 1 ]]; then
			python second.py
		else
			if [[ $a[2] -eq 1 -o $a[3] -eq 1 -o $a[4] -eq 1 ]]; then
				python third.py
			else
				if [[ $a[5] -eq 1 ]]; then
					python sixth.py
				else
					if[[ $a[6] -eq 1 ]]; then
						python seventh.py
					else
						if [[ $a[7] -eq 1 ]]; then
							python eighth
						else
							echo "I don't know !!!"
						fi
					fi
				fi
			fi
		fi
	fi

else
	echo "Healthy Life Owner Identified"
fi