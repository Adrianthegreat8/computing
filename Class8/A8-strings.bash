#aibanez1:2/15/2024:A8-strings.bash
color=$@

if [ $color = blue ]
then
  echo $color is a relaxing color
elif [ $color = red ]
then
  echo $color is an exciting color
else
  echo you should enter either red or blue
fi
