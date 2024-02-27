# aibanez1:02/27/2024:A10-create.py

# QA
L = ['yellow', 'orange', 'blue']
number = [2, 4, 7, 9]
fruits = ['apple', 'orange', 'pear', 'banana']

s = 'color'
ss = 'c o l o r'

D = {1: 'a', 2: 'b', 3: 'c'}
T = ('Hello', 2, 100)

# QB
s1 = ('*'.join(L))
print(s1)

#QC
s2=(L[-1], L[1], L[0])
print('*'.join(s2))

#QD
print(list(s))

#QE
print(list(ss[0:9:2]))

#QF
print(list((D[1],D[2],D[3])))

#QG
print(T[0])

#QH
T1=tuple(L)
print(T1)

#QI
print(dict(zip(fruits,number)))