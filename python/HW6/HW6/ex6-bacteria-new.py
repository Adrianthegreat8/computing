#aibanez1:03/10/2024:ex6-bacteria-new.py

#Q1
from math import e

#Q2
k = 0.10661
A0 = 100.0

#Q3
times = list(range(1,37))

#Q4
numbac = [(A0*e**(k*x))for x in times]
print(numbac)

#Q5
index=times.index(13)
print('%.2e' %numbac[index])