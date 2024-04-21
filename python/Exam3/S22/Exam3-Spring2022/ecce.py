#aibanez1:04/21/2024:ecce.py

#QA
import numpy as np

#QB
def eccentricity (a,b):
    e = np.sqrt(1-((b/a)**2))
    return e

#QC
a_v = np.random.randint(20,31,10)

#QD
b_v = np.random.randint(2,11,10)

#QE
eccen_v = eccentricity(a_v, b_v)

#QF
highindecies = eccen_v > 0.95
eccen_v = eccen_v[highindecies]
a_v = a_v[highindecies]
b_v = b_v[highindecies]

for e, a, b in zip(eccen_v, a_v, b_v):
    print('%.2f %d %d' %(e,a,b))


