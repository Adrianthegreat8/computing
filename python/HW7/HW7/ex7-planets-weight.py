#aibanez1:03/12/2024:ex7-planets-weight.py

D={"venus":0.9,"mars":0.38,"mercury":0.38,"jupiter":2.36,
   "saturn":0.92,"uranus":0.89,"neptune":1.13,"pluto":0.07}

#Q1
def weight_planet():
   """
converts a weight of somethin on earth to the weight on another planet
   """
   print(list(D.keys()))
   name = input('Enter the name of a planet listed above\n')
   we = float(input('Enter some weight in kg\n'))
   wp = we * D[name]
   return name, wp

#Q2
weight_name = weight_planet()

#Q3
print('Your weight on the planet %s is %.2f kg' %(weight_name[0], weight_name[1]))

