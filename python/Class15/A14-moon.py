#aibanez1:03/12/2024:A14-moon.py

#QA
def w_moon(we):
    g_earth = 9.81
    g_moon = 1.62
    wm = we*g_moon/g_earth
    return wm

#QB
wm_out=w_moon(100)

#QC
print('My object weighs %.2f Kg on the Moon' %wm_out)

#QD
weights = [w_moon(i) for i in range(50,60)]

print(weights)