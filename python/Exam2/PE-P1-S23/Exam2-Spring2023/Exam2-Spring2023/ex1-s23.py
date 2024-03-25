#aibanez1:03/16/2024:ex1-s23.py

D={'s1': ['g','a','t','*'], 's2':['t','a','c','&'], 's3':['a','%']}

#Q1
Lchar = [i.pop(-1) for i in D.values()]

print(D)
print(Lchar)

#Q2
GATTACA = ''
for i in D.values():
    GATTACA += ''.join(i).upper()

print(GATTACA)

#Q3
