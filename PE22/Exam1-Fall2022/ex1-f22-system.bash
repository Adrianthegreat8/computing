#aibanez1:2/19/2024:ex1-f22-system.bash

#Q0 
#I promise not to communicate with another human being in any way about this exam.

#Q1

#Q1.1
cat script1.bash
. script1.bash

#Q1.2
printf "#aibanez1:02/19/2024:script1.bash \necho this is my location \npwd \n" > script1-fixed.bash

#Q2
var="# script1.bash has been fixed #"

#Q3
echo $var >> script1.bash

#Q4
paste -d " " ./files/file\${1..3} | tr '@31' 'aei'

#Q5
cp ./files/??[!123] ../

#Q6
n1=2
. script2.bash 2> /dev/null | sort -nk$n1

