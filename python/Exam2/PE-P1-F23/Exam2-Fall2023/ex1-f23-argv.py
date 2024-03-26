#aibanez1:03/26/2024:ex1-f23-argv.py
D={'colors': ['blue','red','yellow'],'numbers': [{'integer':[1,2,3]} , {'float':[1.2,3.4]}]}

#Q0
#I promise not to communicate with another human being in any way about this exam

#Q1
from sys import argv
num = int(argv[1])

#Q2
D['numbers'][0]['integer'].append(num)
print(D)

#Q3
import random
print(random.choice(D['colors'])*num)
#D={'colors': ['blue','red','yellow'],'numbers': [{'integer':[1,2,3]} , {'float':[1.2,3.4]}]}

#Q4
L = [j for j in range(1, num+1)]
print(sum(L))

