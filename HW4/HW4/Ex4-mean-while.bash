#aibanez1:2/16/2024:Ex4-mean.bash

count=0
sum=0

while [ $count -lt 50 ]
do
  count=$(( $count + 1 ))
  sum=$(( $sum + $count))
done

average=$(( $sum / $count ))

echo The sum is $sum, the count is $count, and the average is $average
