#aibanez1:03/26/2024:module1.py
""" This module provide fucntions to calculate efficiencies of a heat engine
"""

"""
I promise no to communicate with another human being in any way about this exam.
"""
import math as m

def convert(Tc):
     'Converts temperature in Celsius to temperature in Kelvin'
     Tk=Tc+273
     return Tk


def names():
     'Returns two strings: Carnot and Curzon'
     return 'Carnot','Curzon'

     
#Q1.1 a
def efficiencies(Tcold, Thot):
     ncarnot = 1 - (Tcold/Thot)
     ncurzon = 1 - m.sqrt(Tcold/Thot)
     return ncarnot,ncurzon

#Q1.1 b
if __name__ == '__main__':
     Tc_c = 10
     Tc_h = 300
     Tk_c = convert(Tc_c)
     Tk_h = convert(Tc_h)

     R = efficiencies(Tk_c, Tk_h)

     print('Carnot efficiency is %.2f' %R[0])
     print('Curzon efficiency is %.2f' %R[1])
