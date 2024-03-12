#aibanez1:03/12/2025:ex7-Qpotential.py

#Q1
from math import sqrt

#Q2
def f_k1 (m, E):
    k1 = sqrt( 2 * m * E )
    return k1

#Q3
def f_k2 (m, E, V):
    k2 = sqrt( 2 * m * (E - V ))
    return k2

#Q4
def T_R (m, E, V):
    k1 = f_k1(m, E)
    k2 = f_k2(m, E, V)

    T = ( 4* k1 * k2 ) / (( k1 + k2 )**2)
    R = (( k1 - k2 )**2) / (( k1 + k2 )**2)

    return (T, R)

#Q5
T,R= T_R(9.11*10**-31, 10, 9)

print('T = %.2f and R = %.2f, and their sum is %.2f' %(T, R, T+R))

