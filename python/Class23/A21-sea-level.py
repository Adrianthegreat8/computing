#aibanez1:04/16/2024:A21-sea-level.py

#QA

import pandas as pd
import numpy as np

df = pd.read_csv('sea-level_fig-1.csv', skiprows=7, usecols=[0,1], names=['Years','Sea Level'])
df.dropna(inplace=True)
print(df)

years, sea_level = np.array(df['Years']), np.array(df['Sea Level'])

#QB
sea_level = sea_level*2.54

#QC
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6,4))

plt.rcParams['font.size']=12
ax.plot(years, sea_level, 'b.', label='EPA data')
ax.set_xlabel('Years')
ax.set_ylabel('Sea Level')

#QD
model_func = np.poly1d(np.polyfit(years, sea_level, 1))

sea_level_predicted = model_func(years)
ax.plot(years, sea_level_predicted, 'r', label='linear model')

print(model_func.c)
print(model_func)

#QE
from sklearn.metrics import r2_score

r2 = r2_score(sea_level, sea_level_predicted)
print('R^2 =',r2) # R^2 ~~ 0.971

#QF
x_prediction = np.linspace(2025,2070,5)
sea_level_predicted2 = model_func(x_prediction)

#QG
ax.plot(x_prediction,sea_level_predicted2, 'gd', label='prediction')
ax.legend()
ax.grid()
fig.savefig('fig1.png')
plt.show()