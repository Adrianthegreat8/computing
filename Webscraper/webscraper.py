# text scraper

_floats=[]
costs=[]

with open('text.txt', 'r', encoding='utf-8') as f:
    f_lines = f.readlines()
    for i in f_lines:

        L=i.split(' ')

        if L[0] == 'Float:':
            _float=L[1]
            _floats.append(_float[:-2])
        elif L[0].count('$') >= 1:
            price=L[0]
            costs.append(float(price[1:-1]))

avg=0
_sum=0

for i in _floats:
    _sum=_sum+float(i)

totalcost=0

for i in costs:
    totalcost=totalcost+i

avg=_sum/len(_floats)
avgcost=totalcost/len(costs)

print('')
print('Average float is: %.3f' %avg)
print('Number of items:',len(_floats))
print('Total cost: $%.2f' % totalcost)
print('Average cost: %.2f' % avgcost)
print('Cost of 10: %.2f' %(avgcost*10))