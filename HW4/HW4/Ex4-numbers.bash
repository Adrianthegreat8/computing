#aibanezx1:2/16/2024:Ex4-numbers.bash

for i in {1..40}
do
  test=$(( $i % 2 ))
  if [ $test -eq 0 ]
  then
    echo $i >> even.out
  else
    echo $i >> odd.out
  fi
done
