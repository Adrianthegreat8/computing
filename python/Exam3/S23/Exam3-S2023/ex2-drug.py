#aibanez1:04/21/2024

#Q1
import numpy as np
import matplotlib.pyplot as plt

#Q2
data = np.loadtxt('drugtime.csv', delimiter=',')
print(data)

#Q3
hour,amount = data[0,:],data[1,:]

#Q4
amount = np.abs(amount)

#Q5
from scipy.optimize import curve_fit
def modelfunc(x,a,b):
    y = a * np.exp(b*x)
    return y

popt, pcov = curve_fit(modelfunc, hour, amount, [9.83372499e+02, -1.06230041e-01] )
print(popt)

#Q6
xsmall = np.linspace(0,81,100)
ypsmall = modelfunc(xsmall,*popt)

fig, ax = plt.subplots()

ax.plot(hour,amount, '.b',label = 'data')
ax.plot(xsmall,ypsmall, 'r-', label = 'exponential fit')
ax.set_xlabel('hours since drug was administered')
ax.set_ylabel('amount of drug in body (mg)')
plt.rcParams['font.size']= 14
ax.legend()
ax.grid()

plt.show()

#Q7
five_hr_est = modelfunc(5,*popt)
print('The amount of drug after 5 hours is %.3f mg' % five_hr_est)