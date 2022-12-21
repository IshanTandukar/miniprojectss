#hangman

import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)  #Randomly chooses a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():  
    word = get_valid_word(words)
    word_letters = set(word)  #Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  #What the user has guessed

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:  
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives,'lives left and you have used these letters: ',' '.join(used_letters))

        #What current word is (iw W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ",' '.join(word_list))

        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1 #Takes away a life if wrong    
                print('Letter is not a word. ')


        elif user_letter in used_letters:
            print("You have already used the character.Please try again")

        else:
            print('Invalid character. Please try again.')
    #gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print('You died,sorry.The word was',word)
    else:
        print('You guessed th word',word,'!!')    
             
hangman()



