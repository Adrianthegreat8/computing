#aibanez1:03/14/2025:celestial.py

"celestial"

"""
This module allows for calculating weight on other planets
"""

"Surface acceleration due to gravity on different planets"
Dg={"mercury": 3.70, "venus":8.88, "earth": 9.81, "mars":3.72, "jupiter" :24.79,
"saturn":10.44, "uranus":8.69, "neptune": 11.15}


def planet_weight(planetname,we):
    "takes parameters planet and weight on earth and returns the planet name and weight on that planet"
    wp = we * Dg[planetname] / Dg["earth"]
    return planetname,wp
    
    

def planet_weight1():
    "user enters weight on earth and asks the user to enter a planet name. The weight on that planet is printed"
    we=float(input("Enter a weight on the earth "))
    name=input("Enter a planet name: ")
    wp = we * Dg[name] / Dg["earth"]
    print("Weight on %s is %.2f Kg" %(name,wp))



if __name__ == '__main__':
    from sys import argv
    a, b = planet_weight(argv[1],float(argv[2]))
    print('Weight on %s is %.2f Kg' % (a, b))
    planet_weight1()