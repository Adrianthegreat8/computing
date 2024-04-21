#aibanez1:04/19/2024:snowgone.py

#QA
import numpy as np
import pandas as pd

#QB
C = pd.read_csv('snowdata.csv',skiprows=1)
print(C) #keep

#QC
import matplotlib.pyplot as plt
week,depth = np.array(C['week']),np.array(C['depth'])

#QD
model_func = np.poly1d(np.polyfit(week, depth, 2))
print(model_func.c)

#QE
yp = model_func(week)

SSR = ((depth - yp)**2).sum()
SST = ((depth - depth.mean())**2).sum()
R2 = 1-(SSR/SST)
print('The R-squared value is %.2f' % R2)

#QF
predweek = np.arange(week[-1],25.5,.5)
preddepth = model_func(predweek)

#QG
snowgonebool = preddepth >= 0
snowgonearr = preddepth[snowgonebool]
ind = np.argmin(snowgonearr)

gonedepth = snowgonearr[-1]
goneweek = predweek[ind]

print('The snow gone week is %.1f' % goneweek)

#QI
fig, ax = plt.subplots()
ax.plot(week,depth,'b.',label='data',)
# ax.plot(predweek,preddepth,'r-',label='fit')

xsmall = np.arange(np.min(week),goneweek+.5,0.5)
ysmall = model_func(xsmall)
ax.plot(xsmall,ysmall,'-r',label='fit')
ax.plot(goneweek,0,'dg',label='snow gone week')

ax.set_xticks([5,10,15])
ax.set_xlabel('week number')
ax.set_ylabel('depth of snow in inches')
ax.grid()
plt.show()


#
