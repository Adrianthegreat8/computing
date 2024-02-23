#aibanez1:2/6/2024:A5-eeg.bash

#Q1
grep -v \# eeg-control.dat > eeg.dat

#Q2
echo \#data are sorted according to voltage values > eeg-sorted.dat

#Q3
sort -nk4 eeg.dat >> eeg-sorted.dat

#Q4
v1=`grep -c FP1 eeg.dat`

#Q5
echo There are $v1 recorded values FP1

#Q6
grep Y eeg.dat | sort -nk4 | tail -1 | cut -d" " -f4

#Q7
tr " " ":" < eeg.dat | tail -5

#Q8
tr " " "," < eeg.dat > eeg1.dat

#Q9
grep -e FP1 -e FP2 eeg1.dat > FP12.dat

#Q10
grep FP1 eeg.dat | grep " 1 "
