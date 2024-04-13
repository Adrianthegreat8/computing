#aibanez1:04/11:2024:A20-plants.py

#Q1
import numpy as np
import pandas as pd
df = pd.read_csv('plants_data.txt', index_col=0, sep='\s+')
print(df.head(3))

#Q2
surface_area = np.array(df['surface_area_km2'])
occurrence = np.array(df['occurrences'])
density = occurrence/surface_area

df.insert(3, 'density', density)

#Q3
df_sorted = df.sort_values('density', ascending=False)
print(df_sorted)

#Q4
import matplotlib.pyplot as plt
df_top5 = df_sorted.iloc[:5,:]

plt.figure(figsize=(7, 4))
plt.rcParams['font.size']=12
plt.rcParams['font.family']='Arial'

plt.bar(np.array(df_top5.index.values), np.array(df_top5['density']), label='top 5')

plt.title('Density of Plant Species')
plt.xlabel('Plant Species')
plt.ylabel('Density (Occurences per km^2')
plt.legend()
plt.grid(True, axis='y')

plt.show()