#aibanez1:2/13/2024:A7-loop-var.bash

var='AZ CA CO NV NM UT'

for i in $var
do
  grep $i data-temp/temp.dat | sort -nk3 | head -1
done
