#aibanez1:03/27/2024:ex1-s24-while.py

L=['purple','orange','white','black','yellow',
   'red','purple','orange','white','black','yellow', 'red']

#Q0 I promise not to communicate with another human being in any way about this exam.

#Q1
import random

D = {}
count = 0
while len(D) < 5:
   color = random.choice(L)
   number = random.randint(1,10)
   if ((color in D.keys()) or (number in D.values())):
      continue
   else:
      D[random.choice(L)] = random.randint(1,10)
   count += 1

#Q2
print(D,'\nHas been constructed in', count, 'iterations.')

