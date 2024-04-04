#aibanez1:04/2/2024:A17-cones.py

import numpy as np

d = [0.2,1.0,1.5,3.0,-1.0,4.2,3.14]
h = [0.0400,1.0000,2.2500,9.0000,1.0000,17.6400,9.8596]

#Q1
D = np.array(d)
H = np.array(h)

V = (1/12)*np.pi*(D**2)*H
print(V)

#Q2
mean = np.mean(V)
stdev = np.std(V)

print('The average is %.2f and std is %.2f' % (mean,stdev))