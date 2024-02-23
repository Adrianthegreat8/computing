#aibanez1:2/8/2024:Ex3-stock.bash

#Q1
awk '$1==2 && ($2=="JNJ" || $2=="PFE") {print $1, $2, $4, $7}' dow_jones_2011.dat

#Q2
awk '{print $1, $2, (($7-$4)/$4)*100}' dow_jones_2011.dat > diff_week.dat

#Q3
awk '$3>7 && $3<=10 {printf "%-6s %.2f\n", $2, $3}' diff_week.dat 
###WORK IN PROGRESS FINISH BEFORE SUBMITTING

#Q4
sed 's/ /:/g' dow_jones_2011.dat > dow_jones_2011_new.dat

#Q5
sort -t: -nk5 dow_jones_2011_new.dat | tail -1 | awk -F: '{printf "highest price=$%.1f stock=%s date %s\n", $5, $2, $3}'
