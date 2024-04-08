#aibanez1:04/04/2024:ex9-particles.py

import numpy as np

#Q1
raw_data = np.loadtxt('particles-data.csv', delimiter=',', skiprows=1)

#Q2
backgroud_raw = raw_data[:5,:]
background_averages = np.mean(backgroud_raw, axis = 0)
foreground_raw = raw_data[5:,:]
data_clean = foreground_raw - background_averages

#Q3
event_number = data_clean[:,0]
energy = data_clean[:,1]
momentum = data_clean[:,2]
charge = data_clean[:,3]
spin = data_clean[:,4]

#Q4
bool_energy_charge = np.logical_and(energy > 10, charge > 0)
specific_energy = data_clean[bool_energy_charge]
print(specific_energy) #keep

print('\n')

for particle in specific_energy:
    print(particle)

#Q5
ind = np.argmax(energy, axis=0)
max_energy = energy[ind]
event_max_energy = event_number[ind]

print('\n')

print('Maximum Energy Value is %.1f Gev' % max_energy)
print('Event Number where Maximum Energy Occurs: %d' % event_max_energy)

#Q6
bool_antimatter = charge < 0
antimatter = np.array(data_clean[bool_antimatter])
print(antimatter)

np.savetxt('antimatter.csv', antimatter, fmt=('%d %.1f %.1f %.1f %.1f'), delimiter=',', newline='\n', header='Event Number, Energy, Momentum, Charge, Spin')

#Q7
antimatter_height, antimatter_width = antimatter.shape

print('There are', antimatter_height, 'antimatter events')

#Q8
total_charge = sum(charge)
print('Total Charge of All Particles is: %.1f e' %total_charge)

#Q9
bool_neg_momentum = momentum < 0
event_neg_momentum = np.int64(event_number[bool_neg_momentum])
print(event_neg_momentum)

#Q10
spin_positive_bool = spin > 0
spin_positive = spin[spin_positive_bool]
sqroot_spin = np.sqrt(spin_positive)
print('Square Root of Positive Spin Values :\n', sqroot_spin)