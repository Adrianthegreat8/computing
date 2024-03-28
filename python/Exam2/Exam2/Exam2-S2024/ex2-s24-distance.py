#aibanez1:03/27:ex2-s24-distance.py

#Q1
from math import sin, cos, pi, sqrt

#Q2
def distance (r, theta, z):
    x = r * cos(theta)
    y = r * sin(theta)
    d = sqrt((x**2)+(y**2)+(z**2))
    return d

#Q3
r1=[4,2,-3,3] #r
z1=[-2,-1,-5,1] #z
P=['P1','P2','P3','P4'] #point names
theta1 = [(2*pi)/3, pi/3, pi/2, pi] #theta

zipped = list(zip(r1,theta1,z1,P))

Ldistance = [distance(i[0], i[1], i[2]) for i in zipped]

largestD = max(Ldistance)
indexLargestD = Ldistance.index(largestD)
largestDName = P[indexLargestD]

print('The point with maximum distance is', largestDName)