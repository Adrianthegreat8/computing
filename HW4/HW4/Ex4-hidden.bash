#aibanez1:2/15/2024:Ex4-hidden.bash

scripts=`ls -a scripts/.*.bash`

rm stdout.txt

for i in $scripts
do
  . $i >> stdout.txt
done
