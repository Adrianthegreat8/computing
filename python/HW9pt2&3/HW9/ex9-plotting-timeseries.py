#aibanez1:04/05/2024:ex9-plotting-timeseries.py

files=['Carbon dioxide emission-MTCO2e.txt','Land Temperature Anomalies-Celsius.txt',
       'Labor Force Statistics-percent.txt', 'Supercomputer power-FLOPS.txt']

#Q1
import numpy as np
import matplotlib.pyplot as plt

#Q2
def timeseries (ax, time, value, str_format, xlabel, ylabel, str_legend):

       ax.plot(time, value, str_format, label=str_legend)
       ax.set_xlabel(xlabel)
       ax.set_ylabel(ylabel)

       return ax

#Q3
units = [i.split('-')[1][:-4] for i in files]
topics = [i.split('-')[0] for i in files]

formats=['ob--','og--','om--','or--']

#Q4

plt.rcParams['font.size']=12
plt.rcParams['font.family']='Times'
plt.rcParams['figure.subplot.wspace']= 0.4
plt.rcParams['figure.subplot.hspace']= 0.3

#Q5
fig, ax = plt.subplots(2,2, figsize=(8,8))

#Q6
for ind,subplot in enumerate(ax.flatten()):
       raw_data = np.loadtxt(files[ind], delimiter=',', skiprows=1)
       timeseries(subplot,raw_data[:,0],raw_data[:,1],formats[ind],'Year',units[ind],topics[ind])
       subplot.grid()
       subplot.legend()

plt.show()