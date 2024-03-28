#aibanez1:03/28/2024:ex9-ndarray.py

#Q1
import numpy as np

#Q2
arr1 = np.ones(5,)
print(arr1)

#Q3
arr2 = np.zeros((1,5))
print(arr2)

#Q4
arr3 = np.arange(20,23.5,0.5)
print(arr3)

#Q5
arr4 = np.linspace(20,23, num = 5)
print(arr4)

#Q6
arr6 = np.random.random(5,)
print(arr6)

#Q7
print(arr6[3:])

#Q8
idx = np.array([0,1,3])
print(arr6[idx])

#Q9
M = np.random.randint(1,101, size=(5,6))
print(M)

#Q10
r = M[1,:]
print(r)

#Q11
c = M[:,-2:]
print(c)

#Q12
A = np.identity(3)
B = np.random.randint(1,3, size=(3,3))

C = np.vstack((A,B))
print(C)

#Q13
size = C.size
x,y = C.shape
dim = C.ndim

print('The number of elements of C is', size)
print('C is a', str(x)+'x'+str(y), 'matrix')
print('C is a', str(dim)+'D array')