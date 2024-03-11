#aibanez1:03/10/2024:ex6-dcompre.py
#Q1
D = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
selectedKeys = [0, 2, 5]

Dsel = {i:j for i,j in D.items() if i in selectedKeys}

print(Dsel)

#Q2
ChainA={'prot1':'VGFTYU','prot2':'NHGTYU','prot3':'UIJYHTUI'}
ChainB={'prot1':'WSEQRT','prot2':'JUHYTR','prot3':'NHYUTO'}

ChainAB = {i:ChainA[i]+ChainB[i] for i in ChainA}
print(ChainAB)

