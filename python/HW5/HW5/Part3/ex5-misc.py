

Laz=['***','temperature anomaly AZ']

L=['Nevada','Colorado','Colorado']

L1=["New Mexico", 'Utah',"California"]

D={'California':[1.23,1.13,1.34,1.52, 1.46,1.98],'Colorado':[1.28,1.80,1.57,1.45]}

DNA='aca##a#g#atg##c#attgt'

Dchem={'hydrogen': ['H', 3], 'helium': ['He', 2], 'lithium':['Li', 3],'Adamantium':['Ad',22]}


#Q1
print(Laz[0]*2+'   '+' '.join(Laz[1].split(' ')[:-1])+'   '+Laz[0]*2)

#Q2
mCA=min(D['California'])

#Q3
print('In California the minumum temperature is', mCA)

#Q4
L.extend(L1)
print(L)

#Q5
ind=L.index('Colorado')
print(L.pop(ind))
print(L)

#Q6
RNA=((DNA.replace('#', '')).replace('t','u')).upper()
print(RNA)

#Q7
print('A occurs',RNA.count('A'), 'times')

#Q8
del Dchem['Adamantium']
print(Dchem)

#Q9
Dchem['hydrogen'][1]=1
print(Dchem)