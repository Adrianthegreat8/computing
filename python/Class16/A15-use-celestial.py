#aibanez1:03/14/2024:A15-celestial.py

#QA
import celestial

#QB
print('The surface acceleration due to gravity of jupiter is %.2f m/s2' %celestial.Dg['jupiter'])

#QC
a,b=celestial.planet_weight('jupiter', 100)
print('Weight on %s is %.2f Kg' %(a,b))

#QD
L = [celestial.planet_weight(i,100) for i in celestial.Dg.keys()]
print(L)