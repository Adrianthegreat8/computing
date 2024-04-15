#aibanez1:04/14/2024:ex10-sources.py

#Q1
import numpy as np
import pandas as pd

df = pd.read_csv('energy-sources.txt', delimiter=':', comment='#')
print(df)

#Q2
total_energy = df['energy'].sum()
print('In 2022, total U.S. energy consumption was equal to %.1f quadrillion Btu.' % total_energy)

#Q3
percentage = np.array((df['energy']/total_energy)*100)
df.insert(3, 'percentage', percentage)
print(df)

#Q4
renewable_bool = df['renewable'] == True
renewable = df[renewable_bool]
renewable_contribution = renewable['percentage'].sum()

nonrenewable_bool = df['renewable'] == False
nonrenewable = df[nonrenewable_bool]
nonrenewable_contribution = nonrenewable['percentage'].sum()

print('Renewable energy contributes to %.2f%%' %renewable_contribution)
print('Non-renewable energy contributes to %.2f%%' %nonrenewable_contribution)

#Q5
newdf = pd.DataFrame(nonrenewable.iloc[:,[0,3]])
new_row = pd.DataFrame.from_dict({'source': ['Renewable'], 'percentage': renewable_contribution})
newdf = pd.concat([newdf,new_row],ignore_index=True)
print(newdf)

#Q6
import matplotlib.pyplot as plt

newdf = newdf.sort_values('percentage')
print(newdf)

plt.figure(figsize=(6, 4))
plt.rcParams['font.size']=12
plt.rcParams['font.family']='Arial'

plt.barh(np.array(newdf['source']),np.array(newdf['percentage']))

plt.title('US Energy Consumption by Source, 2022')
plt.xlabel('Energy Consumption (%)')
plt.grid(True, axis='x')

plt.show()
