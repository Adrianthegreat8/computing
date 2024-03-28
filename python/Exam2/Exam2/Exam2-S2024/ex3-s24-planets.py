#aibanez1:03/27/2024:ex3-s24-planets.py

#Q1
myfile = open('planets-all.csv', 'r')
L = myfile.readlines()
myfile.close()

print(L) #keep

#Q2
Lplanets = L[0].split(',')[1:-1]

#Q3
Lmoons = []
for i in L:
    if 'Number of Moons' in i:
        Lmoons = [int(j) for j in i.split(',')[1:]]

print(Lmoons) #keep

#Q4
planetNameMoons = input('Enter an imaginary planet name and its number of moons separated by a space:')

name,moon = (planetNameMoons.split())

Lplanets.insert(1, name.upper())
Lmoons.insert(1, int(moon))

#Q5
planetsMoons = zip(Lplanets,Lmoons)

for i in planetsMoons:
    print('%-10s %d' % (i[0], i[1]))

#QEC
print('\n')

for i in L:
    if 'Surface Pressure' in i:
        Lpressures = [j for j in i.split(',')[1:]]

print(Lpressures)

LpressuresClean = []

for i in Lpressures:
    if ('*' not in i) and ('Unknown' not in i):
        LpressuresClean.append(float(i))
    elif 'Unknown' in i:
        LpressuresClean.append(0)
    else:
        newI = list(i)
        while '*' in newI:
            newI.remove('*')
        newI = float(''.join(newI))
        LpressuresClean.append(newI)

print(LpressuresClean)

maxPressure = 0
for index, i in enumerate(LpressuresClean):
    if i > maxPressure:
        maxPressure = i
        maxIndex = index

print('The planet with the largest surface pressure is', Lplanets[maxIndex])