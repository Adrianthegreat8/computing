#aibanez1:03/16/2024:ex2-blizzard.py

myfile = open('blizzard.txt', 'w')

count = 0

while count < 4:
    wind_speed = float(input('Enter a value for the wind speed \n'))
    visibility = float(input('Enter a value for visibility in miles \n'))

    if wind_speed > float(30) and visibility < 0.5:
        write = '%.1f %.1f' % (wind_speed, visibility)
        myfile.write(write+'\n')
        count += 1

