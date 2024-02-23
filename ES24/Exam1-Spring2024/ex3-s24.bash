#aibanez1:02/21/2024:ex3-s24.bash

#Q1
grep -v -e '>' -e '*' galaxies_raw.dat > galaxies.dat

#Q2
galz=`awk '(($2 > 8000) || ($2 < 4000)) && ($3 > 10.0) {print}' galaxies.dat | wc -l`

#Q3
echo The number of galaxies with velocity \< 4000 and \> 8000 is $galz

#Q4
awk '$3 < -40 {printf "v=%.2e km/s %10.2f mJy\n", $2, $3}' galaxies.dat
