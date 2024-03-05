#aibanez1:03/05/2024:A12-patients.py

#QA
d1={'maria':[168,65,122], 'giovanna':[179,105,110], 'carlo':[190,95,130], 'francesco':[176,100,145]}

#QB
tpressure = 0
count = 0

for values in d1.values():
    tpressure += values[2]


print('The average pressure is:', tpressure / len(d1) )

#QC
s=''
for name in d1.keys():
    if name[-1] == 'a' :
        s += name

print(s)

