#aibanez1:02/29/2024:A11-opperations.py

#QA
P=[110,100,90,67,89] # blood pressure
names=['maria','gio','dome','anna','caty'] #patients
s='abracadabra'
D={'a':'@','e':3,'i':1,'o':0}

#QB
print(max(P))

#QC
print('Average is', sum(P)/len(P))

#QD
print('The blood pressure of gio is', P[names.index('gio')])

#QE
print(s.count('a'))

#QF
print('-'*10+'\n'+'H'*3+'e'*2+'l'+'o'*4+'\n'+'-'*10)

#QG
print('c'+str(D['i'])+D['a']+str(D['o']))
