#aibanez1:04/18/2024:ex11-fluorsecence.py

#Q1
import numpy as np
data = np.loadtxt('ExpData-Fluorescence.csv',skiprows=1,delimiter=',')
x,y = data[:,0],data[:,1]

#Q2
from scipy.optimize import curve_fit

def mymodel (x,A,f,t1,t2,):
    y = A * ( (1-f) * np.exp( (-1*x) / t1 ) + ( f * np.exp( (-1*x) / t2 ) ) )
    return y

guess_arr = np.array([10,0.5,2.5,10])

popt, pcov = curve_fit(mymodel, x, y, guess_arr)

#Q3
import matplotlib.pyplot as plt

xsmall = np.arange(np.min(x),np.max(x)+0.1,0.5)
ysmall = mymodel(xsmall,*popt)

fig, ax = plt.subplots()

ax.plot(x,y, 'b.', label = 'experimental data')
ax.plot(xsmall,ysmall, 'r-', label = 'biexponential decay model')

ax.set_xlabel('time (ns)')
ax.set_ylabel('Fluorescence Intensity')

ax.grid()
ax.legend()

#Q4
fig1, ax1 = plt.subplots()

yp = mymodel(x,*popt)
residuals = y - yp
ax1.plot(x,residuals,'b.-')
y0small = np.zeros(xsmall.size)
ax1.plot(xsmall,y0small,'r--')
ax1.set_xlabel('time (ns)')
ax1.set_ylabel('residuals')
ax1.grid()

plt.show()

#Q5
"""
This is a good model as the residuals are grouped randomly around 0. If the residuals increased or decreased
systematically that would be an indication of a bad model.
"""

#Q6
print(popt) #this shows fitted parameters

#Q7
perr = np.sqrt(np.diag(pcov)) #std err is sqrt of the diagonals of perr
print(perr)

#Q8
import pandas as pd

L = ['A','f','tau1','tau2']
final = pd.DataFrame(np.vstack([popt,perr]).transpose())
final.index = L

print(final)

final.to_csv('results.csv', index=True, header=False, float_format='%.3f')