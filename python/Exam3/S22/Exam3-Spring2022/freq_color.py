#aibanez1:04/19/2024:freq_color.py

#I promise not to communicate with another human being in any way about this exam

#QA
import numpy as np
import pandas as pd

#QB
data = np.loadtxt('freq.dat')

#QC
values = data.size
print('There are %.e frequency values' %values)

#QD
boolviolet = np.logical_and( data > 668 , data <= 789 )
violet = data[boolviolet]
violet_count = violet.size

boolblue = np.logical_and( data > 606, data <= 668 )
blue = data[boolblue]
blue_count = blue.size

boolgreen = np.logical_and( data > 526, data <= 606 )
green = data[boolgreen]
green_count = green.size

colors = np.array(['violet','blue','green'])
indexval = np.array(['668-789 THz','606-668 THz','526-606 THz'])
counts = np.array([violet_count,blue_count,green_count])

T = np.vstack((colors,counts))
T = T.transpose()

columnsval = ['Color','Count']

T = pd.DataFrame(T, index = indexval, columns=columnsval)

# print(T)

#QE
largest_count_color = T.iloc[np.argmax(T['Count'], axis=0),0]
print(largest_count_color)