#aibanez1:04/23/2024:ex1-f23-temperature.py

#Q0
#I promise not to communicate with another human being in any way about this exam.

#Q1
import numpy as np
import matplotlib.pyplot as plt

#Q2
data = np.loadtxt('temperature.csv',delimiter=',',skiprows=6)
year, temperature = data[:,0],data[:,1]

#Q3
tempaverage = temperature.mean()
highbool = temperature>0
lowbool = temperature<=0

highx,highy = year[highbool],temperature[highbool]
lowx,lowy = year[lowbool],temperature[lowbool]

#Q4
mymodel = np.poly1d(np.polyfit(year, temperature, 1))

xsmall = np.arange(np.min(year),np.max(year)+0.1,0.5)
ysmall=mymodel(xsmall)

#Q5
xp = np.arange(2025,2051,5)
yp = mymodel(xp)

#Q6
fig, ax = plt.subplots()

plt.rcParams['font.size']= 14
plt.rcParams['font.family']='Times'

ax.set_title('EPA - USA')
ax.plot(highx,highy, '.b',label = 'data above average')
ax.plot(lowx,lowy, '.r', label = 'data below average')
ax.plot(xsmall,ysmall, 'k-', label = 'linear model')
ax.plot(xp,yp,'.k', label = 'prediction')
ax.set_xlabel('hours since drug was administered')
ax.set_ylabel('amount of drug in body (mg)')

ax.legend()
ax.grid()

plt.show()

#Q7
yp_for_residuals = mymodel(year)
residuals = temperature-yp_for_residuals

SSR = np.sum(residuals**2)
print(SSR)
SST = ((temperature - temperature.mean())**2).sum()
R2 = 1-(SSR/SST)
print('The R-squared value is %.2f.' %R2)

#Q8
print('The last year the temperature was below the average was in %d.' %(lowx[np.argmax(lowx)]))