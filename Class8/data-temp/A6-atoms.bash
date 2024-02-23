#aibanez1:2/8/2024:A6-atoms.bash

#Q1
awk '$6 >= 28 {print}' atoms.pdb

#Q2
awk '$12 != "C" {print}' atoms.pdb

#Q3
awk '$3 == "N" && $4 == "LYS" && $6 == 9 {print}' atoms.pdb

#Q4
awk '$4 == "LYS" && ($6 == 9 || $6 == 28) {print}' atoms.pdb

#Q5
awk '$4 == "MET" {print $2, $3, $6}' atoms.pdb > MET.pdb

#Q6
awk '{print $3, ($7 + $8)/10, $11}' atoms.pdb

#Q7
awk '$4 == "HIS" {printf "%s %8.2f\n", "X:", $7}' atoms.pdb

#Q8
awk '{print ($7+$8+$9)/3}' atoms.pdb | sort -n | head -1
