#aibanez1:02/27/2024:ex5-bacteria.py

import math as m

k=0.10661
t=36

Ao=float(input("Input Ao: "))

Abac = Ao * m.exp(k*t)

print("The number of bacteria will be %.1e" %(Abac))