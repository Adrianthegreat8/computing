#aibanez1:2/1/2024:A4-textpro.bash

#Q1
wc -l temp.dat

#Q2
head -10 temp.dat

#Q3
grep CA temp.dat

#Q4
grep -c CA temp.dat

#Q5
grep -v \# temp.dat

#Q6
grep -e CA -e CO temp.dat

#Q7
grep -c -e CA -e CO temp.dat

#Q8
grep -c -v -e UT -e CO temp.dat

#Q9
# a space " "

#Q10
sort -n -k3 temp-clean.dat

#Q11
cut -f1 -d" " temp-clean.dat

#Q12
cut -c 1-4 temp-clean.dat

#Q13
#a colon ":"

#Q14
sort -t":" -k2 temp-clean1.dat

#Q15
cut -f2,3 -d":" temp-clean1.dat
