#aibanez1:2/9/2024:Ex3-misc.bash

#Q1
grep -v \# species.dat | sed 's/*//g' > species-clean.dat

#Q2
awk -F, '{print $2}' species-clean.dat | sort -n | tail -1
#this code shows the largest island in the dataset

#Q3
var1=40
awk -F, -v a="$var1" '$3>a {print $1}' species-clean.dat 

#Q4
awk -F, '{print ($3/$2), $1}' species-clean.dat | sort -n | awk '{printf "%-10.1e %s\n", $1, $2}' | tr a-z A-Z
