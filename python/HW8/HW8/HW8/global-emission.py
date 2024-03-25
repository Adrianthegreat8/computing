#aibanez1:03/25/2024:global-emission.py

#Q1
from statistics import mean, stdev

#Q2
myfile = open('global-emission.dat', 'r')
L = myfile.readlines()
myfile.close()

#Q3

keys = [i.split(',')[0] for i in L]
values = [[float(k) for k in i.split(',')[1:]] for i in L]

D = dict(zip(keys,values))

print(D)

"""
Here I decided to use list comprehension twice. Once to make a list of countries and once to make a list of the emission 
values.
The values list was tricky because they had to be converted into floats. I used a double comprehension to loop through
each line of L, splitting by ',' and selecting only the values. I then used a second list comprehension to loop through
that list and convert each value in the list from a string into a float.
"""
print('\n')
#Q4
Dres = {i:[mean(D[i]), stdev(D[i])] for i in D}

#Q5
for i in Dres.items():
    print('%-22s %7.1f %8.1f %13s' % (i[0], i[1][0], i[1][1], '(MMT CO2 Eq)'))

#Q6
myfile = open('results-emission.dat', 'w')
myfile.write('Region name            average   stddev      Unit'+'\n')
for i in Dres.items():
    myfile.write(('%-22s %7.1f %8.1f %13s' % (i[0], i[1][0], i[1][1], '(MMT CO2 Eq)'))+'\n')
