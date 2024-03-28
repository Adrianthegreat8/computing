#aibanez1:03.28/2024:A16-indexing-array.py
import numpy as np

#Q1
arr1 = np.random.randint(0,10, size=(9,))
print(arr1) #remove

#Q2
print(arr1[3])

#Q3
print(arr1[2:6])

#Q4
idx = np.array([1,3,5])
print(arr1[idx])

#Q5
arr2 = np.random.random((3,4))
print(arr2)

#Q6
print(arr2[1,1])

#Q7
print(arr2[:2,:3])

#Q8
row_idx = np.arange(0,3)
print(row_idx)
col_idx = np.array([2,1])

print(arr2[row_idx])
print(arr2[col_idx])

#Q9
print(arr2[1,:])

#Q10
print(arr2[:,2])