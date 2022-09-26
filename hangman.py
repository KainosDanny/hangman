# Importing the random library
import random
# File name then import the name of the variable
from word import words
import string

def getValidWord(words):
    # Randomly chooses a word from the list in the word.py
    word = random.choice(words)
    # Making sure that the word generated does not have either a space ' ' or a - in the word
    while '-' in word or ' ' in word:
        word = random.choice(words)
    # We are dealing with uppercase letter in this scenario since uppercase and lowercase letter are different when compared
    return word.upper()


def hangman():
    # Generate our word for our hangman game
    word = getValidWord(words)
    # Letters in the word
    wordLetter = set(word) 
    # Getting all the uppercase letters since we are dealing with uppercase words
    alphabet = set(string.ascii_uppercase)
    # Variable used to keep track of what letter the user has guessed
    usedLetter = set()
    # Essentially the player loses if they guessed it wrongly six times (game ends on the 6th attempt)
    lives = 6

    # When wordLetter reaches 0 it mean u have guessed the word :)
    while len(wordLetter) > 0 and lives > 0:
        # Message indicating how many lives you got left and what letter you have used
        # What join does = ' '.join(['a', 'b', 'cd']) --> a b cd and we used the , to separate each word/letter as seen below and then we add an space to them
        print('You have ', lives, ' lives left and you have used these letters: ', ' '.join(usedLetter))

        # What the current word is like (ie W-R-)
        wordList = [letter if letter in usedLetter else '-' for letter in word]
        print('Current word: ', ' '.join(wordList))

        # Getting user input
        userLetter = input('Guess a letter: ').upper()
        # Essentially checking if the user has entered a valid character and that character has not been used yet
        if userLetter in alphabet - usedLetter:
            usedLetter.add(userLetter)
            # If user guessed correctly on a letter remove that letter from the actual list 
            # 
            # change - to the actually letter
            if userLetter in wordLetter:
                wordLetter.remove(userLetter)
            else:
                lives -= 1
        elif userLetter in usedLetter:
            print('You have already used this letter. Please try again.')
        else:
            print('You have typed in an invalid leter! Please try again.')
    if(lives == 0):
        print('You have died, sorry. The word was ', word)
    else:
         print('You have guessed the word: ', word, '!!')
    

print(hangman())