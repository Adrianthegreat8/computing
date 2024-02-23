#aibanez1:02/19/2024:ex2-f22-flow.bash

count1=0
count2=0

for i in $@
do
  res=$(( $i / 4 ))
  if [ $res -gt 0 ]
  then
    count1=$(( $count1 + 1 ))
  elif [ $res -lt 0 ]
  then
    count2=$(( $count2 + 1 ))
  else
    echo $i/4 reults in zero
  fi
done

echo $count1 ' results are > 0'
echo $count2 ' results are < 0'
