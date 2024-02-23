echo Y T I L I B A  | tr ' ' '\n' > file1
echo {7..1}| tr ' ' '\n' > file2
paste file1 file2

rm file{1,2}

Ops error
