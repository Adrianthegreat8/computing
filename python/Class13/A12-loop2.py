#aibanez1:03/05/2024:A12-loop2.py

#QA
veggie=['spinach', 'broccoli', 'edamame', 'bell pepper']
num=[30,15,25,11]

#QB
print(' ')

for i in range(len(veggie)):
    print(num[i],' ', veggie[i])

#QC
print(' ')

for i, number in enumerate(num):
    print(number, ' ', veggie[i])

#QD
print(' ')

for n,v in zip(num,veggie):
    print(n, ' ', v)