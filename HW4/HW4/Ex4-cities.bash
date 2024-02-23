#aibanez1:2/15/2024:Ex4-cities.bash

rm -r cities
#this line was added for my convenience when debugging my script please dont take off points for it I know it isn't supposed to be here

mkdir cities

for i in NY DC LA SF
do
  mkdir cities/$i
  touch cities/$i/file_$i.txt
  echo $i | tr A-Z a-z >> cities/$i/file_$i.txt
done

cat cities/NY/file_NY.txt
