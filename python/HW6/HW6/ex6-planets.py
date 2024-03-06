#aibanez1:03/05/2024:ex6-planets.py

name=['MERCURY', 'VENUS', 'EARTH', 'MARS', 'JUPITER', 'SATURN', 'URANUS', 'NEPTUNE', 'PLUTO'] 

temp=[167, 464, 15, -65, -110, -140, -195, -200, -225] 

orb_vel=[47.4,35.0,29.8,24.1,13.1,9.7,6.8,5.4,4.7] 

num_moons=[0,0,1,2,92,83,27,14,5]

#Q1
for n, t, moons, vel in list(zip(name, temp, num_moons, orb_vel)):
    if (vel >= 10) & (moons > 1):
        print('%-10s %-5.1f km/s %3d %4d C' %(n,vel,moons,t))