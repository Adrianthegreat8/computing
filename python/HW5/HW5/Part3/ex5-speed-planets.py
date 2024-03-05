#aibanez1:03/01/2024:ex5-speed-planets.py

## source https://nssdc.gsfc.nasa.gov/planetary/factsheet/

Dplanets={'MERCURY': ['170640', 167], 'VENUS': ['126000', 464], 'EARTH': ['107280'],
   'MARS': ['86760', -65],'JUPITER': ['47160', -110], 'SATURN': ['34920', -140],
   'URANUS': ['24480', -195], 'NEPTUNE': ['19440', -200], 'PLUTO': ['16920', -225]}

L=['s', 'p', 'a', 'c', 'e']

#Q1
print(''.join(L).upper())

#Q2
Dplanets['EARTH'].append(15)
print(Dplanets['EARTH'])

#Q3
Lplanets=list(Dplanets.keys())
Lplanets.sort()

#Q4
print('The planets of our solar system are:\n'+str(Lplanets))

#Q5
name=input('Enter a planet: ').upper()

#Q6
vel=float(int(Dplanets[name][0])/3600)

#Q7
print(name, 'orbital velocity around the sun %.1f km/s and its temperature is %.1f C' % (vel, Dplanets[name][1]))

