# aibanez1:04/21/2024:ex1-games.py
import numpy as np
# I will not communicate in any way, with any other person about this exam.

# Q1
import pandas as pd

# Q2
df = pd.read_csv('video_games.csv', header=0)

# Q3
rows, columns = df.shape
print('There are', rows, 'rows and', columns, 'columns')

# Q4
df.drop_duplicates(inplace=True)

# Q5
rows, columns = df.shape
print('Yes, I have duplicates, and now there are', rows, 'and', columns, 'columns')

# Q6
print(df.isnull().sum())

# Q7
df.dropna(inplace=True)

# Q8
print(df.columns.values)

# Q9
df = df.drop(['NA_Sales', 'Critic_Score', 'User_Score', 'Global_Sales'], axis=1)
print(df.iloc[:2])

# Q10
new_labels = [i.split('_')[0] for i in df.columns.values]
df.columns = new_labels
print(new_labels)

# Q11
dfbool = (df['Year'] >= 2011) & (df['JP'] > df['EU']) & (df['Developer'] == 'Nintendo')
df = df[dfbool]
print(df[['Name', 'Genre']])