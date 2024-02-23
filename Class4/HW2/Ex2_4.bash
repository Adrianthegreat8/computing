#aibanez1:2/4/2024:Ex2_4.bash

#Q0
cd ~/HW2
ls

#Q1
wc -cl 6KX7.pdb

#Q2
grep -e EXPDTA -e TITLE -e HEADER 6KX7.pdb

#Q3
grep -v -c SEQRES 6KX7.pdb

#Q4
grep -e GLU 6KX7.pdb
