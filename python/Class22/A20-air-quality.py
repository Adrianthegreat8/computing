#aibanez1:04/11/2024:A20-air-quality.py

#Q1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Q2
raw_data = pd.read_csv('air_quality_no2.csv', parse_dates=True)

#Q3
raw_data.head(4)

#Q4
raw_data.info()

#Q5
columns, rows = (raw_data.shape[0], raw_data.shape[1])
print(columns, 'columns')
print(rows, 'rows')

#Q6
if raw_data.duplicated().sum() > 0:
    print('There are', raw_data.duplicated().sum, 'rows, deleting them now.')
    raw_data.drop_duplicates(inplace=True)

#Q7
print(raw_data.isnull().sum())

#Q8
raw_data.dropna(axis=1, inplace=True)

#Q9
labels = raw_data.columns.values

#Q10
new_labels = [i.split('_')[1] for i in labels[1:]]
raw_data = raw_data.rename(columns={'station_paris': new_labels[0], 'station_london': new_labels[1]})

#Q11
max_NO2_paris_id = raw_data['paris'].idxmax()
time, NO2 = raw_data.iloc[max_NO2_paris_id]['datetime'],raw_data.iloc[max_NO2_paris_id]['paris']
print(time, NO2)

#Q12
print(raw_data)
df_mean = raw_data.iloc[:,1:].mean()
df_std = raw_data.iloc[:,1:].std()

paris_mean, london_mean = df_mean.iloc[0], df_mean.iloc[1]
paris_std, london_std = df_std.iloc[0], df_std.iloc[1]

print('London mean=%.2f and std=%.2f (ppb)' %(london_mean,london_std))
print('Paris mean=%.2f and std=%.2f (ppb)' %(paris_mean,paris_std))

#Q13
fig, ax = plt.subplots(figsize=(4,4))
plt.rcParams['font.size']=11
plt.rcParams['font.family']='Arial'

dates = np.array(raw_data.loc[:,'datetime'])
paris_data = np.array(raw_data.loc[:,['paris']])
london_data = np.array(raw_data.loc[:,['london']])

ax.plot(dates,paris_data, '-', label='paris')
ax.plot(dates,london_data, '-', label='london')
ax.tick_params(labelrotation=45)
ax.legend()
ax.set_ylabel('NO2 (ppb)')

plt.show()