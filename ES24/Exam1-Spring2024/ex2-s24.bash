#aibanez1:02/21/2024:ex2-s24.bash

rm first
rm second

for i in planets/*.bash
do
  echo $i | awk -F/ '{print $2}' | awk -F. '{print $1}' >> first

  . $i >> second 

done
paste -d, first second
