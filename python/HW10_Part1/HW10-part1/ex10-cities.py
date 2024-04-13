#aibanez1:04/09/2024:ex10-cities.py

D = {'New York': 8500000,
    'Los Angeles': 4000000,
    'Chicago': 2700000,
    'Houston': 2300000,
    'Phoenix': 1600000,
    'Philadelphia': 1500000,
    'San Antonio': 1400000,
    'San Diego': 1300000,
    'Dallas': 1200000}

import pandas as pd

#Q1
cities_series = pd.Series(D).iloc[:6]
print(cities_series)

#Q2
cities = cities_series.index.values
print(cities)

#Q3
cities_slice = cities_series[:3]
print(cities_slice)

#Q4
print(cities_series[['Los Angeles','Houston','Phoenix']])

#Q5
bool1 = cities_series > 2000000
print(cities_series[bool1])

#Q6
bool2 = cities_series > 5000000
big_cities = len(cities_series[bool2])
print('Number of cities with population greater than 5 million is:', big_cities)