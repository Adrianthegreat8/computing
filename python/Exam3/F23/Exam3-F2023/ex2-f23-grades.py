#aibanez1:04/23/2024:ex2-f23-grades.py

#Q1
import pandas as pd
import matplotlib.pyplot as plt

#Q2
df = pd.read_csv('grades.dat',delimiter=':')
print(df.head())

#Q3
import numpy as np
collumn_label = np.array(df.columns.values)
print(collumn_label)

#Q4
new_col_label = [i.replace('*','') for i in collumn_label]
print(new_col_label)

df.columns = new_col_label
print(df)

#Q5
print(df.describe().iloc[[1,2],1])

#Q6
print(df.iloc[df['exam'].idxmin()])

#Q7
grade = df['quiz']*0.25 + df['exam']*.5 + df['HW']*.25
df['grade'] = grade

print(df)

#Q8
gradebool = df['grade'] > 90
df1 = df[gradebool]
df1 = df1[['name','grade']].reset_index()
print(df1)

#Q9
A = df['grade'][df['grade']>=90].size
B = (df['grade'][((df['grade']<90) & (df['grade']>=80))]).size
C = df['grade'][((df['grade']<80) & (df['grade']>=70))].size
D = df['grade'][((df['grade']<70) & (df['grade']>=60))].size
F = df['grade'][df['grade']<60].size

fig, ax = plt.subplots()

ax.bar(['A','B','C','D','F'],np.array([A,B,C,D,F]),label = 'data above average')
ax.set_xlabel('grades')
ax.set_ylabel('number of students')

plt.show()