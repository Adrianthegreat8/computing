#aibanez1:02/20/2024:ex2-fishery.bash

#Q1
grep 1960 fishery-production.csv > f1960
grep 1982 fishery-production.csv > f1982

#Q2
paste -d, ./f1960 ./f1982 > f1960-1982

#Q3
awk -F, '$1 == "American Samoa" {print $1, $8 - $4}' f1960-1982

#Q4
sort -t, -nk4 fishery-production.csv | tail -1 | awk -F, '{printf "Largest fishery production was %d metric tons in %d in %s\n", $4, $3, $2}'
