#aibanez1:02/19/2024:ex3-f22-cars.bash

#Q1
lines=`wc mtcars.csv | awk '{print $1}'`
lines1=$(( $lines - 1 ))
tail -$lines1 mtcars.csv > mtcars_data.csv

#Q2
sort -t, -nk2 mtcars_data.csv | cut -d, -f1,2,7 | tr , : > mpg_sorted.dat

#Q3
mpg=`head -5 mpg_sorted.dat | awk -F: '{print $2}'`

#Q4
av_mpg=`echo $mpg | awk '{print ($1+$2+$3+$4+$5)/5}'`

#Q5
av_weight5=4.6858
printf "The average wieght is %.0f and has mpg of %.1f\n" $av_weight5 $av_mpg

