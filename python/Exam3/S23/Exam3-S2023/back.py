
import numpy as np
import pandas as pd
L=[[0.0, 5.0, 10.0, 20.0, 25.0, 30.0], [1000.0, 550.0, 316.0, 180.0, 85.0, 31.0]]

data=np.array(L)

hour=np.array([ 0.,  5., 10., 20., 25., 30.])
amount=np.array([1000.,  550.,  316.,  180.,   85.,   31.])


amountp=np.array([1000.,  550.,  316.,  180.,   85.,   31.])


D={'name': {0: 'Darby George',
  1: 'Helen Dee',
  2: 'Giovanni Lupa',
  3: 'Cat Donovan'},
 'mass': {0: 63.2, 1: 43.5, 2: 92.4, 3: 50.1}}

df=pd.DataFrame(D)



Dr={'name': {0: 'Darby George',
  1: 'Helen Dee',
  2: 'Giovanni Lupa',
  3: 'Cat Donovan',
  4: 'John Smith'},
 'mass': {0: 63.2, 1: 43.5, 2: 92.4, 3: 50.1, 4: 45.6}}

dfr=pd.DataFrame(Dr)





Dc={'name': {0: 'Darby George',
  1: 'Helen Dee',
  2: 'Giovanni Lupa',
  3: 'Cat Donovan',
  4: 'John Smith'},
 'mass': {0: 63.2, 1: 43.5, 2: 92.4, 3: 50.1, 4: 45.6},
 'conc': {0: 7.918751345269175,
  1: 2.7030354828572842,
  2: 16.76468571276853,
  3: 4.2573175567835655,
  4: 3.1682442569176503}}

dfc=pd.DataFrame(Dc)



Ds={'name': {1: 'Helen Dee',
  4: 'John Smith',
  3: 'Cat Donovan',
  0: 'Darby George',
  2: 'Giovanni Lupa'},
 'mass': {1: 43.5, 4: 45.6, 3: 50.1, 0: 63.2, 2: 92.4},
 'conc': {1: 2.7030354828572842,
  4: 3.1682442569176503,
  3: 4.2573175567835655,
  0: 7.918751345269175,
  2: 16.76468571276853}}

dfs=pd.DataFrame(Ds)
