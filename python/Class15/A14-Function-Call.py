#aibanez1:03/12/2024:A14-Function-Call.py



#Write a docstring in each of these functions.
#The first function already contains its doc string


#a
def func1(par1,par2,par3):
    """ takes 3 parameters and returns the mutiplication of them.
    """
    x=par1*par2*par3
    return x

#b
def func2(par1,par2,par3):
    """ Takes 3 parameters and prints the multiplication of them.
    """
    x=par1*par2*par3
    print(x)

    
#c 
def func3():
    """ Calls the input function for the user and prints the cube of that input.
    """
    num=float(input("Enter a number to calculate the cube: "))
    print(num*num*num)


#d
def func4():
    """ Calls the input function for the user to input a number, returns hello that number of times.
    """
    s="hello"
    num=int(input("Enter an integer number to repeat a string: "))
    return s*num

#e 
def func5():
    """ Calls for input from user. Appends subject to list if it does not exist then prints the list of subjects.
    """
    subject=[]
    for i in range(5):
        sub=input("Enter a subject: ")
        if sub not in subject:
            subject.append(sub)
    print("This is your list of unique entries: ", subject)
    

    

#function calls

#a
func1(1,2,3)

#b
func2(1,2,3)

#c
func3()

#d
func4()

#e
func5()








    
