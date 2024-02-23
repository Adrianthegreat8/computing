#aibanez1:02/21/2024:EC-s4.bash

var=`echo 1 10,20 2,30 30,3 40`

for i in {1..4}
do
pairs=`echo $var | awk -F, -v i="$i" '{print $i}'`
. CL.bash $pairs
done
