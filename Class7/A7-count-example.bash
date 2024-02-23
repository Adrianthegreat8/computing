#aibanez1:2/13/2024:A7-count-example.bash

c=0
for i in $@
do
  c=$((c+1))
done
echo The final count is: $c
