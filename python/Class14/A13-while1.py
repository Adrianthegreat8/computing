#aibanez1:03/07/2024:A13-while1.py

#QA
mycolor = 'green'

#QB
incorrect_guesses=[]
while True:
    guess = input('Guess a color: \n')
    if guess == mycolor:
        print('correct\n')
        print('This is the list of wrong guesses:', incorrect_guesses)
        break
    incorrect_guesses.append(guess)
    print('Sorry, try again \n')