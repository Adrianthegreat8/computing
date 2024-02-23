#aibanez1:2/8/2024/Ex3-artists.bash

#Q1
var=$(sort -t: -nk1 music-artists.dat | tail -1 | cut -d: -f2,3 | tr a-z A-Z)

#Q2
echo $var | sed 's/:/ - /'

#Q3
grep -e BAC -e RIES music-artists.dat | sed 's/BAC/BACH/' | tr -s 'S'

#Q4
grep Stephen music-artists.dat | grep HELLER >> music-artists.dat 

#Q5
cat music-artists.dat

#Q6
head -5 music-artists.dat| cut -c 1-6 | tr A-Z a-z

#Q7
. script.bash 2> /dev/null | sed 's/#/ \n/'
