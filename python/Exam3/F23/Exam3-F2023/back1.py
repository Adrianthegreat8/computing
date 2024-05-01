#backup variables

import numpy as np


year=np.array([1901., 1902., 1903., 1904., 1905., 1906., 1907., 1908., 1909.,
       1910., 1911., 1912., 1913., 1914., 1915., 1916., 1917., 1918.,
       1919., 1920., 1921., 1922., 1923., 1924., 1925., 1926., 1927.,
       1928., 1929., 1930., 1931., 1932., 1933., 1934., 1935., 1936.,
       1937., 1938., 1939., 1940., 1941., 1942., 1943., 1944., 1945.,
       1946., 1947., 1948., 1949., 1950., 1951., 1952., 1953., 1954.,
       1955., 1956., 1957., 1958., 1959., 1960., 1961., 1962., 1963.,
       1964., 1965., 1966., 1967., 1968., 1969., 1970., 1971., 1972.,
       1973., 1974., 1975., 1976., 1977., 1978., 1979., 1980., 1981.,
       1982., 1983., 1984., 1985., 1986., 1987., 1988., 1989., 1990.,
       1991., 1992., 1993., 1994., 1995., 1996., 1997., 1998., 1999.,
       2000., 2001., 2002., 2003., 2004., 2005., 2006., 2007., 2008.,
       2009., 2010., 2011., 2012., 2013., 2014., 2015., 2016., 2017.,
       2018., 2019., 2020., 2021.])


temperature=np.array([-0.27 , -0.468, -0.666, -0.828, -0.504, -0.378, -0.684, -0.774,
       -0.792, -0.72 , -0.792, -0.612, -0.576, -0.252, -0.18 , -0.576,
       -0.702, -0.558, -0.45 , -0.414, -0.288, -0.45 , -0.45 , -0.432,
       -0.324, -0.126, -0.306, -0.324, -0.594, -0.198, -0.108, -0.234,
       -0.468, -0.198, -0.288, -0.216, -0.018, -0.036,  0.018,  0.288,
        0.486,  0.198,  0.198,  0.504,  0.324, -0.018, -0.072, -0.09 ,
       -0.144, -0.27 ,  0.   ,  0.072,  0.234, -0.18 , -0.234, -0.324,
        0.126,  0.216,  0.144,  0.09 ,  0.18 ,  0.198,  0.216, -0.252,
       -0.126, -0.018,  0.   , -0.054,  0.198,  0.108, -0.126,  0.072,
        0.342, -0.108,  0.018, -0.126,  0.378,  0.216,  0.414,  0.504,
        0.594,  0.342,  0.648,  0.306,  0.288,  0.432,  0.702,  0.702,
        0.54 ,  0.81 ,  0.702,  0.432,  0.504,  0.63 ,  0.846,  0.576,
        0.936,  1.17 ,  0.792,  0.756,  1.026,  1.116,  1.152,  1.044,
        1.206,  1.134,  1.116,  0.972,  1.152,  1.296,  1.026,  1.152,
        1.206,  1.332,  1.674,  1.782,  1.638,  1.476,  1.71 ,  1.764,
        1.512])


#variables for blue dots
x_pos=np.array([1939., 1940., 1941., 1942., 1943., 1944., 1945., 1952., 1953.,
       1957., 1958., 1959., 1960., 1961., 1962., 1963., 1969., 1970.,
       1972., 1973., 1975., 1977., 1978., 1979., 1980., 1981., 1982.,
       1983., 1984., 1985., 1986., 1987., 1988., 1989., 1990., 1991.,
       1992., 1993., 1994., 1995., 1996., 1997., 1998., 1999., 2000.,
       2001., 2002., 2003., 2004., 2005., 2006., 2007., 2008., 2009.,
       2010., 2011., 2012., 2013., 2014., 2015., 2016., 2017., 2018.,
       2019., 2020., 2021.])


y_pos=np.array([0.018, 0.288, 0.486, 0.198, 0.198, 0.504, 0.324, 0.072, 0.234,
       0.126, 0.216, 0.144, 0.09 , 0.18 , 0.198, 0.216, 0.198, 0.108,
       0.072, 0.342, 0.018, 0.378, 0.216, 0.414, 0.504, 0.594, 0.342,
       0.648, 0.306, 0.288, 0.432, 0.702, 0.702, 0.54 , 0.81 , 0.702,
       0.432, 0.504, 0.63 , 0.846, 0.576, 0.936, 1.17 , 0.792, 0.756,
       1.026, 1.116, 1.152, 1.044, 1.206, 1.134, 1.116, 0.972, 1.152,
       1.296, 1.026, 1.152, 1.206, 1.332, 1.674, 1.782, 1.638, 1.476,
       1.71 , 1.764, 1.512])


