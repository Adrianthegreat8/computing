#aibaenz1:04/18/2024:ex11-radiative-forcing.py

#Q1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('climate-forcing_fig-1.csv', skiprows=6, index_col=0)
SE = np.std(data,axis=0)/np.sqrt(len(data))

averages = np.mean(data,axis=0)

print(averages)
print(SE)

fix, ax = plt.subplots()
ax.bar(averages.index,averages, yerr=SE, capsize = 6, label = 'data from 1979 to 2019')
ax.grid(visible=True, which='major', axis='y', color='grey', linestyle='-')
ax.tick_params(labelrotation=45)
plt.rcParams['font.size']=12
ax.legend()
ax.set_ylabel(r'$radiative forcing(W{\bullet}m^{-2})$')


#Q2
y = np.array(data['Carbon dioxide'])
x = np.array(data.index)

mymodel = np.poly1d(np.polyfit(x,y,1))

print(mymodel.c) #keep

linearmodel = mymodel(x)

xpredicted = np.arange(2020,2031,5)
ypredicted = mymodel(xpredicted)

fig1, ax1 = plt.subplots()
ax1.plot(x,y,'b.',label='Carbon dioxide data')
ax1.plot(x,linearmodel,'r-',label='linear model')
ax1.plot(xpredicted,ypredicted,'gd',label='prediction')

ax1.set_xlabel('year')
ax1.set_ylabel(r'$radiative forcing(W{\bullet}m^{-2})$')
plt.rcParams['font.size'] = 12
ax1.grid()
ax1.legend()

SSR = ((y - linearmodel)**2).sum()
SST = ((y - y.mean()) ** 2).sum()
R2 = 1-(SSR/SST)
print(R2)

plt.show()