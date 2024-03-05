#aibanez1:03/05/2024:A12-loop.py

#QA
s='PYTHON MONTY PYTHON'

for letter in s:
    print(letter.lower())

#QB
print('')

veggie=['spinach', 'broccoli', 'edamame', 'bell pepper']

for veg in veggie:
    print(veg.upper())

#QC
print('')

dzoo= {"pangolin" : 5, "sloth" : 3, "tiger" : 2, "turtle" : 10}

for animal,value in dzoo.items():
    print(value, animal)