#aibanez1:03/07/2024:A13-sum-lists.py

#QA
L1=[1,2,3,4]
L2=[5,6,7,8]

#QB
Lsum = []
Lzip = list(zip(L1,L2))

for i in range(len(Lzip)):
    Lsum.append(Lzip[i][0] + Lzip [i][1])

print(Lsum)