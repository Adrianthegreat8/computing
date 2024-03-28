#aibanez1:03/26/2024:wordle.py

#a
while True:
    x = input('Please input a 5-character word: ')
    if len(x) == 5:
        break
    else:
        print('You entered a', len(x), 'letter word. Try again.')

# your while loop should be here and should incorporate the input function provided below.                         
# if you cannot do this, leave your partial code as a comment                                        
# and just use the input functon as it is.

#b 
user = list(x)

word = 'exams'
target = list(word)

guess = list('-'*5)
notinword = []

# Your for loop should be here
for i in range(5):
    if user[i].lower() == target[i]:
        guess[i] = user[i].upper()
    elif user[i].lower() in target:
        guess[i] = user[i].lower()
    else:
        notinword.append(user[i])

#QC
print('Your word:', ' '.join(guess))
print('Not in word:', ' '.join(notinword))