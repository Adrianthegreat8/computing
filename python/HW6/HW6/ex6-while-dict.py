#aibanez1:03/05/2024:ex6-while-dict.py
import random

D = {}

while len(D) < 4:
    color = input('Ender a color: \n')
    D[random.randint(1,10)]=color


print(D)