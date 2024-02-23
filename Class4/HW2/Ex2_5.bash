#aibanez1:2/4/2024:Ex2_5.bash

#Q0
cd ~/HW2

#Q1
sort -t":" -nk3 amino_hydro_weight.dat

#Q2
cut -d":" -f1,3 amino_hydro_weight.dat

#Q3
paste -d"*" file{1,2,1}

#Q4
cat file{1,2,1}

#Q5
sed 's/Chile/Vinile/' file2

#Q6
price=173.531
stock="IBMComp"
date="5/6/2011"

printf "highest price=$%.1f stock=%.3s date %.8s\n" $price $stock $date
