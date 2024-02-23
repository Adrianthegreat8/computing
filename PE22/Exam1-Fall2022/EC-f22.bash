#aibanez1:02/19/2024:EC-f22.bash

lines=`wc -l mpg_sorted.dat | awk '{print $1}'`
group=1
groups=$(( $lines / 4 ))

while [ $group -le $groups ]
do
 
  block_mpg=`head -$(( 4 * $group )) mpg_sorted.dat | tail -4 | awk -F: '{print $2}'`
  avg_mpg=`echo $block_mpg | awk '{print ($1+$2+$3+$4)/4}'`

  block_weight=`head -$(( 4 * $group )) mpg_sorted.dat | tail -4 | awk -F: '{print $3}'`
  avg_weight=`echo $block_weight | awk '{print ($1+$2+$3+$4)/4}'`

  printf "%-6.1f %.1f\n" $avg_mpg $avg_weight
  group=$(( $group + 1 ))

done
