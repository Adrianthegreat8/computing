#aibanez1:2/18/2024:Ex4-symbols.bash

#Q1
symbols="BAC HD IBM JNJ MSFT PFE WMT XOM"

#Q2
for i in $symbols
do
  grep $i dow_jones_2011.dat > $i.dat
done

#Q3
for i in $symbols
do
  out=`sort -nk7 $i.dat | tail -1 | awk '{print $2, $3, $7}'`
  printf "%-5s %-12s %.1f\n" $out
done
