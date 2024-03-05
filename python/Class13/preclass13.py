L=['yellow','orange','blue']
s='ABC'

for i,j in zip(L,s):
     print(i,j)


print(list(zip(L,s)))

D={1:'a',2:'b'}

print('a' in D.values())

import random
r=8
while r!=8:
     r=random.randint(1,10)
     print(r)