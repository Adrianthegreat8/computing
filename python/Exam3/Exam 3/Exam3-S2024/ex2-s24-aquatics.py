#aibanez1:04/24/2024:ex2-s24-aquatics.py

#Q1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Q2
df = pd.read_csv('GroundwaterChemistry.csv',comment='#',usecols=[2,20,21,22,23])

#Q3
print(df.head(4))

#Q4
df1bool = df['sampling_point']=='Pond Lab, Bush Well'
df1 = df[df1bool].drop('sampling_point',axis=1)
print(df1)

#Q5
df1.dropna(inplace=True)

#Q6
df1_stats = df1.describe()

#Q7
mean = df1_stats.iloc[1,:]
std = df1_stats.iloc[2,:]
stderr = std/np.sqrt(df1_stats.iloc[0,:])

fig, ax = plt.subplots()

labels = [i.replace('-IC','') for i in df1_stats.columns]
ax.bar(labels,mean, yerr=stderr, capsize=6, label='ion chromatography')

plt.rcParams['font.size']= 13
ax.set_ylabel('mg/L')

ax.legend()
ax.set_yticks(np.arange(0,100,20))
ax.grid(axis='y')
ax.set_title('Pond Lab, Bush Well')
plt.show()