#aibanez1:04/04/2024:A18-myplot.py

import matplotlib.pyplot as plt
import numpy as np

a = 10
b = 5

x = np.linspace(0,10,40)

y1 = (a) * (x**2)
y2 = (b) * (x**3)

fig, ax = plt.subplots(figsize=(5,3))

ax.plot(x,a*x**2, '--r', label='quadratic')
ax.plot(x,b*x**3, 'b', label='cubic')

ax.set_xlim(0, 10.5)
ax.legend()
ax.grid()
ax.set_xticks(np.arange(1,11,1))
ax.set_yticks(np.arange(0,6000,1000))
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.rcParams['font.size']=14
plt.rcParams['font.family']='Helvetica'

plt.show()