#variables for red dots
x_neg=np.array([1901., 1902., 1903., 1904., 1905., 1906., 1907., 1908., 1909.,
       1910., 1911., 1912., 1913., 1914., 1915., 1916., 1917., 1918.,
       1919., 1920., 1921., 1922., 1923., 1924., 1925., 1926., 1927.,
       1928., 1929., 1930., 1931., 1932., 1933., 1934., 1935., 1936.,
       1937., 1938., 1946., 1947., 1948., 1949., 1950., 1951., 1954.,
       1955., 1956., 1964., 1965., 1966., 1967., 1968., 1971., 1974.,
       1976.])


y_neg=np.array([-0.27 , -0.468, -0.666, -0.828, -0.504, -0.378, -0.684, -0.774,
       -0.792, -0.72 , -0.792, -0.612, -0.576, -0.252, -0.18 , -0.576,
       -0.702, -0.558, -0.45 , -0.414, -0.288, -0.45 , -0.45 , -0.432,
       -0.324, -0.126, -0.306, -0.324, -0.594, -0.198, -0.108, -0.234,
       -0.468, -0.198, -0.288, -0.216, -0.018, -0.036, -0.018, -0.072,
       -0.09 , -0.144, -0.27 ,  0.   , -0.18 , -0.234, -0.324, -0.252,
       -0.126, -0.018,  0.   , -0.054, -0.126, -0.108, -0.126])

#yp - predicted values from the model
yp=np.array([-0.79945753, -0.78233985, -0.76522217, -0.74810448, -0.7309868 ,
       -0.71386912, -0.69675144, -0.67963376, -0.66251608, -0.6453984 ,
       -0.62828072, -0.61116304, -0.59404536, -0.57692768, -0.55981   ,
       -0.54269232, -0.52557464, -0.50845696, -0.49133928, -0.4742216 ,
       -0.45710392, -0.43998623, -0.42286855, -0.40575087, -0.38863319,
       -0.37151551, -0.35439783, -0.33728015, -0.32016247, -0.30304479,
       -0.28592711, -0.26880943, -0.25169175, -0.23457407, -0.21745639,
       -0.20033871, -0.18322103, -0.16610335, -0.14898567, -0.13186799,
       -0.1147503 , -0.09763262, -0.08051494, -0.06339726, -0.04627958,
       -0.0291619 , -0.01204422,  0.00507346,  0.02219114,  0.03930882,
        0.0564265 ,  0.07354418,  0.09066186,  0.10777954,  0.12489722,
        0.1420149 ,  0.15913258,  0.17625026,  0.19336794,  0.21048563,
        0.22760331,  0.24472099,  0.26183867,  0.27895635,  0.29607403,
        0.31319171,  0.33030939,  0.34742707,  0.36454475,  0.38166243,
        0.39878011,  0.41589779,  0.43301547,  0.45013315,  0.46725083,
        0.48436851,  0.50148619,  0.51860387,  0.53572156,  0.55283924,
        0.56995692,  0.5870746 ,  0.60419228,  0.62130996,  0.63842764,
        0.65554532,  0.672663  ,  0.68978068,  0.70689836,  0.72401604,
        0.74113372,  0.7582514 ,  0.77536908,  0.79248676,  0.80960444,
        0.82672212,  0.8438398 ,  0.86095749,  0.87807517,  0.89519285,
        0.91231053,  0.92942821,  0.94654589,  0.96366357,  0.98078125,
        0.99789893,  1.01501661,  1.03213429,  1.04925197,  1.06636965,
        1.08348733,  1.10060501,  1.11772269,  1.13484037,  1.15195805,
        1.16907573,  1.18619342,  1.2033111 ,  1.22042878,  1.23754646,
        1.25466414])

#variables for prediction during 2025-2050 - black dots
xpred=np.array([2025, 2030, 2035, 2040, 2045, 2050])
ypred=np.array([1.32313486, 1.40872326, 1.49431167, 1.57990007, 1.66548847,
       1.75107687])

# R squared
R2=0.8445917563947412




