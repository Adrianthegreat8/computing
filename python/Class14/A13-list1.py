#aibanez1:03/07/2024:A13-list1


L1=[['a', 'p', 'p', 'l', 'e'], ['b', 'a', 'n', 'a', 'n', 'a'],
    ['c', 'h', 'e', 'r', 'r', 'y'], ['k', 'i', 'w', 'i'],
    ['m', 'a', 'n', 'g', 'o']]

Dave = {"Iron Man": 2008, "Captain America ":2011,
             "Thor" : 2011,"The Incredible Hulk" :2008,
             "Doctor Strange": 2016, "Spider-Man: Homecoming":2017}


#QA
L2 = [''.join(x) for x in L1]
print(L2)

#QB
ave2010 = [ movie for movie,year in Dave.items() if year > 2010]
print(ave2010)



