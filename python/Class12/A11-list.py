#aibanez1:02/29/2024:A11-list.py

#QA
Lzoo=['pangolin','cobra','chicken','lion','elephant']

#QB
Lzoo1=Lzoo[:]

#QC
Lzoo[Lzoo.index('chicken')]='fox'
print(Lzoo)

#QD
Lzoo.append('elephant')
print(Lzoo1)

#QE
print(Lzoo.count('elephant'))

#QF
Lzoo.extend(["zebra", "koala"])
print(Lzoo)

#QG
Lzoo.reverse()
print(Lzoo)

#QH
Lzoo.insert(2,'emu')
print(Lzoo)

#QI
var=Lzoo.pop(0)
print(Lzoo)
print(var)

#QJ
Lzoo.remove('lion')

#QK
print(Lzoo1)