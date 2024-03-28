#aibanez1:03/26/2024:my_efficiencies.py

#QA
import module1 as m

#QB
myfile = open('power_data.dat', 'r')
L = myfile.readlines()
myfile.close()

#QC
L1 = L[1:]

#QD
#Power station,Tcold,Thot,Observed
for i in L1:
    j = i.split(',')
    Tc_C = float(j[1])
    Th_C = float(j[2])

    Tc_K = m.convert(Tc_C)
    Th_K = m.convert(Th_C)

    carnot,curzon = m.efficiencies(Tc_K, Th_K)
    #carnot,curzon
    print('%-20s %5.2f %5.2f %5.2f' %(j[0], carnot, curzon, float(j[3])))