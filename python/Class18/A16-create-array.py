#aibanez1:03/28/2024:A16-create-array.py

import numpy as np

#Q1
v = np.arange(-1,1,.25)
print(v)
print(type(v))
print(v.dtype)
print(v.shape)
print(v.size)
print(v.ndim)

#Q3
v1 = np.arange(0,11)
print(v1)

#Q4
from math import pi

v3 = np.linspace(-pi,pi,5)
print(v3)

#Q5
v4 = np.zeros((5,))
print(v4)

#Q6
vb = np.ones((5,1))
print(vb)

#Q7
M = np.random.randint(1,20, size=(6,2))
print(M)

#Q8
Mt = np.transpose(M)
print(Mt)

#Q9
Mf = M.flatten()
print(Mf)

#Q10
rows,columns = (M.shape)
print('There are', rows, 'and', columns, 'columns')

#Q11
O = np.ones((3,4))
print(O)

#Q12
O1 = np.reshape(O, (6,2))
print(O1)

#Q13
V = np.vstack((O1,M))
print(V)

#Q14
H = np.hstack((O1,M))
print(H)

#Q15
L = v.tolist()
print(L)