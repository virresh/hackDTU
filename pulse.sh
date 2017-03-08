#!/bin/bash
min=100
x=`python get_pulse.py` #Calling the final python pulse detector
y=`echo "$x" | sort -n | awk '{a[NR]=$0}END{if(NR%2==1)print a[int(NR/2)+1];else print(a[NR/2-1]+a[NR/2])/2}'` #Getting the median heart beat rate for more accuracy
if [[ 1 -eq "$(echo "${y} > ${min}" | bc)" ]]
then
	# echo "Signs of 'Trachycardia' Possible"
	z=`python questionnaire.py` #Display the questionnaire, if the heart beat rate exceeds the limit of a normal one.
	i=0
	# echo $z
	a=()
	for var in $z; do
		a[i]=$var
		i=$i+1
	done
	#Run python scripts according to priority of questions
	if [[ ${a[0]} -eq 1 ]]
	then
		python first.py
	else
		if [[ ${a[1]} -eq 1 ]]; then
			python second.py
		else
			if [ ${a[2]} -eq 1 ] || [ ${a[3]} -eq 1 ] || [ ${a[4]} -eq 1 ] ]; then
				python third.py
			else
				if [[ ${a[5]} -eq 1 ]]; then
					python sixth.py
				else
					if [[ ${a[6]} -eq 1 ]]; then
						python seventh.py
					else
						if [[ ${a[7]} -eq 1 ]]; then
							python eight.py
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
