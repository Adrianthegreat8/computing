#aibanez1:2/13/2024:A7-sum-example.bash

s=0
for i in $@
do
  s=$((s+$i))
done
echo The final sum is: $s

#. A7.sum-example.bash {1..1000}
