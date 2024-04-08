#aibanez1:04/04/2024:A18-sub.py
import numpy as np
import matplotlib.pyplot as plt

#Q1
fig, ax = plt.subplots(3,1, figsize=(5,8))
plt.rcParams['font.size']=12
plt.rcParams['font.family']='Ariel'
plt.rcParams['figure.subplot.hspace']= 0.5

x5 = np.linspace(0,2*np.pi,5)
ax[0].plot(x5,np.sin(x5),'db:')
ax[0].set_xlabel(r'$\theta$')
ax[0].set_ylabel(r'$sin(\theta)$')
ax[0].set_xlim(0,6)
ax[0].grid()

x10 = np.linspace(0,2*np.pi,10)
ax[1].plot(x10,np.sin(x10),'or--')
ax[1].set_xlabel(r'$\theta$')
ax[1].set_ylabel(r'$sin(\theta)$')
ax[1].set_xlim(0,6)
ax[1].grid()

x100 = np.linspace(0,2*np.pi,100)
ax[2].plot(x100,np.sin(x100),'k')
ax[2].set_xlabel(r'$\theta$')
ax[2].set_ylabel(r'$sin(\theta)$')
ax[2].set_xlim(0,6)
ax[2].grid()


#Q2
fig1, ax1 = plt.subplots(3,1, figsize=(5,8))


n = [5,10,100]
style = ['db:', 'or--', 'k']

for i,j in enumerate(ax1.flatten()):
    x = np.linspace(0,2*np.pi,n[i])
    j.plot(x,np.sin(np.linspace(0,2*np.pi,n[i])),style[i])
    j.set_xlabel(r'$\theta$')
    j.set_ylabel(r'$sin(\theta)$')
    j.set_xlim(0, 6)
    j.grid()

plt.show()
