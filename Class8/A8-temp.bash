#aibanez1:2/15/2024:A8-temp.bash

state=`cut -d' ' -f2 ./data-temp/temp-clean.dat | sort -u`

for i in $state
do
  if [ $i = CA ]
  then
    grep $i ./data-temp/temp-clean.dat | sort -nk3 | cut -d' ' -f3 | tail -1
  fi
done
