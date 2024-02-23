#aibanez1:2/6/2024:A5-stream.bash

#Q1
. t1.bash 
#both stdout and stderr are sent to the screen

#Q2
. t1.bash 2> t1.out
#stderr is redirected to t1.out and stdout is sent to the screen

#Q3
. t1.bash > t1.out
#stderr is redirected to screen and stdout is sent to t1.out

#Q4
. t1.bash >> t1.out
#stderr is sent to screen and stdout is appended to t1.out

#Q5
. t1.bash &> t1.out
#both stderr and stdout is sent to t1.out

#Q6
var=`. t1.bash`
#stderr is sent to the screen. stdout is sent to var in one line

#Q7
. t1.bash 2> /dev/null | tr a-z A-Z
#stdout is sent to the screen and capitalized. stderr is sent to /dev/null

#Q8
echo Hello, I can get it | tr 'eat,' '3@9*'

