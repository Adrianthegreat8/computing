#aibanez1:03/26/2024:ex3-f23-rhomb.py

#Q1
def rhombarea (d1, d2):
    A = (d1*d2)/2
    return A

#Q2
def valid_entries ():
    while True:
        d1_d2 = input('Enter two numbers > 0 separated by a comma: ')
        d1 = float(d1_d2.split(',')[0])
        d2 = float(d1_d2.split(',')[1])
        if (d1 > 0) & (d2 > 0):
            return (d1,d2)
            break

#Q3
myfile = open('valid.txt', 'w')
myfile.write('%s %7s %6s\n' %('d1', 'd2', 'A'))
for i in range(4):
    d1,d2 = valid_entries()
    A = rhombarea(d1,d2)
    myfile.write('%.1f %7.1f %7.1f\n' % (d1, d2, A))

myfile.close()