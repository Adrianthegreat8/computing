#aibanez1:04/18/2024:A22-nist.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Q1
data = np.loadtxt('Chwirut1.txt',skiprows=1)
print(data)
y,x = data[:,0],data[:,1]

#Q2
def my_model (x,b1,b2,b3):
    y = np.exp(-b1*x)/(b2+b3*x)
    return y

popt, pcov = curve_fit(my_model, x, y, [1.9027818370E-01,6.1314004477E-03,1.0530908399E-02])

#Q3
xsmall = np.arange(np.min(x),np.max(x)+0.1,0.5)
ypsmall = my_model(xsmall,*popt)

fig, ax = plt.subplots(2,1, figsize = (6,4))

ax[0].plot(x,y, '.',label = 'NIST data')
ax[0].plot(xsmall,ypsmall, 'r-', label = 'NIST model')
ax[0].set_xlabel('metal distance')
ax[0].set_ylabel('ultrasonic response')
ax[0].legend()
ax[0].grid()

#Q4
yp = my_model(x,*popt)
residuals = y - yp
ax[1].plot(x,residuals,'.')
y0small = np.zeros(xsmall.size)
ax[1].plot(xsmall,y0small,'r')
ax[1].set_xlabel('metal distance')
ax[1].set_ylabel('residuals')
ax[1].grid()

#Q5
SSR = np.sum(residuals**2)
print('Sum of Squares Residuals %e' % SSR)

#Q6
print(popt)

#Q7
perr = np.sqrt(np.diag(pcov))
print(perr)

#Q8
np.savetxt('results.csv', np.vstack([popt,perr]), fmt='%.4e', delimiter=',', header='b1,b2,b3')

plt.show()
