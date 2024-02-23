#aibanez1:02/20/2024:ex3-f23.bash

#Q1
grep -v -e \# -e \% happiness.dat > mydata.dat

#Q2
awk '{printf "%s %f\n", $1, ($6/$5)*1000000000}' mydata.dat | sort -urnk2 | awk '{printf "%-10s %.1e\n", $1, $2}'

#Q3
awk '$2 == "Female" {print $1, $3}' mydata.dat | sort -nk2 | tail -1 | tr 0-9 ' ' | tr a-z A-Z
