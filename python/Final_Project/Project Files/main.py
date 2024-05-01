#plot united states gdp growth against unemployment

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('cpsaat01.csv',skiprows=6,index_col=0)

data = data.iloc[:,8]
data.dropna(inplace=True)
Unemployment_DATA = data

data1 = pd.read_csv('API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_84037.csv',skiprows=3,header=0,index_col=0)
GDP_DATA = data1.loc['United States'][4:-2]

fig, ax = plt.subplots(figsize = (7,7))

ax.plot(Unemployment_DATA.index.values,Unemployment_DATA[:],'.b',label='Unemployment Rate')
ax.tick_params(labelrotation=90)

plt.legend()
plt.rcParams['font.size']= 11
plt.rcParams['font.family']='Times'


plt.show()