#aibanez1:2/13/2023:A7-loop-letters.bash

for n in {a..z}
do
echo $n | tr a-z A-Z > file-$n.txt
done

