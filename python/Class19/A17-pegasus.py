#aibanez1:04/2/2024:A17-pegasus.py
import numpy as np

#A=np.loadtxt(filename, delimiter='sep')

#Q1
data = np.loadtxt('drop.dat')

#Q2
lines = np.shape(data)[0]

print('There are %d lines' %lines)

#Q3
time = data[:,0]
acceleration = data[:,1]

#Q4
timebool = time>0
timep = time[timebool]
accelerationp = acceleration[timebool]

#Q5
amax = np.max(accelerationp)
ind = np.argmax(accelerationp)
timemax = timep[ind]

#Q6
print('Maximum acceleration was %.3f G and it occured at time %.3f s' % (amax,timemax))

#Q7
acc5 = np.sort(accelerationp)[-5:]
asortind = np.argsort(accelerationp)
t5 = timep[asortind][-5:]

#Q8
zipped = zip(acc5,t5)
for i in zipped:
    print(i[1], i[0])

#Q9
final = np.transpose(np.vstack((np.transpose(t5),np.transpose(acc5))))
np.savetxt('file5.csv', final, fmt='%.2f', delimiter=',')