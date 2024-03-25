#aibanez1:03/16/2024:ex3-datasets.py

names=['emissions.txt','labor.txt','land.txt','supercomputer.txt']

#Q1
def find_max(recorded_values, years):
    max_value = max(recorded_values)
    cooresponding_year_index = recorded_values.index(max_value)
    max_years = years[cooresponding_year_index]
    return (max_value, max_years)

#Q2
def topic_unit(header_line):
    return header_line.split('-')[0], header_line.split('-')[1]

#Q3
import random

filename = random.choice(names)

#Q4
print('Analyzing', filename)

#Q5
myfile = open(filename, 'r')
L = [lines for lines in myfile.readlines()]

#Q6
header = L[0]

L1 = L[1:]

#Q7
Ly = [int(i.split(',')[0]) for i in L1]

#Q8
Lv = [float(i.split(',')[1]) for i in L1]

#Q9
M, Y = find_max(Lv, Ly)

#Q10
topic, unit = topic_unit(header)

#Q11
print(topic, 'max value', M, unit[:-1], 'in', Y)