#aibanez1:04/09/2024:A19-fundamental.py

physics_data = {
    'Parameter': ['Mass', 'Length', 'Time', 'Velocity', 'Acceleration'],
    'Value': [0.1, 2.5, 0.05, 10, 9.8],
    'Unit': ['kg', 'm', 's', 'm/s', 'm/s^2'],
    'Fundamental': [True, True, True, False, False]}

#Q1
import pandas as pd
import numpy as np

#Q2
physics_data_frame = pd.DataFrame(physics_data)
print(physics_data_frame)

#Q3
physics_data_frame_rows = physics_data_frame.index.values
print(physics_data_frame_rows)

#Q4
physics_data_frame_column_label = physics_data_frame.columns.values
print(physics_data_frame_column_label)

#Q5
print(physics_data_frame.loc[:,'Parameter'])

#Q6
print(physics_data_frame.loc[[1,3,4],:])

#Q7
print(physics_data_frame[['Parameter','Unit']])

#Q8
print(physics_data_frame.Fundamental)

#Q9
bool1 = (physics_data_frame['Fundamental'] == True) & (physics_data_frame['Value'] >= 1)
print(physics_data_frame[bool1])

#Q10
bool2 = (physics_data_frame['Unit'] == 'kg') | (physics_data_frame['Unit'] == 's')
print(physics_data_frame.loc[bool2,['Parameter','Unit']])