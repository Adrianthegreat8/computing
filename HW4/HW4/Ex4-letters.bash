#aibanez1:2/16/2024:Ex4-letters.bash

rm letters.txt
#same with this line :)

count=0

for i in $@
do
  echo $i >> letters.txt
  count=$(( $count + 1 ))
done

echo The file letters.txt contains $count letters.

#. Ex4-letters.bash a b c d e
