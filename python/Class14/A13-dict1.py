#aibanez1:03/07/2024:A13-dict1.py

#d1={name: [height, weight, bp]}

#QA
d1={'anita':[168,65,122],'toni':[179,105,110],
    'maria':[190,95,130],'laura':[176,100,145]} 

d2 = {x:y for x,y in d1.items() if ( y[1] > 90 ) & ( y[2] > 120 )}
print(d2)

#QB
d3 = {}
for x,y in d1.items():
    if ( y[1] > 90 ) & ( y[2] > 120 ):
        d3[x]= y

print(d3)