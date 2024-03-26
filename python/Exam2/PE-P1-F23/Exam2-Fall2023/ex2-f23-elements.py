#aibanez1:03/26/2024:ex2-f23-elements.py

#Q1
from weight import Dw

#Q2
myfile = open('data-elements.csv', 'r')
L = myfile.readlines()
myfile.close()

print(L)

#Q3
print(L.pop(0).upper())
#List Data set without header

#Q4
Datomicity = {i.split(',')[2][1:-1]:int(i.split(',')[3][:-1]) for i in L}
print(Datomicity)
#Dictionary Symbol:Atomicity

#Q5
print('There are', list(Datomicity.values()).count(3), 'triatomic molecules.')

#Q6
Ddiatomic = {i:Dw[i]*j for i,j in Datomicity.items() if j == 2}
print(Ddiatomic)
#Dictionary Diatomic Molecules:Molecular weight

#Q7
Ddiatomic_keys = list(Ddiatomic.keys())
Ddiatomic_values = list(Ddiatomic.values())

#Q8
for i in range(len(Ddiatomic_keys)):
    print('%-4s %7.2f' % ( Ddiatomic_keys[i] + str(Datomicity[Ddiatomic_keys[i]]), Ddiatomic_values[i]))

#Q9
#This is with all the variables combined
polyatomic = {i.split(',')[2][1:-1]:Dw[i.split(',')[2][1:-1]] for i in L if int(i.split(',')[3]) > 3}
max_weight_symbol = list(polyatomic.keys())[list(polyatomic.values()).index(max(list(polyatomic.values())))]
max_weight_atomicicty = Datomicity[max_weight_symbol]

print(max_weight_symbol+max_weight_atomicicty)

#This is the broken down version
# polyatomic = {i.split(',')[2][1:-1]:Dw[i.split(',')[2][1:-1]] for i in L if int(i.split(',')[3]) > 3}
#
# polyatomic_keys = list(polyatomic.keys())
# polyatomic_values = list(polyatomic.values())
#
# max_polyatomic_weight = max(polyatomic_values)
# max_weight_index = polyatomic_values.index(max_polyatomic_weight)
# max_weight_symbol = polyatomic_keys[max_weight_index]
# max_weight_atomicicty = Datomicity[max_weight_symbol]
#
# print(max_weight_symbol+max_weight_atomicicty)