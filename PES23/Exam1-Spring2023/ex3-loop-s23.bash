#aibanez1:02/20/2024:ex3-loop-s23.bash

#Q1
x=`tail -649 fishery-production.csv | awk -F, '{print $2}' | sort -u`

#Q2

for i in $x
do 
  if [ $i = ARG ] 
  then 
    tail -649 fishery-production.csv | awk -F, '{printf "%s,%s\n", $1, $2}' | sort -u | awk -F, '$2 == "ARG" {print $1}'
  else  
    echo $i
  fi
done
