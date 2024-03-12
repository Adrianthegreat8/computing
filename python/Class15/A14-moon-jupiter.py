#aibanez1:03/12/2024:A14-moon-jupiter.py

#QA
def w_moon_jupiter (we):
    g_earth = 9.81
    g_moon = 1.62
    g_jupiter = 24.79

    wm=we*g_moon/g_earth
    wj=we*g_jupiter/g_earth

    return [wm,wj]

#QB
my_weight = w_moon_jupiter(100)

#QC
print(my_weight)

#QD
print('The weight on the moon is %.2f \nThe weight on Jupiter is %.2f' %(my_weight[0], my_weight[1]))