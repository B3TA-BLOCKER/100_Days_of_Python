from os import system
from Hangman_words import word_list
from Hangman_art import logo
import random
from Hangman_art import stages


system('cls')
print(logo)
# - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

live = word_length

display = []
for _ in range(word_length):
    display += "_"


end_of_game = False

while not end_of_game:
    # Asking the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    system('cls')
    print(logo)
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
        #If guess is not a letter in the chosen_word,
        #Then reduce 'lives' by 1. 
        #If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word :
        live -=1
        if live == 0 :
            end_of_game = True
            print("You Lose !! ")

        #Join all the elements in the list and turn it into a String.

    print(f"{' '.join(display)}")
    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[live])


for letter in chosen_word:
    if guess == letter :
        print(guess,end="")
    else:
        print(" _ ",end="")
