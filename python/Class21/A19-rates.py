#aibanez1:04/09/2024:A19-rates.py

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian']
heart_rates = [72, 65, 70, 75, 78, 80, 85, 90, 95]

#Q1
import pandas as pd
import numpy as np

#Q2
ser1 = pd.Series(heart_rates,names)
print(ser1)

#Q3
print(ser1.index.values)

#Q4
print(ser1.values)

#Q5
print(ser1.iloc[:4])
#iloc[] is easier because you can slice using index values instead of hardcoding the data labels.

#Q6
print(ser1.loc[['Bob','Eva','Grace']])
#loc[] is easier here because we can simply call the labels of the values we want.
# If we used iloc[] we would need to find the indecies of the values first and then call the items

#Q7
bool1 = (ser1 > 70) & (ser1 < 90)
ser2 = ser1.loc[bool1]
print(ser2)

#Q8
ser3 = ser1.iloc[np.array(bool1)]
print(ser3)

#Q9
selected_cities = ['New York', 'Los Angeles', 'Houston', 'Chicago', 'Philadelphia']

data = {'New York': 75,
    'Los Angeles': 80,
    'Chicago': 70,
    'Houston': 85,
    'Phoenix': 90,
    'Philadelphia': 78,
    'San Antonio': 87,
    'San Diego': 82,
    'Dallas': 88}

cities = pd.Series(data).loc[selected_cities]
print(cities)




