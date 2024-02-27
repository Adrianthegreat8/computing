#aibanez1:02/27/2024:A10-nested.py

#QA
D={'s1':'GACTC',
   's2':'134,256',
   'd1':{'tuple1':(1,2,3),'L1':[1,2,3,4,5,6]},
   'L2':['a','b','c','d'],
   'L3':[{'d3':'you made it'},'bravo']
   }

#QB
print(D['L3'][1], D['L3'][0]['d3'])
