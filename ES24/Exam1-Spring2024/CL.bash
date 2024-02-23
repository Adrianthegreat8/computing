#aibanez1:02/21/2024:CL.bash

numbers=$@

first=`echo $numbers | awk '{print $1}'`
second=`echo $numbers | awk '{print $2}'`

if [ $first -gt $second ]
then
  echo greater, here is the difference: $(( first - second ))
else
  echo smaller or equal
fi
