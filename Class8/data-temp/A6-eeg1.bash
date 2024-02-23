#aibanez1:2/8/2024:A6-eeg1.bash

#Q1
count=$(awk -F, '$4 > 10 && $2 == "FP1" {print}' eeg1.dat | wc -l)

#Q2
var=FP2
awk -F, -v var="$var" '$2 == var {print}' eeg1.dat

#Q3
awk -F, '{print}' eeg1.dat | sort -t, -nk4 | tail -1 | awk -F, '{printf "highest voltage=%.2f mV t=%.0f ms  channel=%s\n", $4, $3, $2}' 
