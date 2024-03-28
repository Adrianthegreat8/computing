#aibanez1:03/26/2024:riddle.py

d1 = {'What':1,'is':2,'always':3}

s1 = 'IN:FRONT:OF:YOU'

l1 = ['cannot','but']

l2 = ['be','!','seen','?']

d2 = {'Almost':['The','end'],'there':{'before' : 'past', 'after' : 'future'}}

#QA
L1 = list(d1.keys())
#['What', 'is', 'always']
L2 = s1.lower().split(':')
#['in', 'front', 'of', 'you']
L3 = l1[::-1]
#['but', 'cannot']
l2.pop(1)
L4 = l2[:]
L5 = L1+L2+L3+L4

#QB
print(str(' '.join(L5)))

#d2 = {'Almost':['The','end'],'there':{'before' : 'past', 'after' : 'future'}}
#QC
print(d2['Almost'][0], d2['there']['after'])