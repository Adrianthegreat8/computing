#aibanez1:04/09/20204:ex10-chemistry

D={'Compound': ['Water', 'Ethanol', 'Carbon dioxide', 'Ammonia', 'Methane'],
    'Molecular Weight (g/mol)': [18.015, 46.07, 44.01, 17.031, 16.043],
    'Boiling Point (C)': [100, 78.37, -78.5, -33.34, -161.5],
    'Organic': [False, True, False, False, True]}

import pandas as pd
import numpy as np

#Q1
d1 = pd.DataFrame(D)
d1 = d1.set_index('Compound')
print(d1)

#Q2
print(d1.index.values)
print(d1.columns.values)

#Q3
d1.columns = ['Molecular Weight','Boiling Point','Organic']
print(d1)

#Q4
print(d1.loc[['Ethanol','Ammonia','Methane'],:])

#Q5
bool1 = (d1['Organic'] == True) & (d1['Molecular Weight'] > 30.0)
print(d1[bool1])

#Q6
bool2 = d1['Organic'] == False
print(d1[bool2][['Boiling Point','Molecular Weight']])