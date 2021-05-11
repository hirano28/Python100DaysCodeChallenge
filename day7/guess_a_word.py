import random

wordList = ['Paçoca', 'Lasanha', 'Sorvete']
choosenWord = random.choice(wordList)
guess = input("Guess a letter: ")

for letter in choosenWord:
    if guess == letter:
        print('true')
    else:
        print('false')

print('Choosen Word: ' + choosenWord)