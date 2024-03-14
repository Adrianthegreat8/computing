#aibanez1:03/14/2024:A15-temp.py

#QA
myfile = open('temp.dat', 'r')
L = myfile.readlines()
myfile.close()

print(L)

#QB
L1 = [i for i in L if '#' not in i]
print(L1)

#QC
from statistics import mean

L2 = [float(i.split()[-1]) for i in L1]
print(mean(L2))

#QD
Lstate = []
for i in L1:
    j = i.split()[1]
    if j not in Lstate:
        Lstate.append(j)
print(Lstate)

#QE
for i in L1:
    j = i.split()
    if float(j[2]) > 1.9:
        print('%-5s %.1f' %(j[1], float(j[2])))

#QF
myfile = open('results.txt', 'w')
myfile.write('State      Temp\n')
for i in L1:
    j = i.split()
    if float(j[2]) > 1.9:
        myfile.write('%3s %10.1f\n' %(j[1], float(j[2])))
myfile.close()

#QG
D = {}

for state in Lstate:
    temps = [float(i.split()[2]) for i in L1 if i.split()[1] == state]
    D[state] = temps

print(D)

