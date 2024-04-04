import numpy as np

M = np.random.randint(1,100,size=(2,3))

Mm=np.min(M, axis=0)

print(M)

print(Mm)