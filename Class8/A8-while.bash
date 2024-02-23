#aibanez1:2/15/2024:A8-while.bash

#Q1
myvar=10
while [ $myvar -ne 10 ]
do
  echo $myvar
  myvar=$(( myvar + 1 ))
done

#Q2
myvar=1
while [ $myvar -ne 0 ]
do
  echo $myvar
  myvar=$(( myvar + 1 ))
done
