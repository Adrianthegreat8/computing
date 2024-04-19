#aibanez1:04/16/2024:A21-sound-error.py

# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from sklearn.metrics import r2_score

raw_data = np.loadtxt('sound_data.txt')

temp = raw_data[:,0]
data = raw_data[:,1:] - 2

print(raw_data)
print(data)

average = np.mean(data, axis=1)
print(average)

height,width = data.shape
error = ((np.std(data, axis=1))/np.sqrt(width))
print(error)

fig, ax = plt.subplots(figsize=(5,5))
ax.errorbar(temp,average, yerr=error, fmt = 'b.', capsize = 5, label = 'average of 5 trials')

ax.set_xticks(temp)
ax.set_xlabel('Temperature (ºC)')
ax.set_ylabel('Velocity (m/s)')
ax.grid()
ax.legend()

plt.show()