#aibanez1:03/12/2024:A14-isc.py

def func_isc():
    while True:
        answer = input('Did you enjoy this course? Yes or no?\n')
        if (answer == 'yes'):
            print('Good!')
            break
        elif (answer == 'no'):
            print('Sorry!')
            break
        else:
            print('You didn\'t pick yes or no! Try again')

func_isc()
