#aibanez1:02/20/2024:ex2-f23.bash

list=`ls dir1`
files=0
dirz=0

for i in $list
do
  if [ -f ./dir1/$i ]
  then
    files=$(( $files + 1 ))
  else
    dirz=$(( $dirz + 1 ))
  fi
done

echo The current number of files is $files
echo The current number of directories is $dirz
