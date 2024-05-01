#aibanez1:04/21/2024:ex3-insulin.py

#Q1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Q2
df = pd.read_csv('mypatients.dat', header=0)
print(df)

#Q3
new_row = pd.DataFrame.from_dict({'name': ['John Smith'], 'mass': 45.6})
df = pd.concat([df, new_row], ignore_index=True)
print(df)

#Q4
def modelfunc (t,Co,m):
    C = Co * np.exp(-1 * (30*t) / m)
    return C

conc = modelfunc(5,85,df['mass'])

df['conc'] = conc
print(df)

#Q5
df = df.sort_values('conc')
print(df)

#Q6
fig, ax = plt.subplots()

indices = np.arange(len(df))
ax.bar(indices,np.array(df['conc']),label='conc')

ax.set_xticks(indices)
ax.set_xticklabels(df['mass'])

ax.tick_params(labelrotation=90)
ax.set_xlabel('mass (Kg)')
ax.set_ylabel('concentration (pmol/L)')
plt.legend()
plt.grid()
plt.show()