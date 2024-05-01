#aibanez1:04/24/2024:ex1-s24-copper.py

#Q0
#I promise not to communicate with another human being in any way about this exam.

#Q1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Q2
data = np.loadtxt('Hahn1.csv',skiprows=5,delimiter=',')
y,x = data[:,0],data[:,1]

#Q3
def modelfunc (x,b1,b2,b3,b4,b5,b6,b7):
    y = (( b1 + (b2*x) + (b3 * (x**2)) + (b4 * (x**3))) / (1 + (b5*x) + (b6 * (x**2)) + (b7 * (x**3))))
    return y

bguess = [1.0776351733E+00, -1.2269296921E-01, 4.0863750610E-03, -1.4262662514E-06, -5.7609940901E-03, 2.4053735503E-04, -1.2314450199E-07]

popt, pcov = curve_fit(modelfunc, x, y, bguess)

#Q4
print(popt)

#Q5
perr = np.sqrt(np.diag(pcov))
print(perr)

#Q6
fig, ax = plt.subplots(figsize=(6,4))

modelx = np.linspace(np.min(x),np.max(x),200)
modely = modelfunc(modelx,*popt)

plt.plot(modelx,modely,'r-',label='model')
plt.plot(x,y,'.',label='data')

plt.rcParams['font.size']= 14
ax.set_xlabel(r'$temperature ({\degree}K)$')
ax.set_ylabel('coefficient of thermal expansion')

plt.legend()
plt.grid()
plt.show()

#Q7
names=['b1','b2','b3','b4','b5','b6','b7']

df = pd.DataFrame(np.vstack((popt,perr)).transpose(),columns=['estimate','std error'])
df['parameter'] = names
df = df.set_index('parameter')
print(df)