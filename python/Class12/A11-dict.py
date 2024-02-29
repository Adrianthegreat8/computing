#aibanez1:02/29/2024:A11-dict.py

#QA
D={"orange":3, "blue":4, "black":5}

#QB
D1=D.copy()

#QC
print(len(D))

#QD
D["purple"]=4
print(D)

#QE
D.update({"red":6})
print(D)

#QF
t=D.popitem()
print(D)

#QG
v=D.pop("orange")
print(D)

#QH
del D["blue"]
print(D)

#QI
print(D1)