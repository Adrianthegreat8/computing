#aibanez1:02/22/2024:ex5-space.py

#Q1
from math import sqrt, pi

#Q2
G=6.67*10**-11
Me=5.96*10**24
Re=6.36*10**6
Rs=4.00*10**5

#Q3
var1="International Space Station"

#Q4
print("%s orbits at %.0e m from Earth." %(var1,Rs))

#Q5
R=Re+Rs

#Q6
T=2*pi*sqrt((R**3)/(G*Me))

#Q7
print("The period is %.0f minutes." %(T/60))


